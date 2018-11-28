#include <iostream>
#include <stdlib.h>

using namespace std;

int main()
{
    int T;
    cin>>T;
    for(int t=0; t<T; ++t)
    {
        unsigned long N;
        cin>>N;
        int bs[2]={1,1};
        int ds[2]={0,0};
        int s=0;
        int pr=0;
        for(int n = 0;n<N; ++n)
        {
            char c;
            int b;
            cin>>c>>b;
            int nr=(c=='O')?0:1;
            if (nr!=pr)
            {
                s+=ds[pr];
                int d=abs(b-bs[nr]);
                ds[nr]=((ds[pr]<d)?(d-ds[pr]):0)+1;
                pr=nr;
            } else
            {
                ds[nr]+=abs(b-bs[nr])+1;
            }

            bs[nr]=b;
        }
        s+=ds[pr];
        cout<<"Case #"<<(t+1)<<": "<<s<<endl;
    }
    return 0;
}
