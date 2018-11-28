using namespace std;

#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <cmath>
#include <queue>
#define FOR(i,a,n) for(int i=a; i<n; i++)
#define REP(i,n) FOR(i,0,n)
#define MAX 1000
#define GI ({int _; scanf("%d", &_);_;})
#define INF (int)1e9
#define sz size()
#define pb push_back
#define mkp make_pair
#define eps 1e-15
#define DINF 1e100
typedef long long LL;
typedef vector<int> VI;

int mp[1000][1000][2];
int main() {
	LL kases = GI+1;	

	FOR(kase, 1, kases) {
		int r = GI, x1,x2, y1, y2;
		memset(mp,0,sizeof(mp));
		REP(i,r) {
			x1 = GI, y1 = GI, x2 = GI, y2= GI;
			for(int j = x1; j <= x2; j++)
			for(int k = y1; k <= y2; k++)
			mp[j][k][0] = 1;
		}
		int t = 0, sec = 0;
		bool fnd = true;
		while(fnd) {
			fnd = false;
			//REP(i,10)  { REP(j,10) cout << mp[i][j][t]; cout << endl; }
			REP(i,300) REP(j,300) {
				mp[i][j][1-t] = mp[i][j][t];
				if(mp[i][j][t] == 0 && (i!=0 && mp[i-1][j][t]) && (j!=0 && mp[i][j-1][t])) mp[i][j][1-t] = 1;
				if(mp[i][j][t] == 1 && (i==0 || mp[i-1][j][t]==0) && (j==0 || mp[i][j-1][t]==0)) mp[i][j][1-t] = 0;
				if(mp[i][j][1-t]) fnd = true;
			}
			sec++;
		//	cout << endl;
			t = 1-t;
		}



	  	 printf("Case #%d: %d\n", kase, sec);
	}
}
