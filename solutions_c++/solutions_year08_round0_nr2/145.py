#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct event
{
    int tm;
    int station;
    bool leave;

    event() {}
    event(int t, int s, bool l) : tm(t), station(s), leave(l) {}

    bool operator<(const event &b) const
    {
        if (tm != b.tm)
            return tm < b.tm;
        else
            return leave < b.leave;
    }
};

static int get_time()
{
    int h, m;
    scanf(" %d:%d", &h, &m);
    return h * 60 + m;
}

int main()
{
    int cases;
    scanf("%d", &cases);
    for (int cas = 0; cas < cases; cas++)
    {
        int T, A, B;
        vector<event> events;
        scanf("%d %d %d", &T, &A, &B);
        for (int i = 0; i < A + B; i++)
        {
            int dep = get_time();
            int arr = get_time() + T;
            events.push_back(event(dep, (i < A) ? 0 : 1, true));
            events.push_back(event(arr, (i < A) ? 1 : 0, false));
        }
        sort(events.begin(), events.end());

        int avail[2] = {0, 0};
        int ans[2] = {0, 0};
        for (size_t i = 0; i < events.size(); i++)
        {
            int st = events[i].station;
            if (events[i].leave)
            {
                if (avail[st] == 0)
                    ans[st]++;
                else
                    avail[st]--;
            }
            else
                avail[st]++;
        }
        cout << "Case #" << cas + 1 << ": " << ans[0] << " " << ans[1] << "\n";
    }
}
