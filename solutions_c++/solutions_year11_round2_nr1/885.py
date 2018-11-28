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


int t,n;

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
int a[100][100];
double wp[100],owp[100],oowp[100];
char s[1000];

int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);

   scanf("%d",&t);
   for(int prob=0;prob<t;prob++)
   {
       n=ni();
       REP(i,n)
       {
           wp[i]=0;
           owp[i]=0;
           oowp[i]=0;
       }

       REP(i,n)
       {
           scanf("%s",s);
           //cout<<s<<endl;
           REP(j,n)
           {
               if(s[j]=='.')
               a[i][j]=-1;
               else if(s[j]=='1')
               a[i][j]=1;
               else
               a[i][j]=0;
           }

       }
       REP(i,n)
       {
           double cnt=0,win=0;
           REP(j,n)
           {
               //cout<<a[i][j]<<endl;
               if(a[i][j]==1)
               {
                   win+=1;
                   cnt+=1;
               }
               else if(a[i][j]==0)
               cnt+=1;
           }
           //cout<<cnt<<" "<<win<<endl;
           wp[i]=win/cnt;
       }
       //REP(i,n)
       //cout<<wp[i]<<endl;


       REP(i,n)
       {
           double cnt2=0;

           REP(j,n)
           {
               if(a[i][j]!=-1)
               {
                   cnt2+=1;
                   double cnt=0,win=0;
                   REP(k,n)
                   {
                       if(k==i)
                       continue;
                       if(a[j][k]==1)
                       {
                           cnt+=1;
                           win+=1;
                       }
                       else if(a[j][k]==0)
                       cnt+=1;
                   }
                   owp[i]+=((win)/cnt);
               }
           }
           owp[i]/=cnt2;

       }




       REP(i,n)
       {
           double cnt3=0;
           REP(j,n)
           {
               if(a[i][j]!=-1)
               {
                   cnt3+=1;
                   //double cnt=0,win=0;

                   oowp[i]+=owp[j];
               }
           }
           //if(cnt3!=0)
           oowp[i]/=cnt3;
       }

       printf("Case #%d:\n",prob+1);
       REP(i,n)
       {
           printf("%.6lf\n",.25*wp[i]+.5*owp[i]+.25*oowp[i]);
       }


   }


   //system("pause");
   return 0;

}
