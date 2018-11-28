#include <map>
#include <set>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <bitset>
#include <vector>
#include <cstdio>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define abs(x) ((x) > 0 ? (x) : -(x))
typedef long long LL;

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int t;
    cin>>t;


    for (int i=1; i<=t; i++)
    {
        cout<<"Case #"<<i<<": ";

        int n, s, p;
        cin>>n>>s>>p;
        int kol = 0;
        for (int j=0; j<n; j++)
        {
            int sum;
            cin>>sum;
            if (sum >= 3*p - 2) kol++;
            else
            {
                if (sum>=3*p - 4 && sum>=2 && sum<=28)
                {
                    if (s>0)
                    {
                        s--;
                        kol++;
                    }
                }
            }
        }
        cout<<kol<<endl;
    }
    return 0;
}
