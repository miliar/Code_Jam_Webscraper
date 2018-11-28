#include <iostream>
#include <cmath>
//standard libraries , reference available on www.cplusplusreference.com
using namespace std;
int main()
{
    int t=1;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int Oat=1,Bat=1,Oindex=0,Bindex=0,Olen=0,Blen=0,Pindex=0;
        int n;
        cin>>n;
        char Priority[n+1];
        int Oposlst[n+1],Bposlst[n+1];
        char in;
        int pos;
        for (int j=0;j<n;j++)
        {
            cin>>in;
            Priority[j]=in;
            cin>>pos;
            if(in == 'O')
            {
                Oposlst[Olen++]=pos;
            }
            else
            {
                Bposlst[Blen++]=pos;
            }
        }
        int steps=0,done=0;
        for(;Pindex<n;steps++)
        {
            if(Oat!=Oposlst[Oindex])
            {
                Oat+=(Oposlst[Oindex]-Oat) / fabs (Oposlst[Oindex]-Oat);
            }
            else if(Priority[Pindex]=='O' )
            {
                Oindex++;
                done=1;
            }

            if(Bat!=Bposlst[Bindex])
            {
                Bat+=(Bposlst[Bindex]-Bat) / fabs (Bposlst[Bindex]-Bat);
            }
            else if(Priority[Pindex]=='B')
            {
                Bindex++;
                done=1;

            }
            if(done){Pindex++;done=0;}
        }
        cout<<"Case #"<<i<<": "<<steps<<endl;
    }
return 0;
}
