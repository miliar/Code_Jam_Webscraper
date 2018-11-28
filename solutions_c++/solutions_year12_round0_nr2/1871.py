#include <cstdio>
#include <string>
#include <iostream>
#include <set>
#include <cmath>
#include <cstdlib>
#include <map>
#include <algorithm>
using namespace std;

#define FILEIO
string _input="B-large.in";


int main()
{
#ifdef FILEIO
    freopen(_input.c_str(),"r",stdin);
    freopen((_input+".txt").c_str(), "w", stdout);
#endif

    int T; scanf("%d",&T);
    for(int IT=0;IT<T;IT++)
    {
        int n,s,p; scanf("%d%d%d",&n,&s,&p);
        int total[1000];
        for(int i=0;i<n;i++)scanf("%d",&total[i]);
        sort(total,total+n);
        int ts=0;
        int result=0;
        for(int i=n-1;i>=0;i--)
        {
            int x;
            x=(total[i])/3;
            if(x*3!=total[i])x+=1;
            if(x>=p)
            {
                result++;
                continue;
            }
            if(total[i]<2) continue;
            if(ts==s)continue;
            x=(total[i]-2)/3;
            x+=2;
            if(x>=p)
            {
                ts++;
                result++;
            }
        }
        printf("Case #%d: ", IT+1);
        printf("%d\n",result);
    }
    return 0;
}
