#include <iostream>

using namespace std;

int main()
{
    int T, N, Po[100], Pb[100], i, j, time, o, b, opos, bpos, ot, bt, flag;
    char R[100];
    cin>>T;
    i=1;
    while(i<=T)
    {
        cin>>N;
        o=b=0;
        for(j=0; j<N; j++)
        {
            cin>>R[j];
            if(R[j]=='O')
            {
                cin>>Po[o];
                o++;
            }
            else
            {
                cin>>Pb[b];
                b++;
            }
        }
        opos=bpos=1;
        ot=bt=0;
        j=0;
        time=0;
        while(j<N)
        {
            flag=0;
            if(opos<Po[ot])
                opos++;
            else if(opos>Po[ot])
                opos--;
            else if(R[j]=='O')
            {
                flag=1;
                ot++;
            }
            if(bpos<Pb[bt])
                bpos++;
            else if(bpos>Pb[bt])
                bpos--;
            else if(R[j]=='B')
            {
                flag=1;
                bt++;
            }
            if(flag)
                j++;
            time++;
        }
        cout<<"Case #"<<i<<": "<<time<<endl;
        i++;
    }
    return 0;
}
