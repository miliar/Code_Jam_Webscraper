#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int T,Ttotal, N, Ocurrent, dO, Osaved, Bcurrent, dB, Bsaved, total, dest;
    char temp;
    cin>>T;
    Ttotal=T;
    while(T--)
    {
        cin>>N;
        Ocurrent=Bcurrent=1;
        total = dO= Osaved= dB= Bsaved=0;
        while(N--)
        {
            cin>>temp>>dest;
            if(temp=='O')
            {
                dO = Ocurrent - dest;
                if(dO<0) dO = -dO;
                if(dO<=Osaved)
                {
                    total+=1;
                    Ocurrent = dest;
                    Bsaved += 1;
                    Osaved=0;
                }
                else
                {
                    Bsaved+=dO-Osaved+1;
                    total+=dO-Osaved+1;
                    Ocurrent = dest;
                    Osaved=0;
                }
            }
            else
            {
                dB = Bcurrent - dest;
                if(dB<0) dB = -dB;
                if(dB<=Bsaved)
                {
                    total+=1;
                    Bcurrent = dest;
                    Osaved += 1;
                    Bsaved=0;
                }
                else
                {
                    Osaved+=dB-Bsaved+1;
                    total+=dB-Bsaved+1;
                    Bcurrent = dest;
                    Bsaved=0;
                }
            }
        }
        cout<<"Case #"<<Ttotal-T<<": "<<total<<endl;
    }
    return 0;
}
