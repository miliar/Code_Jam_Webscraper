#include <iostream>
#include <vector>
//#include <algorithm>
#include <stdlib.h>

using namespace std;

int main()
{
    int T;
    cin>>T;
    for(int t=0; t<T; ++t)
    {
        int N;
        cin>>N;
        vector<int> xs(N+1);
        for(int n=1;n<=N;++n)
        {
            int v;
            cin>>v;
            xs[n]=v;
        }
        int r=0;
        for(int n=1;n<=N;++n)
        {
            int i=xs[n];
            if (i==0)
                continue;
            int k=0;
            for(;i!=n;++k) 
            {
                int ni=xs[i];
                xs[i]=0;
                i=ni;
            }
            if (k) r+=k+1;
        }
        

        cout<<"Case #"<<(t+1)<<": "<<r<<".000000"<<endl;
    }
    return 0;
}
