#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <ctime>
 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define rep(i,s,n) for(int i=s; i<n; i++)
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
 
const int INF = 1000000000;

using namespace std;

int con[1030];
int price[1030];
long long dp[1030][12];
int n;

long long solve(int ind, int skipped)
{
    if(dp[ind][skipped] != -1) return dp[ind][skipped];
    if(ind >= (n - 2) / 2)
    {
        int temp = ind - (n - 2)/2;
        int nSkip = min(con[2 * temp], con[2 * temp + 1]);
        if(nSkip < skipped) return dp[ind][skipped] = INF;
        if(nSkip == skipped) return dp[ind][skipped] = price[ind];
        return dp[ind][skipped] = 0;
    }
    long long cost = price[ind] + solve(2 * ind + 1, skipped) + solve(2 * ind + 2, skipped);
    cost = min(cost, solve(2 * ind + 1, skipped + 1) + solve(2 * ind + 2, skipped + 1));
    return dp[ind][skipped] = cost;
}

int main()
{
    int T;
    cin>>T;
    for(int t = 1; t <= T; t++)
    {
        int P;
        cin>>P;
        n = 1 << P;
        rep(i,0,n) cin>>con[i];
        rep(i,0,n) rep(j,0,P+1) dp[i][j] = -1;
        int nRead = n / 2;
        int pos = n - 1 - nRead;
        while(nRead)
        {
            rep(i,0,nRead) cin>>price[i + pos];
            nRead /= 2;
            pos -= nRead;
        }

        long long ans = solve(0,0);
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }

    return 0;
}

