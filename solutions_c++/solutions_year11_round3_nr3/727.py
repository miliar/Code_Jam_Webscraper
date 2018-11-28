#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    int T;
    cin>>T;
    for(int t=0;t<T;t++)
    {
        cout<<"Case #"<<t+1<<": ";

        int N, L, H;
        cin>>N>>L>>H;
        vector<int> f;
        for(int i=0;i<N;i++)
        {
            int x;
            cin>>x;
            f.push_back(x);
        }

        bool flag = true;
        int i=L;
        for(i;i<=H;i++)
        {
            if(flag)
            {
                flag = false;
            for(int j=0;j<f.size();j++)
            {
                if(f[j]%i!=0 && i%f[j]!=0)
                {
                    flag = true;
                    break;
                }
            }
            }
            else
            {
                break;
            }
        }
        if(flag)
        cout<<"NO"<<endl;
        else
            cout<<i-1<<endl;
    }

    return 0;
}
