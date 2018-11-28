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
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small-attempt0.out","wt",stdout);
	int t;
	scanf("%d", &t);
	forn(test,t){
		int n;
		scanf("%d", &n);
		vector <int> d(n);
		int ans = -1;
		forn(i,n)
			scanf("%d", &d[i]);
		forn(i,1<<n){
			int cur;
			cur = i;
			set <int> cind;
			int p = 0;
			while (cur > 0){
				if (cur % 2 == 1)
					cind.insert(p);
				cur /= 2;
				p++;
			}
			int sum1 = 0, sum2 = 0, x1 = 0, x2 = 0;
			forn(j,n)
				if (cind.count(j) == 1){
					sum1 += d[j];
					x1 = x1 ^ d[j];
				}else{
					sum2 += d[j];
					x2 = x2 ^ d[j];
				}
			if (x1 == x2 && cind.size()!=0 && cind.size()!=n)
				ans = max(ans,sum2);
		}
		if (ans == -1)
			printf("Case #%d: NO\n", test+1);
		else
			printf("Case #%d: %d\n", test+1, ans);
	}
    return 0;
}
