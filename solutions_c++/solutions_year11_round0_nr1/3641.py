#include <iostream>
#include <stdlib.h>
using namespace std;

int main()
{
    int i,j,T,N,akto,aktb,wto,wtb,t,ruch;
    char z;
    cin>>T;
    for(i=0;i<T;i++)
    {
        cin>>N;
        akto=1;
        aktb=1;
        t=0;
        wto=0;
        wtb=0;
        for(j=0;j<N;j++)
        {
            cin>>z;
            cin>>ruch;
            if(z=='O')
            {
                if(wto>=abs(ruch-akto))
                {
                t++;
                wtb++;
                wto=0;
                }
                else
                {
                    t+=(abs(ruch-akto)-wto+1);
                    wtb+=(abs(ruch-akto)-wto+1);
                    wto=0;
                }
                akto=ruch;
            }
            else
            {
                if(wtb>=abs(ruch-aktb))
                {
                t++;
                wto++;
                wtb=0;
                }
                else
                {
                    t+=(abs(ruch-aktb)-wtb+1);
                    wto+=(abs(ruch-aktb)-wtb+1);
                    wtb=0;
                }
                aktb=ruch;
            }
        }
        cout<<"Case #"<<i+1<<": "<<t<<endl;
    }
    return 0;
}
