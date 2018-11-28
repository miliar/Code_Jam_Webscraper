#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <cmath>
#include <string>

#define fr(x,y) for(int x=0; x<(y); ++x)
#define fe(x,y,z) for(int x=(y); x<(z); ++x)
#define fw(x,y,z) for(int x=(y); x<=(z); ++x)
#define df(x,y,z) for(int x=(y); x>=(z); --x)
#define mn(x,y) ((x)<(y) ? (x) : (y))
#define mx(x,y) ((x)>(y) ? (x) : (y))
#define ab(x) ((x)<0 ? (-(x)) : (x))
#define MP make_pair
#define PB push_back
#define BIG 1000000000
#define X first
#define Y second
#define dbg(x) if(DEBUG) {cout<<#x<<": "<<(x)<<endl;}
#define dout(x) if(DEBUG) {cout<<x;}
#define dline(x) if(DEBUG) {cout<<x<<endl;}
#define dbgr(x,l) if(DEBUG) {cout<<#x<<": ";fr(innercounter,l) cout<<x[innercounter]<<" ";cout<<endl;}
#define dbge(x,y,z) if(DEBUG) {cout<<#x<<": ";fe(innercounter,y,z) cout<<x[innercounter]<<" ";cout<<endl;}
#define dbgw(x,y,z) if(DEBUG) {cout<<#x<<": ";fw(innercounter,y,z) cout<<x[innercounter]<<" ";cout<<endl;}
#define dbgee(x,l1,l2) if(DEBUG) {cout<<#x<<": "<<endl;fr(icounter,l1){fr(jcounter,l2) cout<<x[icounter][jcounter]<<" ";cout<<endl;}}

bool DEBUG = false;

using namespace std;

int t,n;
char mas[200][200];
int win[200],games[200];
double wp[200], owp[200], oowp[200],r[200];

int main()
{
#ifdef HOME
freopen("input.txt", "r",stdin);
freopen("output.txt", "w", stdout);
//DEBUG = true;
#endif
scanf("%d\n", &t);
fw(test,1,t)
	{
	scanf("%d\n", &n);
	fr(i,n)
		win[i] = games[i] = wp[i] = owp[i] = oowp[i] = 0;
	fr(i,n)
		gets(mas[i]);
	fr(i,n)
	fr(j,n)
		if(mas[i][j]!='.')
			{
			games[i]++;	
			if(mas[i][j]=='1') win[i]++;
			}
	dbgr(win,n);
	dbgr(games,n);
	fr(i,n)
		wp[i] = win[i]*1.0/games[i];
	dbgr(wp,n);
	fr(i,n)
	fr(j,n)
		if(mas[i][j]!='.')
			{
			int a = win[j];
			if(mas[i][j]=='0') a--;
			owp[i]+=(a*1.0/(games[j]-1));
			}
	fr(i,n)
		if(games[i]>0) owp[i]/=games[i];
	dbgr(owp,n);
	fr(i,n)
	fr(j,n)
		if(mas[i][j]!='.')
			{
			oowp[i]+=owp[j];
			}
	fr(i,n)
		if(games[i]>0) oowp[i]/=games[i];
	dbgr(oowp,n);
	fr(i,n)
		r[i] = 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
	dbgr(r,n);
	printf("Case #%d:\n", test);
	fr(i,n)
		printf("%.9lf\n", r[i]);
	}
return 0;
}
