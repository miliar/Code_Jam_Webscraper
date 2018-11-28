#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define eps 1e-9
#define FOR(x, s, e) for(int x = (s); x < (e); ++x)
#define FORc(x, s, e, c) for(int x = (s); x < (e) && (c); ++x)
#define STEP(x, s, e, d) for(int x = (s); x < (e); x+=(d))
#define ROF(x, s, e) for(int x = (s); x >= (e); --x)
#define ROFc(x, s, e, c) for(int x = (s); x >= (e) && (c); --x)
#define vb vector<bool>
#define vi vector<int>
#define vii vector<pair<int, int> >
#define vs vector<string>
#define pb push_back
#define mp make_pair
#define ALL(X) X.begin(), X.end()
#define LL long long
#define pii pair<int, int>
#define x first
#define y second
#define gcd(x, y) __gcd((x), (y))
#define countbit(x) __builtin_popcount(x)

using namespace std;

int main(int argc, char **argv){
	int T;
	cin >> T;
	FOR(Ca, 1, T+1){
		printf("Case #%d: ", Ca);
		int N, M, D;
		cin >> N >> M >> D;
		string s;
		int G[N][M];
		FOR(i, 0, N){
			cin >> s;
			FOR(j, 0, M) G[i][j] = s[j] - '0';
		}
		int res = 0;
		double DX[N][M], DY[N][M], DP[N][M];
		memset(DX, 0, sizeof(DX));
		memset(DY, 0, sizeof(DY));
		memset(DP, 0, sizeof(DP));
		FOR(i, 0, N){
			double s = 0;
			FOR(j, 0, M){
				s += D + G[i][j];
				if (i) DP[i][j] = DP[i-1][j] + s;
				else DP[i][j] = s;
			}
		}
		FOR(i, 0, N){
			double s = 0;
			FOR(j, 0, M){
				s += (i+0.5)*(D + G[i][j]);
				if (i) DX[i][j] = DX[i-1][j] + s;
				else DX[i][j] = s;
			}
		}
		FOR(i, 0, N){
			double s = 0;
			FOR(j, 0, M){
				s += (j+0.5) * (D + G[i][j]);
				if (i) DY[i][j] = DY[i-1][j] + s;
				else DY[i][j] = s;
			}
		}
		
		FOR(i, 0, N) FOR(j, 0, M) FOR(K, 3, 1+max(M, N)){
			if (i+K-1<N && j+K-1 < M){
				double dx, dy, sx = 0, sy = 0, ex=0, ey=0;
				dx = 1.*K/2 + i, dy = 1.*K/2 + j;
				/*
				FOR(p, i, i+K) FOR(q, j, j+K)
					if (p == i && q == j) continue;
					else if (p == i && q == j+K-1) continue;
					else if (p == i+K-1 && q == j) continue;
					else if (p == i+K-1 && q == j+K-1) continue;
					else sx += (p+0.5)*(D+G[p][q]), ex += dx*(D+G[p][q]), sy += (q+0.5)*(D+G[p][q]), ey += dy*(D+G[p][q]);*/
				int xx = i+K-1, yy = j+K-1;
				double px = DX[xx][yy] - (j?DX[xx][j-1]:0) - (i?DX[i-1][yy]:0) + ((i>0&&j>0)?DX[i-1][j-1]:0);
				double py = DY[xx][yy] - (j?DY[xx][j-1]:0) - (i?DY[i-1][yy]:0) + ((i>0&&j>0)?DY[i-1][j-1]:0);
				px -= (i+0.5)*(D+D+G[i][j]+G[i][yy]) + (xx+0.5)*(D+D+G[xx][j]+G[xx][yy]);
				py -= (j+0.5)*(D+D+G[i][j]+G[xx][j]) + (yy+0.5)*(D+D+G[i][yy]+G[xx][yy]);
				double sum = DP[xx][yy] - (j?DP[xx][j-1]:0) - (i?DP[i-1][yy]:0) + ((i>0&&j>0)?DP[i-1][j-1]:0);
				sum -= G[i][j] + G[i][yy] + G[xx][j] + G[xx][yy] + 4*D;
				//printf("%d %d %d: %.3f %.3f vs %.3f %.3f\n", i, j, K, sx, sy, px, py);
				//printf("\t: %.3f %.3f vs %.3f %.3f\n", dx*sum, dy*sum, ex, ey);
				if (fabs(px - dx*sum) < eps && fabs(py - dy * sum) < eps){
					res = max(res, K);
				}
			}
		}
		if (res) cout << res << endl;
		else puts("IMPOSSIBLE");
	}
	return 0;
}
