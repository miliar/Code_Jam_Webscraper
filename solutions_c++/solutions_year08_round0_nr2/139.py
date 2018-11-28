#include <vector>
#include <iostream>
#include <map>
#include <functional>
#include <algorithm>
#include <list>
#include <string>
#include <sstream>
#include <bitset>
#include <cmath>
#include <iomanip>
#include <queue>
#include <set>
#include <stack>
#include <cassert>
using namespace std;

#define rep(i, size) \
    for (int i = 0; i < size; ++ i)


template <typename T>
T convert(const string & str){
    istringstream is(str);
    T r;
    is >> r;
    return r;
}


int getTime(string time){
    size_t i = time.find_first_of(':');
    time[i] = ' ';
    istringstream is(time);
    int a;
    int b;
    is >> a;
    is >> b;
    return a * 60 + b;
}


enum EventType{
    arrive_a,
    arrive_b,
    leave_a,
    leave_b,

};

struct Event
{
    Event(int time, EventType type){
        this->time = time;
        this->type = type;
    }
    int time;
    EventType type;
    friend bool operator > (const Event & a, const Event & b){
        return a.time > b.time ||
            ((a.time == b.time) && a.type > b.type);
    }
};

void solve(){
    int N;
    cin >> N;
    for (int n = 0; n < N; ++ n)
    {   
        int T;
        int NA;
        int NB;
        cin >> T >> NA >> NB;
        vector<int> A;
        vector<int> B;
        rep(i, NA){
            string tmp;
            cin >> tmp;
            A.push_back(getTime(tmp));
            cin >> tmp;
            A.push_back(getTime(tmp));
        }

        rep(i, NB){
            string tmp;
            cin >> tmp;
            B.push_back(getTime(tmp));
            cin >> tmp;
            B.push_back(getTime(tmp));
        }

        vector<Event> events;

        rep(i, NA){

            events.push_back(Event(A[i * 2], leave_a));
            events.push_back(Event(A[i * 2 + 1] + T, arrive_b));
        }

        rep(i, NB){
            events.push_back(Event(B[i * 2], leave_b));
            events.push_back(Event(B[i * 2 + 1] + T, arrive_a));
        }
        
        make_heap(events.begin(), events.end(), greater<Event>());
        
        int trainInA = 0;
        int trainInB = 0;
        int trainUsedA = 0;
        int trainUsedB = 0;

        while(true){
            if (events.size() == 0)
                break;
            Event e = events[0];

            pop_heap(events.begin(), events.end(), greater<Event>());
            events.pop_back();
            switch(e.type){
                case arrive_a:
                    trainInA ++;
                    break;
                case arrive_b:
                    trainInB ++;
                    break;
                case leave_a:
                    if (trainInA == 0)
                        trainUsedA ++;
                    else
                        trainInA --;
                    break;
                case leave_b:
                    if (trainInB == 0)
                        trainUsedB ++;
                    else
                        trainInB --;
                    break;
            }
        }
        cout << "Case #" << (n+1) << ": " << trainUsedA << " " << trainUsedB<< '\n';

    }
}