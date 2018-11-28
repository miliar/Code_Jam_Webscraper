#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <algorithm>

using namespace std;

//#define DEBUG

#ifdef DEBUG
#define DPRINT printf
#else
#define DPRINT ignore
#endif

// Event types
#define START_AT_A 1
#define START_AT_B 2
#define END_AT_A   3
#define END_AT_B   4

ofstream out;

bool isWhiteSpace(char ch)
{
    switch (ch) {
        case ' ':
        case '\t':
        case '\n':
        case '\r':
            return true;
            break;
        default:
            return false;
    }
}

void proceed(ifstream &f)
{
    while (isWhiteSpace(f.peek()))
        f.get();
}

void ignore(const char * c, ...)
{

}

/* Class to store hours and minutes in 24 hour format */
class Time {
    public:
        Time() 
        {
            hour = 0;
            min = 0;
        }

        Time(int h, int m) : hour(h), min(m)
        {
        }

        /* String should be in format (hh:mm) */
        Time(char *t_str)
        {
            setTime(t_str);
        }

        void setTime(char *t_str)
        {
            char *h = strtok(t_str, ":");
            char *m = strtok(NULL, ":");
            hour = atoi(h);
            min = atoi(m);
            //DPRINT("Time(): string = %s, hour = %d, min = %d\n", t_str, hour, min);
        }

        Time& operator=(const Time &t)
        {
            hour = t.hour;
            min = t.min;
            return *this;
        }

        Time operator+(const Time &t)
        {
            hour = hour + t.hour;
            min = min + t.min;
            if (min >= 60) {
                min -= 60;
                hour++;
            }
            return *this;
        }

        bool operator<(const Time &t) const
        {
            if (hour < t.hour)
                return true;
            else if ((hour == t.hour) && (min < t.min))
                return true;
            else
                return false;
        }

        bool operator==(const Time &t) const
        {
            return ((hour == t.hour) && (min == t.min));
        }

        int getHour()
        {
            return hour;
        }

        int getMin()
        {
            return min;
        }

    private:
        int hour;
        int min;
};

class Event {
    public:
        bool operator<(const Event &e) const
        {
            // If time is same, then give lower preference to departure events
            if (time == e.time) {
                if ((e.type == START_AT_A) || (e.type == START_AT_B)) {
                    return true;
                } else {
                    return false;
                }
            } else {
                return (time < e.time);
            }
        }

        Event& operator=(const Event &e)
        {
            type = e.type;
            time = e.time;
            return *this;
        }

        bool operator==(const Event &e) const
        {
            return ((time == e.time) && (type == e.type));
        }

        int type;
        Time time;
};

int trainsAtA;
int trainsAtB;
int trainsStartedAtA;
int trainsStartedAtB;
typedef list<Event> EventList;
EventList eventList;

void printOut(int caseNo)
{
    cout << "Case #" << caseNo << ": " << trainsStartedAtA << " " << trainsStartedAtB << endl;
}

void printEventList()
{
    EventList::iterator iter;
    for (iter = eventList.begin(); iter != eventList.end(); iter++) {
        Event e = *iter;
        DPRINT("Event type: %d, time: %d:%d\n", e.type, e.time.getHour(), e.time.getMin());
    }
}

// The actual algorithm is implemented here. We use a sweep line to sweep across
// the event in the order of increasing time
void getTrainsCount()
{
    trainsAtA = 0;
    trainsAtB = 0;
    trainsStartedAtA = 0;
    trainsStartedAtB = 0;

    eventList.sort();
    printEventList();
    EventList::iterator iter;
    for (iter = eventList.begin(); iter != eventList.end(); iter++) {
        Event currEvent = (*iter);
        switch (currEvent.type) {
            case START_AT_A:
                if (trainsAtA > 0)
                    trainsAtA--;
                else
                    trainsStartedAtA++;

                break;

            case START_AT_B:
                if (trainsAtB > 0)
                    trainsAtB--;
                else
                    trainsStartedAtB++;

                break;

            case END_AT_A:
                trainsAtA++;
                break;

            case END_AT_B:
                trainsAtB++;
                break;
            default:
                break;
        }
    }
}

int main(int argc, char *argv[])
{
    if (argc != 2) {
        cerr << "Usage: TrainTimeTable <input_file.in>\n";
        exit(-1);
    }

    ifstream fin(argv[1]);
    if (!fin) {
        cerr << "Failed to open input file: " << argv[1] << endl;
        exit(-1);
    }

    out.open("output.out");

    int N;
    fin >> N;
    DPRINT("Number of inputs: %d\n", N);
    int caseNo = 1;
    while (N > 0) {
        eventList.clear();
        int turnAroundTime;
        fin >> turnAroundTime;
        int AtoB, BtoA;
        fin >> AtoB >> BtoA;
        DPRINT("************* Case No: %d **************\n", caseNo);
        DPRINT("%d %d %d\n", turnAroundTime, AtoB, BtoA);
        char t_str[6];
        while (AtoB > 0) {
            // Start of train
            proceed(fin);
            fin.read(t_str, 5);
            t_str[5] = '\0';
            Time t_start(t_str);
            Event e;
            e.time = t_start;
            e.type = START_AT_A;
            eventList.push_back(e);

            // End of train
            proceed(fin);
            fin.read(t_str, 5);
            t_str[5] = '\0';
            Time t_end(t_str);
            Time delay(0, turnAroundTime);
            e.time = t_end + delay;
            e.type = END_AT_B;
            eventList.push_back(e);

            AtoB--;
        }
        
        while (BtoA > 0) {
            // Start of train
            proceed(fin);
            fin.read(t_str, 5);
            t_str[5] = '\0';
            Time t_start(t_str);
            Event e;
            e.time = t_start;
            e.type = START_AT_B;
            eventList.push_back(e);

            // End of train
            proceed(fin);
            fin.read(t_str, 5);
            t_str[5] = '\0';
            Time t_end(t_str);
            Time delay(0, turnAroundTime);
            e.time = t_end + delay;
            e.type = END_AT_A;
            eventList.push_back(e);

            BtoA--;
        }

        getTrainsCount();
        printOut(caseNo);
        caseNo++;
        N--;
    }

    fin.close();

    return 0;
}
