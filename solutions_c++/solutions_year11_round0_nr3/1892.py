#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int C[1005];

int main()
{
    int T;
    cin>>T;
    for (int cas=1; cas<=T; ++cas)
    {
        int N;
        cin>>N;
        int xorval = 0;
        int total = 0;
        for (int i=0; i<N; ++i)
        {
            cin>>C[i];
            xorval ^= C[i];
            total += C[i];
        }
        cout<<"Case #"<<cas<<": ";
        if (xorval)
        {
            cout<<"NO"<<endl;
        }
        else
        {
            sort(C, C+N);
            cout<<(total-C[0])<<endl;
        }
    }
    return 0;
}