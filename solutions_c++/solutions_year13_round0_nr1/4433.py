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

#define FOR(t,l,r) for (int t=l; t<(int)r; t++)
#define max(x,y) ((x>y)?x:y)
#define min(x,y) ((x<y)?x:y)
#define abs(x) (((x)<0)?-(x):(x))
const double mth_pi=2*acos(0.);
#define pi mth_pi
#define inf (1<<23)
#define eps 1e-10
#define pb push_back
#define mp make_pair
#define sz size()
#define all(a) a.begin(),a.end()
#define LL long long
#define V vector
#define VD V<double>
#define VI V<int>
#define VII V<VI>
#define mii map<int,int>
#define pii pair<int,int>
#define x first
#define y second

string s[4], ans[4]={"Draw","Game has not completed","X won","O won"};

int main () {
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T; cin >>T;
	FOR(tt,1,T+1) {
		int f=0; bool ff;
		FOR(t,0,4) cin >>s[t];


		FOR(t,0,4) {
			ff=1;
			FOR(i,0,4) if (s[t][i]=='O' || s[t][i]=='.') ff=0;
			if (ff && !f) f=2;
		}
		FOR(i,0,4) {
			ff=1;
			FOR(t,0,4) if (s[t][i]=='O' || s[t][i]=='.') ff=0;
			if (ff && !f) f=2;
		}
		ff=1;
		FOR(t,0,4)
			if (s[t][t]=='O' || s[t][t]=='.') ff=0;
		if (ff && !f) f=2;
		ff=1;
		FOR(t,0,4)
			if (s[t][3-t]=='O' || s[t][3-t]=='.') ff=0;
		if (ff && !f) f=2;


		FOR(t,0,4) {
			ff=1;
			FOR(i,0,4) if (s[t][i]=='X' || s[t][i]=='.') ff=0;
			if (ff && !f) f=3;
		}
		FOR(i,0,4) {
			ff=1;
			FOR(t,0,4) if (s[t][i]=='X' || s[t][i]=='.') ff=0;
			if (ff && !f) f=3;
		}
		ff=1;
		FOR(t,0,4)
			if (s[t][t]=='X' || s[t][t]=='.') ff=0;
		if (ff && !f) f=3;
		ff=1;
		FOR(t,0,4)
			if (s[t][3-t]=='X' || s[t][3-t]=='.') ff=0;
		if (ff && !f) f=3;


		FOR(t,0,4) FOR(i,0,4) if (s[t][i]=='.') if (!f) f=1;
	cout <<"Case #"<<tt<<": "<<ans[f]<<endl;
	}
return 0;
}
