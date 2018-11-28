#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

enum EEventType
{
    EVENT_DEPART,
    EVENT_ARRIVE
};

enum EStation
{
    STATION_A,
    STATION_B
};

struct SEvent
{
    pair<short, short> time;
    EEventType type;
    EStation station;
};

pair<short, short> addMinutes(short h, short m, short mAdd)
{
    m += mAdd;
    if (m >= 60)
    {
        h++;
        m -= 60;
    }

    return make_pair(h, m);
}

bool operator < (const SEvent& e1, const SEvent& e2)
{
    if (e1.time == e2.time)
        return (e1.type == EVENT_ARRIVE && e2.type == EVENT_DEPART);
    else
        return (e1.time < e2.time);
}

void main()
{
    int N = 0;
    cin >> N;
    
    int i;
    for(i = 0; i < N; i++)
    {
        int T = 0;
        cin >> T;

        int NA = 0;
        cin >> NA;
        
        int NB = 0;
        cin >> NB;

        vector<SEvent> timeline;

        int j;
        for(j = 0; j < NA; j++)
        {
            SEvent event;

            short h = 0;
            cin >> h;

            char delim = 0;
            cin >> delim;
            assert(delim == ':');

            short m = 0;
            cin >> m;

            event.time = make_pair(h, m);
            event.type = EVENT_DEPART;
            event.station = STATION_A;

            timeline.push_back(event);

            cin >> h;
            cin >> delim;
            assert(delim == ':');
            cin >> m;

            event.time = addMinutes(h, m, T);
            event.type = EVENT_ARRIVE;
            event.station = STATION_B;

            timeline.push_back(event);
        }

        for(j = 0; j < NB; j++)
        {
            SEvent event;

            short h = 0;
            cin >> h;

            char delim = 0;
            cin >> delim;
            assert(delim == ':');

            short m = 0;
            cin >> m;

            event.time = make_pair(h, m);
            event.type = EVENT_DEPART;
            event.station = STATION_B;

            timeline.push_back(event);

            cin >> h;
            cin >> delim;
            assert(delim == ':');
            cin >> m;

            event.time = addMinutes(h, m, T);
            event.type = EVENT_ARRIVE;
            event.station = STATION_A;

            timeline.push_back(event);
        }
       
        sort(timeline.begin(), timeline.end());

        int initialA = 0;
        int initialB = 0;
        int curA = 0;
        int curB = 0;

        vector<SEvent>::const_iterator it;
        for(it = timeline.begin(); it != timeline.end(); ++it)
        {
            if (it->station == STATION_A)
            {
                if (it->type == EVENT_DEPART)
                {
                    if (curA == 0)
                        initialA++;
                    else
                        curA--;
                }
                else
                {
                    curA++;
                }
            }
            else
            {
                if (it->type == EVENT_DEPART)
                {
                    if (curB == 0)
                        initialB++;
                    else
                        curB--;
                }
                else
                {
                    curB++;
                }
            }
        }
            
        cout << "Case #" << (i + 1) << ": " << initialA << " " << initialB << endl;
    }
}

