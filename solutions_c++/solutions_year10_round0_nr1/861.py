#include<iostream>
#include<cstdio>

using namespace std;

int T,N,K;

int main()
{
    cin>>T;

    for(int CASO=1;CASO<=T;CASO++)
    {
        cin>>N>>K;

        bool off=false;

        while(N--)
        {
            if(!(K&1))
            {
                off=true;
                break;
            }

            K>>=1;
        }

        printf("Case #%d: %s\n", CASO, (off ? "OFF" : "ON"));
    }
}
