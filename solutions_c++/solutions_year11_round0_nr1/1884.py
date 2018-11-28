#include <iostream>
#include <cstdio>
using namespace std;

#define abs(x) ((x)<0?-(x):(x))

int main()
{
    freopen("A-large.in", "rt", stdin);
    freopen("a.small.out", "wt", stdout);
    int T;
    cin>>T;
    for (int cas=1; cas<=T; ++cas)
    {
        int orange_cur = 1, blue_cur = 1;
        int orange_cur_time = 0, blue_cur_time = 0, universal_time = 0;
        int N;
        cin>>N;
        char col;
        int pos;
        for (int i=0; i<N; ++i)
        {
            cin>>col>>pos;
            if (col=='O')
            {
                int actual_move_time = abs(pos-orange_cur);
                int extra_time = universal_time-orange_cur_time;
                int universal_extra_time = max(actual_move_time-extra_time, 0);
                universal_time += universal_extra_time+1;
                orange_cur_time = universal_time;
                orange_cur = pos;
            }
            else if (col=='B')
            {
                int actual_move_time = abs(pos-blue_cur);
                int extra_time = universal_time-blue_cur_time;
                int universal_extra_time = max(actual_move_time-extra_time, 0);
                universal_time += universal_extra_time+1;
                blue_cur_time = universal_time;
                blue_cur = pos;
            }
        }
        printf("Case #%d: %d\n", cas, universal_time);
    }
    return 0;
}
