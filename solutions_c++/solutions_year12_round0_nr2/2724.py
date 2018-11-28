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

bool cmp(int x, int y)
{
    return x/3 > y/3;
}

int main()
{
	#ifndef ONLINE_JUDGE
        //freopen("input.txt","r",stdin);
        freopen("B-small-attempt1.in","r",stdin);
        freopen("output.txt","w",stdout);
	#endif

    int T;
    cin >> T;

    FOR(cs,1,T+1)
    {
        int N,S,p,t[111];

        cin >> N >> S >> p;
        rep(i,N) cin >> t[i];

        sort(t,t+N,cmp);

        int ans = 0;
        int dummy = 0;

        rep(i,N)
        {
            int d = t[i]/3;
            int r = t[i]%3;

            if(d +(r>0) >= p)
            {
                ++ans;
                if(r == 2 || r == 0) ++dummy;
            }
            else
            {
                if(!S) break;
                if(d==0) continue;

                if(r == 2 && p-d==2)
                    ++ans, --S;
                else  if(r == 0 && p-d==1)
                    ++ans, --S;
                else if(r==0 || r==2)
                    ++dummy;
            }
        }

        //assert(dummy >= S);

        printf("Case #%d: %d\n",cs,ans);
    }

	return 0;
}
