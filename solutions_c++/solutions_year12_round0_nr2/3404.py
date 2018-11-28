#include<iostream>
#include<list>
#include<string>
#include<cstring>
#include<sstream>
#include<cctype>
#include<string.h>
#include<algorithm>
#include<cmath>
#include<stack>
#include<fstream>
#include<cstdlib>
#include<vector>
#include<map>
#include<utility>
#include<iomanip>
#include<queue>
using namespace std;
#define clr(a) memset(a,0,sizeof(a))
#define fill(a,v) memset(a,v,sizeof(a))
#define PB push_back
#define pi acos(-1.0)
#define eps 1e-9


int main()
{
    int cnt,n,s,p,tc,kk=1,i,totalPoint;
    double avr;
    //freopen("B-large.in","r",stdin);
    //freopen("A-small-attempt.out","w",stdout);
    cin>>tc;
    while(tc--)
    {
     cnt=0;
     cin>>n>>s>>p;
     for(i=0;i<n;i++)
     {
         cin>>totalPoint;

         if(p==0)
         {
             cnt++;
             continue;
         }

         if(totalPoint==0)
         {
             continue;
         }

         if(totalPoint==1)
         {
             if(p==1)
             cnt++;
             continue;
         }

         if(totalPoint==2)
         {
             if(p==1)
             cnt++;
             else if(p==2 && s)
             {
                 cnt++;
                 s--;
             }
             continue;
         }
         avr=(double)totalPoint/3.0;
         if(p-avr>=1 && p-avr<1.5 && s)
         {
             cnt++;
             s--;
         }

         else if(p-avr<1)
         cnt++;
     }
     cout<<"Case #"<<kk++<<": "<<cnt<<endl;

    }
return 0;
}
