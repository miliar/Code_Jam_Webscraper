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
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int A,B;
    int t;
    int p;

    vector<bool> base;
    cin>>t;
    for (int i=1; i<=t; i++)
    {
        cin>>A>>B;
        cout<<"Case #"<<i<<": ";
        base.clear();
        base.resize(B+1,false);
        p = 10;

        LL kol = 0;

        while (p<=A) p*=10;
        p/=10;
        for (int j = A; j<=B; j++)
        {
            if (!base[j])
            {
                base[j] = true;
                int temp = j;
                int q=1;
                temp = (temp%p)*10 + temp/p;
                while (temp!=j)
                {
                    if (temp>=A && temp<=B)
                    {
                        q++;
                        base[temp] = true;
                    }
                    temp = (temp%p)*10 + temp/p;
                }
                kol+=(LL)q*(LL)(q-1)/2;
            }
        }
        cout<<kol<<endl;
    }
    return 0;
}
