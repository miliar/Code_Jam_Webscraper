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

int h,w;
int ret[1<<12][10][10];
string s[12];
int solve(int mask,int y,int x){
	if(x==w)return solve(mask,y+1,0);
	if(y==h)return 0;
	int& ans = ret[mask][y][x];
	if(ans == -1){
		ans = 0;
		int mask2 = mask&((1<<w)-1);
		mask2 = 2*mask2;
		ans = max(ans,solve(mask2,y,x+1));
		int put = s[y][x]=='.';
		if(mask&(1<<w) && x>0)put=false;
		if(x+1<w && (mask&(1<<(w-2))))put=false;
		if(x>0 && (mask&(1<<0)))put=false;
		if(put){
			mask2++;
			ans = max(ans,1+solve(mask2,y,x+1));
		}
	}
	return ans;
};

int main(){
	int cas,t=0;
	cin >> cas;
	while(cas--){
		t++;
		int i;
		cin >> h >> w;
		FOR(i,h)
			cin >> s[i];
		SET(ret,-1);
		int ans = solve(0,0,0);
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
