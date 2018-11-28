#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <math.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

int main()
{
    int T, t;
    cin >> T;
    for (t=0;t<T;++t)
    {
        uint64_t N, L, H,n;
        cin>>N>>L>>H;
        vector<uint64_t> fr(N);
        for(n=0;n<N;++n)
        {
            uint64_t freq;
            cin >> freq;
            fr[n]=freq;
        }
        cout<<"Case #"<<t+1<<": ";
        uint64_t i;
        for(i=L;i<=H;++i)
        {
            vector<int> divble(N,0);
            for(n=0;n<N;++n)
            {
                if(i%fr[n]==0||fr[n]%i==0) {
                    divble[n]=1;
                }
            }
            for(n=0;n<N;++n)
            {
                if(divble[n]==0)break;
            }
            if(n>=N){cout<<i;break;}
        }
        if(i>H)cout<<"NO";
        cout << endl;
    }

    return 0;
}
