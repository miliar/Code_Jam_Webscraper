#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <climits>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <iostream>
#include <algorithm>
#include <functional>

#include <cassert>
 
using namespace std;

#define EACH(i,c) for(__typeof((c).begin()) i = (c).begin();i!=(c).end();i++)
#define FOR(i,a,b)  for(int i=(a);i<(b);i++)
#define dbg(e)  cout<<(#e)<<" : "<<e<<endl
#define set(v,i) memset(v,i,sizeof(v))
#define all(x) x.begin(),x.end()
#define sz(x) int((x).size())
#define REP(i,n) FOR(i,0,n)
#define pb  push_back
#define mp make_pair

typedef long long LL;

#define EPS 1e-10

vector<string> words;

int main() {
	int test; scanf("%d",&test); REP(tt,test) {
		int l,t,n,c,x;
		vector<int> V,dist;
		scanf("%d%d%d%d",&l,&t,&n,&c);
		REP(i,c) cin >> x, V.pb(x);
		dist.resize(n);

		REP(i,c) {
			int j = 0;
			while(true) {
				if(c*j + i >= n) break;
				dist[c*j + i] = V[i] * 2;
				//cout << "dist ( " << c*j + i << " ) = " << V[i] << endl;
				j++;
			}
		}
		//REP(i,n) cout << dist[i] << " ";
		//cout << endl;
		int T = 0,mark = 0;
		vector<bool> visit(n);
		//t *= 2;
		REP(i,n) {
			if(T + dist[i] > t) break;
			T += dist[i];
			visit[i] = true;
			mark++;
		}
		//dbg(mark);
		if(mark == n) {
			//reached destination;
			printf("Case #%d: %d\n", tt+1,T);
			continue;
		}
		vector<int> X;
		//dbg(dist[mark]);
		int diff = dist[mark] - (t - T);
		//dbg(diff);
		X.pb(diff);
		FOR(i,mark+1,n) X.pb(dist[i]);
		sort(X.rbegin(),X.rend());

		//REP(i,sz(X)) cout<< X[i] << " ";
		//cout << endl;
		T = t;
		//dbg(T);
		
		REP(i,sz(X)) {
			if(l > 0) {
				T += X[i] / 2;
				//dbg(T);
				l--;
			}
			else {
				T += X[i];
			}
		}
		printf("Case #%d: %d\n", tt+1, T);
	}
}


