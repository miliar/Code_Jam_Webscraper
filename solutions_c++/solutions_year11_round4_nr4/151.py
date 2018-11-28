#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include <iostream>
#include <climits>
#include <cstring>
using namespace std;

#define forn(a, n) for(int a = 0; a<(n); ++a)
#define forsn(a,s,n) for(int a = (s); a<(n); ++a)
#define forall(a, all) for(typeof((all).begin()) a = (all).begin(); a != (all).end(); ++a)

#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define dforsn(a,s,n) for(int a = (n)-1; a>=(s); --a)
#define dforall(a, all) for(typeof((all).rbegin()) a = (all).rbegin(); a != (all).rend(); ++a)

#define contains(mask, bit) ((mask & (1LL<<bit)) != 0LL)

typedef long long tint;

struct caso{
	list<int> path;
	int pos;
	
	caso(int p){path.clear(); path.push_back(p); pos = p;}
};

int p, w, dist[404];
list<int> next[404];

int main()
{
	freopen("D-small.in", "r", stdin);
	freopen("D-small.out", "w", stdout);

	int T;
	cin >> T;
	forn(P,T){
		cin >> p >> w;
		
		forn(i, p) next[i].clear();
		
		forn(i, w){
			string cm;
			cin >> cm;
			
			int f=0, t=0, coma;
			forn(i, cm.size()){
				if(cm[i] == ','){
					coma = i+1;
					break;
				}
				f = f*10 + cm[i] - '0';
			}
			forsn(i, coma, cm.size())
				t = t*10 + cm[i] - '0';
			
//			cout << f << " " << t << endl;
			next[f].push_back(t);
			next[t].push_back(f);
		}
		
		memset(dist, -1, sizeof(dist));
		queue<caso> q; q.push(caso(0));
		dist[0] = 0;
		list<list<int> > ans;
		int len = INT_MAX;
		
		while(!q.empty()){
			caso c = q.front(); q.pop();
			int d = dist[c.pos];
			
			if(len < d) break;
			if(c.pos == 1){
				ans.push_back(c.path);
				len = dist[c.pos];
			}
			if(len == d)
				continue;
			
			forall(i, next[c.pos])
				if(dist[*i] == -1 || dist[*i] == d+1){
					caso cc = c;
					cc.path.push_back(*i);
					cc.pos = *i;
					dist[*i] = d+1;
					q.push(cc);
				}
		}
		
		int a = dist[1]-1, b=0;
		
		forall(i, ans){
			set<int> s(i->begin(), i->end());
			int count=0;
			
			s.erase(1);
			
			forn(j, p) if(!s.count(j)){
				forall(adj, next[j]) if(s.count(*adj)){
					count++;
					break;
				}
			}
			
			b = max(b, count);
		}
		
		printf("Case #%i: %i %i\n", P+1, a, b);
	}

	return 0;
}
