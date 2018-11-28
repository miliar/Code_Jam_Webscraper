#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <utility>

using namespace std;

#define dbg(x) cerr<<#x<<" : "<<x<<endl
#define inf (1<<30)
#define PB push_back
#define MP make_pair
#define mset(x,a) memset(x,(a),sizeof(x))
typedef long long LL;
#define twoL(X) (((LL)(1))<<(X))
const double PI = acos(-1.0);
const double eps = 1e-8;

template <class T> T sqr(T x)
{
    return x*x;
}

int gcd(int a, int b)
{
    return (b == 0) ? a : gcd(b, a % b);
}

#define FOREACH(it, a) for(typeof((a).begin()) it = (a).begin(); it!=(a).end(); ++it)
#define ALL(x) (x).begin(), (x).end()

vector <string> dict;
int cnt[11][26];

int work(string & order, int sid, list <int> & lastv) {
	int ret = 0;
	int tcnt[26];
	list <int> v = lastv;
	
	int sz = dict[sid].size();
	memcpy(tcnt, cnt[dict[sid].size()], sizeof(tcnt));
	for(int i=0; i<order.size(); ++i) {
		if(tcnt[order[i]-'a'] == 0) continue;
		bool fd = 0;

		for(int j=0; j<sz; ++j) {
//			dbg(j);
			for(list<int> :: iterator it = v.begin(); it != v.end(); ++it) {
				if(*it == sid) {
					if(dict[*it][j] == order[i]) fd = 1;
					continue;
				}
				if(dict[sid][j] == order[i] && dict[*it][j] == order[i]) {
					continue;
				}
				if(dict[*it][j] == order[i] || dict[sid][j] == order[i]) {
					for(int k=0; k<sz; ++k) {
						char ch = dict[*it][k];
						--tcnt[ch-'a'];
					}
					list<int> :: iterator it2 = it;
					--it;
					v.erase(it2);
				}
			}
			
		}
		if(!fd) {
			++ret;
			
		}
	}
	return ret;
}

int main(int argc, char** argv)
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int ti=1; ti<=t; ++ti) {
		int n,m;
		scanf("%d%d", &n, &m);
		list <int> v[11];
		dict.clear();
		mset(cnt, 0);
		string cur;
		for(int i=0; i<n; ++i) {
			cin>>cur;
			dict.PB(cur);
			v[(int)(cur.size())].push_back(i);
			for(int j=0; j<cur.size(); ++j) {
				++cnt[(int)(cur.size())][cur[j]-'a'];
			}
		}

		string order;
		
		printf("Case #%d:", ti);
		for(int i=0; i<m; ++i) {
			cin>>order;
			int sid, mans=-1;
			for(int j=0; j<n; ++j) {
				int ans = work(order, j, v[(int)(dict[j].size())]);
				if(mans < ans) {
					sid = j;
					mans = ans;
				}
			}
			
			cout<<" "<<dict[sid];
		}
		puts("");

	}
    return (EXIT_SUCCESS);
}

