#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;


int o[100]={0};
int b[100]={0};
int oi=0;
int bi=0;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w+", stdout);

    int t;
    cin >> t;
    REP (tt, t)
    {
        cout << "Case #" << (tt+1) << ": ";
		int res =0;

        int n;
        cin >> n;

		int cost[2]={0,0};
		// Orange: 0 
		// Blue: 1 
		char bot;
		int pos;
		int lastpos[2] = {1, 1};
		int lastbot = -1;

        REP (i, n)
        {
            cin >> bot>>pos;
			//cout <<"move"<<bot<<" " <<pos<<endl;
			int self = (bot=='O')?0:1;
			int other = (bot=='O')?1:0;

			if (self == lastbot) {
				cost[self]+=(1+abs(pos-lastpos[self]));
				res+=(1+abs(pos-lastpos[self]));
				//cout <<"cost sef"<<cost[self]<<" other"<<cost[other]<<endl;;
			} else {
				cost[self] = (1+abs(pos-lastpos[self]));
				//cout <<"cost sef"<<cost[self]<<" other"<<cost[other]<<endl;;
				if(cost[self]<=cost[other])
					cost[self]=1;
				else {
					cost[self]-=cost[other];
				}
				res+=cost[self];
				lastbot = self;
			}
			//cout <<self<<" "<<res<<endl;
			lastpos[self]= pos;
		}

		cout << res << endl;
	}

	return 0;
}
