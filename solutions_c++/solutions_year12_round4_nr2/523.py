#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<ctime>
using namespace std;
int T,n,a,b,m;
long long xx[1010],yy[1010],r[1010];
long long gen(int k)
{
     return (long long)(1000000*(rand()%1000)+1000*(rand()%1000)+rand()%1000)%k;
     }
bool check(long long x,long long y,int k)
{
     for(int i=0;i<m;i++)
     {
          if((x-xx[i])*(x-xx[i])+(y-yy[i])*(y-yy[i])<(r[i]+r[k])*(r[i]+r[k]))
          return false;
          }
     return true;
     }
void create()
{
     m=0;
     while(m<n)
     {
          long long x=gen(a);
          long long y=gen(b);
          if(check(x,y,m))
          {
               xx[m]=x;
               yy[m]=y;
               m++;
               }
          }
     }
int main()
{
     freopen("B-small-attempt1.in","r",stdin);
     freopen("B-small-attempt1.out","w",stdout);

     srand(time(0));

     cin>>T;
     for(int t=1;t<=T;t++)
     {
          cin>>n>>a>>b;
          for(int i=0;i<n;i++)
          cin>>r[i];

          create();

          cout<<"Case #"<<t<<": ";
          for(int i=0;i<n;i++)
          cout<<xx[i]<<" "<<yy[i]<<" ";
          cout<<endl;
          }

     return 0;
     }
