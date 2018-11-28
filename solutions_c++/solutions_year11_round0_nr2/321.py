#include<iostream>
#include<cmath>
#include<algorithm>
#include<limits>
#include<vector>
#include<bitset>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<map>

using namespace std;

#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,FROM,n) for(int i=FROM;i<n;i++)
#define FORR(i,n) for(int i=n;i>=0;i--)
#define ll long long int
#define llu long long unsigned int


int t,n,d,c;

int ni()
{
    int temp;
    scanf("%d",&temp);
    return temp;
}

ll nl()
{
    ll temp;
    scanf("%lld",&temp);
    return temp;
}

llu nlu()
{
    llu temp;
    scanf("%llu",&temp);
    return temp;
}

float nf()
{
    float temp;
    scanf("%f",&temp);
    return temp;
}
/*
bool myfunction( const node& i, const node& j )    //use it to sort vectors
{
    if( i.x < j.x ) return false;
    if( j.x < i.x ) return true;
    return j.c < i.c;
}
*/

char sc[100][4],sd[100][4],s[200],stack[200];

int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

   scanf("%d",&t);
   for(int prob=0;prob<t;prob++)
   {
       c=ni();
       REP(i,c)
       scanf("%s",sc[i]);
       d=ni();
       REP(i,d)
       scanf("%s",sd[i]);
       n=ni();
       scanf("%s",s);
       stack[0]=s[0];
       int si=0;
       FOR(i,1,n)
       {
           int flag=0;
           if(si==-1)
           {
                stack[0]=s[i];
                si=0;
                continue;
           }

           REP(j,c)
           {
               if((stack[si]==sc[j][0] && s[i]==sc[j][1]) || (stack[si]==sc[j][1] && s[i]==sc[j][0]))
               {
                   stack[si]=sc[j][2];
                   flag=1;
                   break;
               }
           }
           if(flag)
           continue;
           REP(j,d)
           {
               REP(k,si+1)
               if((stack[k]==sd[j][0] && s[i]==sd[j][1]) || (stack[k]==sd[j][1] && s[i]==sd[j][0]))
               {
                   si=-1;
                   flag=1;
                   break;
               }
               if(flag)
               break;
           }
           if(flag)
           continue;
           stack[si+1]=s[i];
           si++;
       }
       printf("Case #%d: [",prob+1);
       REP(i,si)
       printf("%c, ",stack[i]);
       if(si!=-1)
       printf("%c]\n",stack[si]);
       else
       printf("]\n");
   }



   //system("pause");
   return 0;

}
