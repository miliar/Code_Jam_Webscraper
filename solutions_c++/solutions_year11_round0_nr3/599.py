#include <iostream>
#include <vector>
#include <algorithm>
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
        int r=0,m=1<<30,s=0;
        for(int n=0;n<N;++n)
        {
            int a;
            cin>>a;
            r ^=a;
            s +=a;
            m=(min)(m,a);

        }
        cout<<"Case #"<<(t+1)<<": ";
        if (!r)
            cout<<(s-m);
        else
            cout<<"NO";
        cout<<endl;
    }
    return 0;
}
