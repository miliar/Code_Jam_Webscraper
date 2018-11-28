#include <iostream>
#include <cstring>
#include <string>
#include <sstream>
#include <queue>
#include <map>
#include <cmath>
#include <cassert>
#include <set>
#include <vector>
#include <utility>
using namespace std;
#define lint long long
#define SZ(s) ((int)(s.size()))
#define PB push_back
#define MP make_pair
#define FORN(i,a,b) for(i=(int)(a);i<(int)(b);i++)
#define FOR(i,n) FORN(i,0,n)
#define FOREACH(it,S) for(typeof(S.begin()) it = S.begin();it != S.end();it++)
#define SET(x,a) memset(x,a,sizeof x)
#define BEG(a) a.begin()
#define END(a) a.end()
#define ALL(a) BEG(a),END(a)
#define vc(T) vector<T >
#define FIR first
#define SEC second
#define SQR(x) ((x)*(x))
#define EPS (1e-9)
#define fmin(x,y) min((x)+0.0,(y)+0.0)
#define fmax(x,y) max((x)+0.0,(y)+0.0)

int ret[128][128];
int h,w,r;
int x[32],y[32];
int rck[128][128];
int mod = 10007;
int solve(int x2,int y2){
	if(x2==w-1 && y2==h-1)return 1;
	if(x2>=w-1 || y2>=h-1 || rck[y2][x2])return 0;
	int& ans = ret[x2][y2];
	if(ans==-1){
		ans = 0;
		if(x2+1 <= w-1 && y2+2<=h-1)
			ans += solve(x2+1,y2+2);
		if(x2+2 <= w-1 && y2+1 <= h-1)
			ans += solve(x2+2,y2+1);
		ans %= mod;
	}
	return ans;
};
int main(){
	int cas,t=0;
	cin>>cas;
	while(cas--){
		t++;
		cin >> h >> w >> r;
		int i;
		FOR(i,r)cin >> y[i] >> x[i]; 
		FOR(i,r)x[i]--,y[i]--;
		SET(ret,-1);
		SET(rck,false);
		FOR(i,r)rck[y[i]][x[i]]=1;
		cout << "Case #" << t << ": " << solve(0,0) << endl;
	}
	return 0;
}
