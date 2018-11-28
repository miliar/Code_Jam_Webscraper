#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <cstring>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define FOR( i,a,b ) for(int i=a;i<b;i++)
#define NS string::npos
#define VI vector <int>
#define sz size
#define PI <int ,int >
#define CLEAR(cab) memset(cab,0,sizeof cab)
using namespace std;
int gcd(int a,int b)
{
    if(b==0)
    return 0;
    if(a%b==0)
    return b;

    return gcd(b,a%b);
}
int main()
{
   int test;
   map<int,int> m;


   freopen("input-large-1a.txt","r",stdin);
   freopen("output-large-1a.txt","w",stdout);
   scanf("%d",&test);
   int pd,pg,i=0;
   long long int n;
   int check;
   while(test--)
   {
       cin>>n>>pd>>pg;
       i++;
       if(pg==100)
       {
           if(pd==100)
           printf("Case #%d: Possible\n",i);
           else printf("Case #%d: Broken\n",i);
           continue;

       }
       if(pg==0)
       {
           if(pd==0)
           printf("Case #%d: Possible\n",i);
           else printf("Case #%d: Broken\n",i);
           continue;
       }

       if(n>=100)
       {
        printf("Case #%d: Possible\n",i);
        continue;
       }

       if(pd==0)
       {
        printf("Case #%d: Possible\n",i);
        continue;
       }

       int k=gcd(100,pd);
       int m=100/k;
       if(m<=n)
       {
        printf("Case #%d: Possible\n",i);
        continue;
       }
       else printf("Case #%d: Broken\n",i);

    }



return 0;
}

