#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define gcj_print(ans) {cout << "Case #" << ((test)+1) << ":" << (ans) << endl;}

int a[110][110];
pair <int, int> p[110][110];
map <pair <int, int>, char> mp;
char c[110][110];
int dx[]={-1,0,0,1},dy[]={0,-1,1,0};
int H,W;

pair <int, int> dfs(int x, int y){
	if(p[x][y] != make_pair(-1,-1)) return p[x][y];
	
	int i,dir=-1;
	REP(i,4){
		int x2=x+dx[i],y2=y+dy[i];
		if(x2 >= 0 && x2 < H && y2 >= 0 && y2 < W && a[x2][y2] < a[x][y] && (dir == -1 || a[x2][y2] < a[x+dx[dir]][y+dy[dir]])) dir = i;
	}
	
	if(dir != -1) return p[x][y] = dfs(x+dx[dir],y+dy[dir]);
	return p[x][y] = make_pair(x,y);
}

int main(void){
	int i,j,T,test;
	
	cin >> T;
	REP(test,T){
		cin >> H >> W;
		REP(i,H) REP(j,W) cin >> a[i][j];
		
		REP(i,H) REP(j,W) p[i][j] = make_pair(-1,-1);
		REP(i,H) REP(j,W) p[i][j] = dfs(i,j);
		
		mp.clear();
		char ch = 'a';
		REP(i,H) REP(j,W){
			if(mp.find(p[i][j]) != mp.end()) c[i][j] = mp[p[i][j]];
			else {
				mp[p[i][j]] = c[i][j] = ch;
				ch++;
			}
		}
		
		gcj_print("");
		REP(i,H) REP(j,W){
			cout << c[i][j];
			if(j == W-1) cout << endl; else cout << ' ';
		}
	}
	
	return 0;
}
