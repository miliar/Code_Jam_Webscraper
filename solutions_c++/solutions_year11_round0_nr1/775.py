#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int T, N;
int last_time[2], last_pos[2];
//o 0, b 1
int main()
{
    freopen("A-large.in", "r",stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++){
        scanf("%d", &N);
        last_time[0] = last_time[1] = 0;
        last_pos[0] = last_pos[1] = 1;
        char op[2];
        int pp;
        int stamp = 0;
        while(N--){
            scanf("%s%d", op, &pp);
            int now = (op[0]=='B');
            int next_time = last_time[now] + abs(last_pos[now]-pp)+1;
            if(next_time > stamp){
                stamp = next_time;
                last_time[now] = stamp;
                last_pos[now] = pp;
            } else{
                stamp++;
                last_time[now] = stamp;
                last_pos[now] = pp;
            }
        }
        printf("Case #%d: %d\n", cas, stamp);
    }
    return 0;
}

