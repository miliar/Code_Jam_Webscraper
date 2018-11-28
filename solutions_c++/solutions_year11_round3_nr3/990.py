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

int main()
{
	#ifndef ONLINE_JUDGE
        freopen("C-small-attempt0.in","r",stdin);
        //freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
	#endif

    int T;
    cin >> T;

    FOR(cs,1,T+1)
    {
        int N,L,H;

        cin >> N >> L >> H;
        VI v(N, 0);

        rep(i,N) cin >> v[i];

        int freq = -1;

        FOR(i,L,H+1)
        {
            int cnt = 0;
            rep(j,N) if ( i % v[j] == 0 || v[j] % i == 0) cnt++;
            if(cnt == N)
            {
                freq = i;
                break;
            }

        }

        cout << "Case #" << cs <<": ";


        if(freq != -1)
            cout << freq << endl;
        else
            cout << "NO" << endl;
    }

	return 0;
}
