#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define SETMIN(a,b) a = min(a,b)
#define SETMAX(a,b) a = max(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define CLR(x,a) memset(x,a,sizeof(x))
#define BEND(v) v.begin(),v.end()
#define MP make_pair
#define A first
#define B second

typedef unsigned long long int ull;
typedef long double ld;

int main() {
	freopen("themepark.in","r",stdin);
	freopen("themepark.out","w",stdout);

	int T;
	cin >> T;
	FOR(t,T) {
		int R,k,N;
		cin >> R >> k >> N;
		int grps[1001], done[1001], pts[1001], next[1001];
		CLR(done,0);
		queue<pair<int,int> > q;
		FOR(i,N) {
			cin >> grps[i];
			q.push(MP(i,grps[i]));
		}
		
		while(!done[q.front().A]) {
			int cur = 0;
			int start = q.front().A;
			done[start] = 1;

			FOR(i,N) {
				if (cur + q.front().B > k) break;

				cur += q.front().B;
				//cerr << q.front().B << " ";
				q.push(q.front());
				q.pop();
			}
			//cerr << endl;
			next[start] = q.front().A;
			pts[start] = cur;
		}

		while (!q.empty()) q.pop();

		int curFront = 0;
		ull ans = 0;
		FOR(i,R) {
			ans += pts[curFront];
			curFront = next[curFront];
		}

		printf("Case #%d: %lld\n", t+1, ans);
	}
	return 0;
}


		
			

