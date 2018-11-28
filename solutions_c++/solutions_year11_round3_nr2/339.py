#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;


int main()
{
    freopen("in2.txt","r",stdin);
    freopen("out2.txt","w",stdout);
    int cases;
    scanf("%d",&cases);
    long long l, t, n;
    long c;
    long x;
    long long time = 0;
    long cur;
    long long ans = 0;
    vector<long> times;
    for(int ic=1;ic<cases+1;ic++)
    {
        times.clear();
        cin >> l >> t >> n >> c;
        vector<long> dist(n);
        for (long i = 0; i < c; i++)
        {
              cin >> x;
              for (long k = 0; k*c + i < n; k++)
              {
                  dist[k*c + i] = x;
              }
        }
        time = 0;
        ans = 0;
        for (cur = 0; cur < n && time < t; cur++)
        {
            ans += (dist[cur]<<1);
            time += (dist[cur]<<1);
        }
        times.assign(dist.begin() + cur, dist.end());
        if(ans>t)
        {
            ans = t;
            times.push_back((time-t)>>1);
        }
        sort(times.begin(), times.end(),greater<long>());
        time = 0;
        for (int i = 0; i < times.size(); i++)
        {
            if (time < l)
            {
                ans+=times[i];
                time++;
            }
            else
            {
                ans+=(times[i]<<1);
            }
        }
        printf("Case #%d: %lld\n",ic,ans);
    }
    return 0;
}
