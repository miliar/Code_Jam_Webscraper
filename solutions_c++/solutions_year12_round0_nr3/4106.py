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

int main () {
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int A, B, T, ans;
	int a, b, c, x, y, z;
	cin >>T;
	FOR(i,0,T) {
		cin >>A>>B;
		ans=0;
		FOR(n,A,B+1) FOR(m,n+1,B+1) {
			if (m>999) break;
			c=n%10, b=(n%100)/10, a=n/100;
			z=m%10, y=(m%100)/10, x=m/100;
			if (a*x==0 && a+x>0) continue;
			if (a+x==0)
				if (b*y==0 && b+y>0) continue;
			if (!a && 10*c+b==m) ans++;
			if (100*b+10*c+a==m) ans++;
			if (100*c+10*a+b==m) ans++; 
		}
		cout <<"Case #"<<i+1<<": "<<ans<<endl;
	}
return 0;
}





