# include <cstdio>
# include <iostream>
# include <fstream>
# include <algorithm>
# include <vector>
# include <string>
# include <set>
# include <utility>
# include <map>
# include <queue>
# include <stack>
# include <list>
# include <bitset>
# include <deque>
# include <cassert>
# include <iomanip>
# include <cmath>
# define pb push_back
# define forn(i,n) for (int i=0; i<(int)n; ++i)
# define ford(i,n) for (int i=n-1; i>=0; --i)
# define get(a,b); a b; cin >> b;
# define ull unsigned long long
# define ll long long
# define ld long double
# define mp make_pair
# define matrix vector < vector <int> > 
# define all(a) a.begin(), a.end()
# define INF 1e9
# define eps 1e-9
using namespace std;

int main(){
	int t;
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	scanf("%d\n", &t);
	map <char,int> bbb;
	bbb['O'] = 0;
	bbb['B'] = 1;
	set <char> rob;
	rob.insert('O');
	rob.insert('B');
	forn(i,t){
		int n;
		scanf("%d", &n);
		vector < pair <int,int> > d;
		forn(j,n){
			char c; int pos;
			c = ' ';
			while (rob.count(c)==0)
				scanf("%c", &c);
			scanf("%d", &pos);
			d.pb(mp(bbb[c],pos));
		}
		int f = 1, s = 1;
		int tf = 0, ts = 0;
		forn(j,d.size()){
			if (d[j].first == 0){
				int ct = abs(d[j].second-f);
				f = d[j].second;
				if (ts>tf){
					ct = max(ct-(ts-tf),0);
					tf = ts + ct + 1;
				}
				else
					tf += ct+1;
			}else{
				int ct = abs(d[j].second-s);
				s = d[j].second;
				if (tf>ts){
					ct = max(ct-(tf-ts),0);
					ts = tf + ct + 1;
				}
				else
					ts += ct + 1;
			}			
		}
		int ans = max(tf,ts);		
		printf("Case #%d: %d\n", i+1, ans);
	}

    return 0;
}
