#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

#define EVT_DEPART_A    (0)
#define EVT_DEPART_B    (1)
#define EVT_ARRIVE_A    (2)
#define EVT_ARRIVE_B    (3)

struct EventSTR {
    int time;
    int type;
};

bool operator<(const EventSTR& a, const EventSTR& b) {
    if (a.time == b.time) {
        return (a.type > b.type);
    } else return (a.time < b.time);
}

vector<EventSTR> events;
vector<int> trainsInA;
vector<int> trainsInB;

int main() {
    int N, NA, NB, T;
    scanf("%d", &N);
    int i, j, k, m, n;
        
    for (i = 0; i < N; i++) {
        events.clear();
        
        printf("Case #%d: ", i+1);
        scanf("%d", &T);
        scanf("%d %d", &NA, &NB);
        for (j = 0; j < NA; j++) {
            scanf("%d:%d", &m, &n);
            EventSTR evt;
            evt.time = m * 60 + n;
            evt.type = EVT_DEPART_A;
            events.push_back(evt);
            
            scanf("%d:%d", &m, &n);
            evt.time = m * 60 + n;
            evt.type = EVT_ARRIVE_B;
            events.push_back(evt);
        }
        for (j = 0; j < NB; j++) {
            scanf("%d:%d", &m, &n);
            EventSTR evt;
            evt.time = m * 60 + n;
            evt.type = EVT_DEPART_B;
            events.push_back(evt);
            
            scanf("%d:%d", &m, &n);
            evt.time = m * 60 + n;
            evt.type = EVT_ARRIVE_A;
            events.push_back(evt);
        }
        
        sort(events.begin(), events.end());
        trainsInA.clear();
        trainsInB.clear();
        int fromA = 0, fromB = 0;
        for (j = 0; j < events.size(); j++) {
            EventSTR& evt = events[j];
            //printf("At time %d, %s %s\n", evt.time, (evt.type / 2) ? "ARRIVE" : "DEPART", (evt.type % 2) ? "B" : "A");
            switch (evt.type) {
            case EVT_DEPART_A:
                fromA++;
                for (k = 0; k < trainsInA.size(); k++) {
                    if (trainsInA[k] == -1) continue;
                    if (trainsInA[k] + T <= evt.time) {
                        trainsInA[k] = -1;
                        fromA--;
                        break;
                    }
                }                
                break;
            case EVT_DEPART_B:
                fromB++;
                for (k = 0; k < trainsInB.size(); k++) {
                    if (trainsInB[k] == -1) continue;
                    if (trainsInB[k] + T <= evt.time) {
                        trainsInB[k] = -1;
                        fromB--;
                        break;
                    }
                }
                break;
            case EVT_ARRIVE_A:
                trainsInA.push_back(evt.time);
                break;
            case EVT_ARRIVE_B:
                trainsInB.push_back(evt.time);
                break;
            }
        }
        printf("%d %d\n", fromA, fromB);
    }
}
