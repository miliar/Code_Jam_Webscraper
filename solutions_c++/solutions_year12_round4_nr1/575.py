#include<iostream>
#include<algorithm>
using namespace std;
int T;
int n,d;
int a[10010],b[10010],dis[10010];
int main()
{
     freopen("A-large.in","r",stdin);
     freopen("A-large.out","w",stdout);

     cin>>T;
     for(int t=1;t<=T;t++)
     {
          cin>>n;
          for(int i=0;i<n;i++)
          cin>>a[i]>>b[i];
          cin>>d;

          int nn=-1;
          int tail=1;
          dis[0]=2*a[0];
          for(int head=0;;head++)
          {
               while(tail<n&&a[tail]<=dis[head])
               {
                    dis[tail]=a[tail]+min(b[tail],a[tail]-a[head]);
                    //cout<<a[tail]<<" "<<b[tail]<<" D "<<dis<<endl;
                    tail++;
                    }
               if(tail==head+1)
               {
                    nn=head;
                    break;
                    }
               }

          int dd=0;
          for(int i=0;i<=nn;i++)
          dd=max(dd,dis[i]);

          if(dd>=d)
          cout<<"Case #"<<t<<": YES"<<endl;
          else
          cout<<"Case #"<<t<<": NO"<<endl;
          }

     return 0;
     }
