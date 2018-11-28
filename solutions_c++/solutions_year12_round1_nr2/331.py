#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <math.h>
#include <set>
using namespace std;
int a[1001], b[1001], s[1001], stars;

int ns(int i)
{
    int r=0;
    if(s[i]==0 && a[i]<=stars)
    r++;
    if(s[i]<2 && b[i]<=stars)
    r++;
    return r;
}

int better(int i, int j)
{
    int si=ns(i), sj=ns(j);
    if(si>sj)
    return i;
    if(sj>si)
    return j;

    if(sj==1)
    {
        if(s[j]==1)
        return j;
        if(s[j]==0 && s[i]==0 && b[j]>b[i])
        return j;
    }

    return i;
}

int main()
{
    freopen("testB.in","r",stdin);
    freopen("testB.out","w",stdout);

    int T;
    cin >> T;

    for(int tc=1; tc<=T; tc++)
    {
        int N;
        cin >> N;

        for(int i=0; i<N; i++)
        cin >> a[i+1] >> b[i+1];
        a[0]=10000; b[0]=10000;

        for(int i=0; i<=N; i++)
        s[i]=0;

        stars=0; int levels=0, flag=0;
        while(stars<2*N)
        {
            int best=0;
            for(int i=0; i<=N; i++)
            best=better(best,i);

            int inc=ns(best);
            if(inc==0)
            {
                printf("Case #%i: Too Bad\n", tc);
                stars=2*N;
                flag=1;
            }
            levels++;
            s[best]+=inc;
            stars+=inc;
        }

        if(!flag)
        printf("Case #%i: %i\n", tc, levels);

    }
    return 0;
}

