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

#define sz(a) int((a).size())
#define ln(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define rep(i,s,n) for(int i=s; i<n; i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
using namespace std;

int solve()
{
    int N, S, P;
    cin>>N>>S>>P;
    vector<int> scores(N);
    int ret = 0;
    for(int i = 0; i < N; i++)
    {
        int score;
        cin>>score;
        if(score < P)
            continue;
        else if(score >= P + 2 * (P - 1))
            ret++;
        else if(P > 1 && score >= P + 2 * (P - 2) && S > 0)
        {
            S--;
            ret++;
        }
    }
    return ret;
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    cin>>T;
    for(int t = 1; t <= T; t++)
    {
        int ans = solve();
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}
