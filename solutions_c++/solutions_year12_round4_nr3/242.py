#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<ctime>
using namespace std;
long long hi[2010],a[2010];
int T,n;
long long gen()
{
     return (long long)(1000000*(rand()%1000)+1000*(rand()%1000)+rand()%1000);
     }
bool check()
{
     for(int i=1;i<n;i++)
     {
          int j=hi[i];
          for(int x=i+1;x<j;x++)
          {
               if((j-i)*(a[x]-a[i])>=(x-i)*(a[j]-a[i]))
               return false;
               }
          for(int x=j+1;x<=n;x++)
          {
               if((j-i)*(a[x]-a[i])>(x-i)*(a[j]-a[i]))
               return false;
               }
          }
     return true;
     }
bool create()
{
     for(int i=1;i<=n;i++)
     a[i]=gen();

     return check();
     }
int main()
{
     freopen("C-small-attempt2.in","r",stdin);
     freopen("C-small-attempt2.out","w",stdout);

     cin>>T;
     for(int t=1;t<=T;t++)
     {
          cin>>n;
          for(int i=1;i<n;i++)
          cin>>hi[i];

          bool im=false;
          for(int i=1;i<=n;i++)
          {
               for(int j=i+1;j<hi[i];j++)
               {
                    if(hi[j]>hi[i])
                    im=true;
                    }
               }

          if(im)
          {
               cout<<"Case #"<<t<<": Impossible"<<endl;
               continue;
               }

          bool success=false;
          for(int i=0;i<1000000;i++)
          {
               bool p=create();
               if(p)
               {
                    cout<<"Case #"<<t<<": ";
                    for(int j=1;j<=n;j++)
                    cout<<a[j]<<" ";
                    cout<<endl;
                    success=true;
                    break;
                    }
               }
          if(!success)
          cout<<"Case #"<<t<<": Dafuq"<<endl;
          }

     return 0;
     }
