#include <iostream>
#include <string>
#include <queue>

using namespace std;

int minutes(const string& t)
{
    int h = (t[0] - '0') * 10 + (t[1] - '0');
    int m = (t[3] - '0') * 10 + (t[4] - '0');
    return h * 60 + m;
}

struct Event
{
    int sta, dep, arv, rdy;

    Event(int s, int d, int a)
        : sta(s), dep(d), arv(a) {}

    bool operator<(Event rhs) const {
        if (dep != rhs.dep)
            return dep > rhs.dep;
        if (arv != rhs.arv)
            return arv > rhs.arv;
        return sta > rhs.sta;
    }
};

Event depEvent(int sta, int dep, int arv)
{
    return Event(sta, dep, arv);
}

Event readyEvent(int sta, int rdy)
{
    return Event(sta, rdy, -1);
}

int main()
{
    int cases;
    cin >> cases;

    for (int cs = 0; cs < cases; ++cs) {
        int turnaround;
        cin >> turnaround;

        int na, nb;
        cin >> na >> nb;

        priority_queue<Event> events;
        for (int i = 0; i < na; ++i) {
            string dep, arv;
            cin >> dep >> arv;
            events.push(depEvent(0, minutes(dep), minutes(arv)));
        }
        for (int i = 0; i < nb; ++i) {
            string dep, arv;
            cin >> dep >> arv;
            events.push(depEvent(1, minutes(dep), minutes(arv)));
        }

        int start[2] = { 0, 0 };
        int ready[2] = { 0, 0 };
        while (!events.empty()) {
            Event event = events.top();
            events.pop();
            if (event.arv == -1) {
                ++ready[event.sta];
            }
            else {
                int sta = event.sta;
                int arv = event.arv;
                if (ready[sta] == 0) {
                    ++start[sta];
                    ++ready[sta];
                }
                --ready[sta];
                events.push(readyEvent(1 - sta, arv + turnaround));
            }
        }

        cout << "Case #" << cs + 1 << ": " << start[0] << ' ' << start[1]
             << '\n';
    }

    return 0;
}
