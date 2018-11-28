#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <numeric>
#include <memory.h>
#include <cstdio>
#include <assert.h>

using namespace std;

#define pb push_back
#define INF 101111111
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define rep(i,n) FOR(i,0,n)
#define ford(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define CL(a,v) memset((a),(v),sizeof(a))
#define mp make_pair
#define X first
#define Y second
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> pii;

int main()
{
	#ifndef ONLINE_JUDGE
//        freopen("input.txt","r",stdin);
//        freopen("C-small-attempt0.in","r",stdin);
        freopen("C-large.in","r",stdin);
        freopen("output.txt","w",stdout);
	#endif

    int T;
    cin >> T;

    bool was[2002000];

    FOR(cs,1,T+1)
    {
        int A,B;
        cin >> A >> B;

        CL(was,0);
        ll ans = 0;

        for(int x = max(A,12); x <= min(B,2000000-1); ++x) if(!was[x])
        {
            was[x] = true;

            int sz = 0, cnt = 1, y = x, m = 1;

            for(int t = x; t; t /= 10) sz ++;

            rep(i,sz-1) m *= 10;

            rep(i,sz-1)
            {
                int t = (y/m);
                y = y - t*m;
                y = y*10+t;
                if((y/m)>0 && A <= y && y <= B && was[y] == false)
                {
                    cnt ++;
                    was[y] = true;
                }
            }

            ans += (ll)cnt*(cnt-1)/2;
        }

        printf("Case #%d: ",cs);
        cout << ans << endl;
    }

	return 0;
}
