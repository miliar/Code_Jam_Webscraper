#include <iostream>
using namespace std;
int Oat,Bat,Otime,Btime;
char c;
int t,n,p;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    cin>>t;
    int i=1;
    while (i<=t)
    {
          Oat=Bat=1,Otime=Btime=0;
          cin>>n;
          while (n--)
          {
                cin>>c;
                cin>>p;
                if (c=='O')
                {
                           Otime+=abs(Oat-p);
                           Oat=p;
                           Otime=max(Otime,Btime);
                           ++Otime;
                }
                else
                {
                           Btime+=abs(Bat-p);
                           Bat=p;
                           Btime=max(Btime,Otime);
                           ++Btime;
                }
          }
          cout<<"Case #"<<i<<": "<<max(Otime,Btime)<<endl;
          ++i;
    }
    return 0;
}
