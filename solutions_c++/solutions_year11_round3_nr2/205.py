#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int a[1000003];

bool comp(int i,int j) { return (i>j); }

int main()
{
    freopen("B-large.in", "rt", stdin);
    freopen("out.txt", "wt", stdout);
    int T, L, N, C;
    long long t;
    cin>>T;
    for (int cas=1; cas<=T; ++cas)
    {
        cin>>L>>t>>N>>C;
        for (int i=0; i<C; ++i)
        {
            cin>>a[i];
        }
        for (int j=C; j<N; j+=C)
        {
            for (int i=0; i<C; ++i)
            {
                a[i+j] = a[i];
            }
        }
        long long time = 0;
        int i;
        for (i=0; i<N; ++i)
        {
            if (time+2*a[i]<=t)
            {
                time += 2*a[i];
                continue;
            }
            else
            {
                long long extra = t-time;
                if (extra & 1) ++extra;
                a[i] -= extra/2;
                time = t;
                break;
            }
        }
        sort(a+i, a+N, comp);
        for (int j=0; j<L && i<N; ++j, ++i)
        {
            time += a[i];
        }
        for (; i<N; ++i)
        {
            time += 2*a[i];
        }
        printf("Case #%d: ", cas);
        cout<<time<<endl;
    }
    return 0;
}
