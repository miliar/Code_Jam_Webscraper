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

using namespace std;

#define FOR(i,a,b)	for(int i=(a); i<(b); ++i)
#define REP(iter,v) for(typeof((v).begin()) iter = (v).begin(); iter != (v).end(); ++iter)
#define MP make_pair
#define PB push_back
#define SZ size()
#define iss istringstream 

#define SORT(x) sort(x.begin(), x.end())
#define ALL(x) x.begin(), x.end()
#define UNIQUE(x) x.erase(unique(x.begin(),x.end()),x.end()) 
#define dbg(x) cerr << #x << " -> '" << (x) << "'\t"
#define dbge(x) cerr << #x << " -> '" << (x) << "'\n"

typedef long long ll, int64;
typedef vector<int> VI;

int64 INF = 1000*1000*1001;

vector<ll> g;
map<int, pair<ll, ll> > m;
ll rnd[2048];

ll k, R;
int N;

int main(void)	{
	int C;
	cin >> C;
	FOR (nc, 1, C+1)	{
		cin >> R >> k >> N;
		g.resize(N, 0);
		FOR (i, 0, N)	{
			cin >> g[i];
		}
		
		ll ch = 0;
		int j = 0;
		
		m.clear();
		FOR (r, 0, R)	{
			m[j] = MP(ch, r);
			rnd[r] = ch;
			ll tot = 0;
			int c = 0;
			while (c < N && g[j] + tot <= k)	{
				tot += g[j];
				j = (j + 1) % N;
				c++;
			}
			ch += tot;
			//cout << j << "\t" << ch << endl;
			//
			
			if (m.count(j) != 0)	{
				ll money = m[j].first;
				ll rds = m[j].second;
				//cout << "r = " << r << endl;
				//cout << "rds = " << rds << endl;
				//cout << "round money = " << (ch - money) << endl;
				ch += (ll)((R - (r + 1)) / (r + 1 - rds)) * (ch - money);
				ch += rnd[rds + (R - (r + 1)) % (r + 1 - rds)] - rnd[rds];
//				FOR (p, 0, (R - (r + 1)) % (r + 1 - rds))	{
//					ch += rnd[rds + p];
//				}
				break;
			}
					
		}
		
		cout << "Case #" << nc << ": " << ch << endl;
	}
	
	
}
