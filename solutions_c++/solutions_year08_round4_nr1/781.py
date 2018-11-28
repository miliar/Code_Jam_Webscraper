#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
typedef long long int lint;
typedef pair<int,int> par;
 
#define sz size
#define pb push_back
#define all(x) (x).begin() , (x).end()
#define sqr(x) (x)*(x)
#define x first
#define y second
#define rep(i,n)  for (int (i)=0;(i)<(int)(n);(i)++)
#define Rep(i,a,n) for (int (i)=(int)(a);(i)<(int)(n);(i)++)
#define MAX 10005
#define MAX2 100000005
par vec[MAX];
int M,V;

par dp[MAX][4];

int main() {
	int N;
	cin >> N;
	Rep(i,1,N+1) {
		cin >> M >> V;
		rep(j,(M-1)/2) cin >> vec[j].x >> vec[j].y;
		rep(j,(M+1)/2) {cin >> vec[j+(M-1)/2].x; vec[j+(M-1)/2].y=-1;}
		
		rep(j,MAX) rep(l,4) dp[j][l].x=0 , dp[j][l].y=MAX2;
		
		for (int j=M-1;j>=(M-1)/2;j--) {
			dp[j][vec[j].x].x=1;
			dp[j][vec[j].x+2].x=1;
			dp[j][vec[j].x].y=0;
			dp[j][vec[j].x+2].y=0;
		}

		for (int j=M-2;j>=0;j-=2) {
				//cout << j << ": " << vec[j/2].x << " " << vec[j/2].y << endl;
			if (vec[j/2].y==-1) continue;
			int changeable=vec[j/2].y;
			if (vec[j/2].x == 0 || changeable) {
				//cout << "HERE" << endl;
				if (vec[j/2].x==0) changeable=0;
				
				rep(a,4) rep(b,4) {
					if ((a==0 || a==2) && (b==0 || b==2)) {// OR 0
						if (dp[j][a].x && dp[j+1][b].x)
							dp[j/2][0].x=1 , dp[j/2][0].y=min(dp[j/2][0].y,dp[j][a].y + dp[j+1][b].y + changeable);
					}
					else {							   // OR 1
						if (dp[j][a].x && dp[j+1][b].x)
							dp[j/2][1].x=1 , dp[j/2][1].y=min(dp[j/2][1].y,dp[j][a].y + dp[j+1][b].y + changeable);
					}
				}
			}
			changeable=vec[j/2].y;
			if (vec[j/2].x == 1 || changeable) {
				//cout << "THERE" << endl;
				if (vec[j/2].x==1)
					changeable=0;
				rep(a,4) rep(b,4) {
					if ((a==1 || a==3) && (b==1 || b==3)) {// And 1
						if (dp[j][a].x && dp[j+1][b].x)
							dp[j/2][3].x=1 , dp[j/2][3].y=min(dp[j/2][3].y,dp[j][a].y + dp[j+1][b].y + changeable);
					}
					else {							       // And 0
						if (dp[j][a].x && dp[j+1][b].x)
							dp[j/2][2].x=1 , dp[j/2][2].y=min(dp[j/2][2].y,dp[j][a].y + dp[j+1][b].y + changeable);
					}
				}
			}
		}
		
		/*for (int j=M-1;j>=0;j--) {
			cout << dp[j][0].x << "(" << dp[j][0].y << ")   ";
			cout << dp[j][1].x << "(" << dp[j][1].y << ")   ";
			cout << dp[j][2].x << "(" << dp[j][2].y << ")   ";
			cout << dp[j][3].x << "(" << dp[j][3].y << ")  ";
			cout << endl;			
		}
		*/
		cout << "Case #" << i << ": ";
		int answer=MAX2;
		if (!V) {
			if (dp[0][0].x) answer=dp[0][0].y;
			if (dp[0][2].x) answer=min(answer,dp[0][2].y);
		}
		else {
			if (dp[0][1].x) answer=dp[0][1].y;
			if (dp[0][3].x) answer=min(answer,dp[0][3].y);			
		}
		if (answer==MAX2) cout << "IMPOSSIBLE" << endl;
		else 			  cout << answer << endl;
	}
	return 0;
}
