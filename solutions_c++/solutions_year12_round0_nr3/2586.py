#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cmath>
#include <cstdio>
#include <cstdio>
#include <cstdlib>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <fstream>
#include <climits>

#define sz(a) int((a).size())
#define ln(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define rep(i,s,n) for(int i=s; i<n; i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
using namespace std;

int countDigits(int a)
{
    int ret = 0; 
    while(a)
    {
        ret++;
        a /= 10;
    }
    return ret;
}

long long solve()
{
    int A, B;
    cin>>A>>B;
    int nDigits = countDigits(A);
    long long factor = 1;
    for(int j = 0; j < nDigits - 1; j++)
        factor *= 10;
    long long ret = 0;
    for(int i = A; i <= B; i++)
    {
        set<int> s;
        int k = i;
        s.insert(k);
        for(int j = 0; j < nDigits - 1; j++)
        {
            int q = k / 10;
            int r = k % 10;
            k = r * factor + q; 
            if(k >= A && k <= B)
            {
                s.insert(k);
            }
        }
        int vmin = INT_MAX;
        tr(s,itr) vmin = min(vmin, *itr);

        if(i == vmin)
        {
            int cur = sz(s);
            ret += cur * (cur - 1) / 2;
        }
    }
    return ret;
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T;
    cin>>T;
    for(int t = 1; t <= T; t++)
    {
        long long ans = solve();
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}   
