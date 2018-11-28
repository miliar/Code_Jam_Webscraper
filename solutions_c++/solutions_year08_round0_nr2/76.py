#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

struct event {
    int inc;
    int side;
    int time;
    bool operator<(const event& e) const { return time < e.time or (time == e.time and inc > e.inc); }
};

event events[400];

int read_time() {
    string str;
    cin >> str;
    return (str[0]-'0')*600 + (str[1]-'0')*60 + (str[3]-'0')*10 + (str[4]-'0');
}

int main(void) {

    int N;
    cin >> N;
    for(int C=0;C<N;++C) {
        int wait_time, NA, NB, E;
        cin >> wait_time >> NA >> NB;
        E = 0;
        for(int i=0;i<NA;i++) {
            events[E].inc = -1;
            events[E].side = 0;
            events[E].time = read_time();
            ++E;
            events[E].inc = 1;
            events[E].side = 1;
            events[E].time = read_time() + wait_time;
            ++E;
        }
        for(int i=0;i<NB;i++) {
            events[E].inc = -1;
            events[E].side = 1;
            events[E].time = read_time();
            ++E;
            events[E].inc = 1;
            events[E].side = 0;
            events[E].time = read_time() + wait_time;
            ++E;
        }
        sort(events, events+E);
        int initial[2], trains[2];
        initial[0]=initial[1]=0;
        trains[0]=trains[1]=0;
        for(int i=0;i<E;++i) {
            int side = events[i].side;
            int inc = events[i].inc;
            trains[side] += inc;
            if(trains[side] < 0) {
                trains[side]++;
                initial[side]++;
            }
        }
        cout << "Case #" << C+1 << ": " << initial[0] << " " << initial[1] << endl;
    }
    return 0;
}
