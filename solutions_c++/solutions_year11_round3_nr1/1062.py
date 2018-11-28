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

int R,C;
char B[55][55];
char A[55][55];


bool solve()
{
    CL(A,'?');

    rep(r,R-1) rep(c,C-1)
    {
        if(B[r][c] == '#' && B[r+1][c] == '#' && B[r][c+1] == '#' && B[r+1][c+1] == '#')
        {
            B[r][c] = '/';
            B[r][c+1] = '\\';
            B[r+1][c] = '\\';
            B[r+1][c+1] = '/';
        }
    }

    rep(r,R) rep(c,C) if(B[r][c] == '#') return false;

    return true;
}

int main()
{
	#ifndef ONLINE_JUDGE
        freopen("A-large.in","r",stdin);
        //freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
	#endif

    int T;
    cin >> T;

    FOR(cs,1,T+1)
    {
        cin >> R >> C;
        rep(r,R) rep(c,C) cin >> B[r][c];

        cout << "Case #" << cs <<":" << endl ;

        if(!solve())
        {
            cout << "Impossible" << endl;
        }
        else
        {
            rep(r,R)
            {
                rep(c,C) cout << B[r][c];
                cout << endl;
            }
        }
    }

	return 0;
}
