#include <cstdio>
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <stdexcept>
#include <vector>
#include <map>

using namespace std;


enum Station
{
    A = 0,
    B = 1
};


enum State
{
    LEAVE = 0,
    ARRIVE = 1
};


struct Event
{
    enum Station m_Station;
    enum State m_State;

    Event() : m_Station(A), m_State(LEAVE) {}
    Event(const Event& evt) : m_Station(evt.m_Station), m_State(evt.m_State) {}
    Event(enum Station statn, enum State state) : m_Station(statn), m_State(state) {}

    Event& operator= (const Event& evt) 
    { 
        m_Station = evt.m_Station;
        m_State = evt.m_State;
        return *this;
    }

   
};

class Schedule
{
    private:
        map<int, vector<Event>*> m_Events;
        int m_a;
        int m_b;
        int m_MaxA;
        int m_MaxB;
        int m_ServTime;

        void BringArriveEventsFirst(vector<Event>* vec_ptr);

    public:
        Schedule() : m_a(0), m_b(0), m_MaxA(0), m_MaxB(0), m_ServTime(0) {}
        void Clear();
        void SetServiceTime(int time) { m_ServTime = time; }
        void InsertEvent(int time, Event evt);
        void Solve();
        int GetANumTrains() { return m_MaxA; }
        int GetBNumTrains() { return m_MaxB; }
        ~Schedule() { Clear(); }
};

void Schedule::Clear()
{
    for (map<int, vector<Event>*>::iterator mi = m_Events.begin(); mi != m_Events.end(); ++mi)
    {
        delete mi->second;
    }
    m_Events.clear();
    m_ServTime = 0;
    m_a = 0;
    m_b = 0;
    m_MaxA = 0;
    m_MaxB = 0;
}

void Schedule::InsertEvent(int time, Event evt)
{
    if (evt.m_State == ARRIVE)
        time += m_ServTime;

    map<int, vector<Event>*>::iterator mi = m_Events.find(time);
    if (mi == m_Events.end())
    {
        vector<Event>* vec_ptr = new vector<Event> ();
        vec_ptr->push_back(evt);
        m_Events.insert(pair<int, vector<Event>*> (time, vec_ptr));
        return;
    }

    mi->second->push_back(evt);
}

void Schedule::BringArriveEventsFirst(vector<Event>* vec_ptr)
{
    if (vec_ptr->size() < 2)
        return;

    vector<Event> reorder;
    for (int i = 0; i < vec_ptr->size(); ++i)
    {
        if (vec_ptr->at(i).m_State == ARRIVE)
            reorder.push_back(vec_ptr->at(i));
    }
    for (int i = 0; i < vec_ptr->size(); ++i)
    {
        if (vec_ptr->at(i).m_State != ARRIVE)
            reorder.push_back(vec_ptr->at(i));
    }

    vec_ptr->clear();
    for (int i = 0; i < reorder.size(); ++i)
    {
        vec_ptr->push_back(reorder[i]);
    }
}


void Schedule::Solve()
{
    m_a = 0;
    m_b = 0;
    m_MaxA = 0;
    m_MaxB = 0;

    vector<Event>* vec_ptr;
    
    for (map<int, vector<Event>*>::iterator mi = m_Events.begin(); mi != m_Events.end(); ++mi)
    {
        //cout << mi->first << endl;
        vec_ptr = mi->second;
        BringArriveEventsFirst(vec_ptr);
        for (int i = 0; i < vec_ptr->size(); ++i)
        {
            const Event& evt = vec_ptr->at(i);
            if (evt.m_Station == A)
            {
                if (evt.m_State == LEAVE)
                {
                    if (m_a == 0)
                    {
                        m_MaxA += 1;
                    }
                    else
                        --m_a;
                }
                else
                {
                    ++m_a;
                }
            }
            else // station B 
            {
                if (evt.m_State == LEAVE)
                {
                    if (m_b == 0)
                    {
                        m_MaxB += 1;
                    }
                    else
                        --m_b;
                }
                else
                {
                    ++m_b;
                }                
            }
        }
    }
}

void ParseFile(const char* input_file, const char* output_file)
{
    ifstream in_file(input_file, ios_base::in);
    if (!in_file)
    {
        cerr << input_file << " could not be opened" << endl;
        return;
    }

    ofstream out_file(output_file, ios_base::out);
    if (!out_file)
    {
        cerr << output_file << " could not be opened" << endl;
        in_file.close();
        return;
    }

    int num_lines = 0, service_time, num_trips_a, num_trips_b;
    int hrs_1, mins_1, hrs_2, mins_2, tim;
    Schedule sc;
    Event evt;

    string line;
    getline(in_file, line);
    istringstream str_stream(line);
    str_stream >> num_lines;
    for (int i = 0; i < num_lines; ++i)
    {
        sc.Clear();
        line.clear();
        getline(in_file, line);
        istringstream strm(line);
        strm >> service_time;
        sc.SetServiceTime(service_time);
        line.clear();
        getline(in_file, line);
        istringstream strm2(line);
        strm2 >> num_trips_a >> num_trips_b;
        
        for (int j = 0; j < num_trips_a; ++j)
        {
            line.clear();
            getline(in_file, line);
            if (sscanf(line.c_str(), "%d:%d %d:%d", &hrs_1, &mins_1, &hrs_2, &mins_2) == 4)
            {
                evt.m_Station = A;
                evt.m_State = LEAVE;
                tim = 60*hrs_1 + mins_1;
                sc.InsertEvent(tim, evt);

                evt.m_Station = B;
                evt.m_State = ARRIVE;
                tim = 60*hrs_2 + mins_2;
                sc.InsertEvent(tim, evt);
            }
            else
            {
                cout << "error with line " << line << endl;
            }
        }

        for (int j = 0; j < num_trips_b; ++j)
        {
            line.clear();
            getline(in_file, line);
            if (sscanf(line.c_str(), "%d:%d %d:%d", &hrs_1, &mins_1, &hrs_2, &mins_2) == 4)
            {
                evt.m_Station = B;
                evt.m_State = LEAVE;
                tim = 60*hrs_1 + mins_1;
                sc.InsertEvent(tim, evt);

                evt.m_Station = A;
                evt.m_State = ARRIVE;
                tim = 60*hrs_2 + mins_2;
                sc.InsertEvent(tim, evt);
            }
            else
            {
                cout << "error with line " << line << endl;
            }
        }

        sc.Solve();

        out_file << "Case #" << (i+1) << ": " << sc.GetANumTrains() << " " << sc.GetBNumTrains() << endl;
    }

    in_file.close();
    out_file.close();

    return;
}

int main(int argc, const char** argv)
{
    if (argc != 3)
    {
        cerr << "Invocation: " << argv[0] << " <input_file> <output_file>" << endl;
        return 1;
    }

    ParseFile(argv[1], argv[2]);
    return 0;
}

