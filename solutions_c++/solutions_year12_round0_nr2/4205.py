#include <algorithm>
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <cmath>
#include <set>
#include <list>
#include <queue>
using namespace std;

#define FOR(t,l,r) for (int t=l; t<r; t++)
#define forn(i) for (i=0; i<n; i++)
#define all int t; forn(t)
#define alli int i; forn(i)
#define max(x,y) ((x>y)?x:y)
#define min(x,y) ((x<y)?x:y)
#define abs(x) ((x<0)?-x:x)
#define pi 2*acos(0.)
#define inf (1<<24)
#define eps 1e-15
#define end cout<<endl
#define pb push_back
#define mp make_pair
#define sz size()
#define LL long long
#define VI vector<int>
#define VII vector<VI>
#define pii pair<int,int>
// #define x first
// #define y second

const int ML=100500;
int ti[ML];

int main () {
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int T, n, s, p, tp, ans;
	cin >>T;
	FOR(i,0,T) {
		cin >>n>>s>>p;
		FOR(t,0,n) cin >>ti[t];
		ans=0;
		sort(ti,ti+n);
		for (int t=n-1; t>=0; t--) {
			tp=ti[t];
			if (tp>3) {
				if ( ( (tp+2)/3 )>=p ) {ans++; continue;}
				if (!s) break; s--;
				if ( ( (tp+4)/3 )>=p ) ans++;
			}
			switch(tp) {
				case 0: {
					if (p==0) ans++;
					else t=-1;
				} break;
				case 1: {
					if (p<=1) ans++;
					else t=-1;
				} break;
				case 2: {
					if (p<=1) ans++;
					else if (s) s--, ans++;
					else t=-1;
				} break;
				case 3: {
					if (p<=1) ans++;
					else if (s) s--, ans++;
					else t=-1;
				} break;
			}
		}
		cout <<"Case #"<<i+1<<": "<<ans<<endl;
	}
return 0;
}





