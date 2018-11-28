#include<iostream>
#include<fstream>
#include<stdio.h>
using namespace std;

int main()
{
    int T, R, k, N, ans, a[1111], now, tot, group;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        scanf("%d%d%d",&R , &k, &N);
        for (int i = 0; i < N; ++i) 
            scanf("%d",&a[i]);
        
        ans = 0;
        now = N - 1;
        while(R--) {
            tot = 0; group = 0;
            while (tot <= k && group <= N) {
                now = (now + 1)%N;
                tot += a[now];
                group++;
            //    printf("%d_%d_%d_\n", now, tot, group);
            }
            ans += tot - a[now % N];
            now = (now + N - 1) % N;
            //cout << ans << endl;
        }
        cout << "Case #"<< t << ": " << ans <<endl;
    }
}
