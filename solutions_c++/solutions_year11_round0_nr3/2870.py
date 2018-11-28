#include<assert.h>
#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>
#include<cstring>

using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size

typedef long long INT;

#define sf scanf
#define pf printf


int main()
{

 //freopen("sample.in","r",stdin);

 freopen("c.in","r",stdin);
 freopen("c.ans","w",stdout);

 int t;
 sf("%d",&t);
 int kase=1;
 while(t--)
 {
     int cand[1000];
     int n,i;
     int total=0;
     sf("%d",&n);
     for(i=0;i<n;i++)
        sf("%d",&cand[i]), total += cand[i];
     int maxTake=-1;
     int count;
     for(count=1;count<(1<<n); count++)
     {
         int little=0;
         int big=0;
         int bigreal=0;
         for(i=0;i<n;i++)
            if ( (count & (1<<i) ) >0)
                little = (little ^ cand[i]);
            else
                big= (big^cand[i]), bigreal += cand[i];

        if ( big == little)
            if ( bigreal>maxTake)
                maxTake = bigreal;

     }
     pf("Case #%d: ",kase++);
     if ( maxTake == -1)
        pf("NO\n");
    else
        pf("%d\n",maxTake);
 }
 return 0;
}
