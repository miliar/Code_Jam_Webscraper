#include<iostream>
#include<math.h>
using namespace std;
int main()
{
    int T, N, Pi, BP, OP, Bwait, Owait, time, t1;
    char Ri;
    cin>>T;
    for(int i=0;i<T;i++)
    {
            cin>>N;
            BP=OP=1;
            Bwait=Owait=0;
            time=0;
            for(int j=0;j<N;j++)
            {
                    cin>>Ri;
                    cin>>Pi;
                    if(Ri=='O')
                    {
                               t1=abs(Pi-OP);
                               if(t1>Owait)
                               {
                                           time=time+t1-Owait+1;
                                           Bwait=Bwait+t1-Owait+1;
                               }
                               else
                               {
                                   time=time+1;
                                   Bwait=Bwait+1;
                               }
                               Owait=0;
                               OP=Pi;
                    }
                    if(Ri=='B')
                    {
                               t1=abs(Pi-BP);
                               if(t1>Bwait)
                               {
                                           time=time+t1-Bwait+1;
                                           Owait=Owait+t1-Bwait+1;
                               }
                               else
                               {
                                   time=time+1;
                                   Owait=Owait+1;
                               }
                               Bwait=0;
                               BP=Pi;
                    }
            }
            cout<<"Case #"<<i+1<<": "<<time<<"\n";
    }
    return 0;
}
                    
                   
                               
