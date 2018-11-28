#include <iostream>
#include <cstdio>
#include <cctype>
#include <string>
#include <cmath>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cassert>
#include <cstring>

using namespace std;

#define REP(i,n) FOR(i,0,n)
#define FOR(i,a,b) for(int i = a; i < b; i++)
#define ROF(i,a,b) for(int i=a;i>b;i--)
#define GI ({int t;scanf("%d",&t);t;})
#define GL ({LL t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define SET(x,a) memset(x,a,sizeof(x))
#define all(a) (a.begin(),a.end())
#define rall(a) (a.rbegin(),a.rend())
#define INF (int)1e9
#define EPS (double)1e-9

typedef unsigned long long ULL;
typedef long long LL;
typedef set <int> si;
typedef pair< int,int > ii;
typedef pair< int, ii > pi;
typedef vector< ii > vii;
typedef vector < vii > vvii;
typedef vector< int > vi;
typedef vector< vi > vvi;

vector<string> games;
int total[105], wins[105], loses[105];
double wp[105], owp[105], oowp[105];

int main() {
	int T = GI;
	FOR(t,1,T+1) {
		int N = GI;
		games.clear();
		games.resize(N);
		REP(i,N) cin >> games[i];

		SET(total, 0); SET(wins, 0); SET(loses, 0);
		REP(i,N) REP(j,N) {
			if (games[i][j] == '1') {
				total[i]++; wins[i]++;
			}
			else if (games[i][j] == '0') {
				total[i]++; loses[i]++;
			}
		}

		REP(i,N) wp[i] = owp[i] = oowp[i] = 0.0;
	
		REP(i,N) wp[i] = (double)wins[i]/(double)total[i];

		int ttotal, twins, tloses, count;
		REP(i,N) {
			count = 0;
			REP(j,N) {
				if (i == j || games[j][i] == '.') continue;
				count++;
				ttotal = total[j], twins = wins[j], tloses = loses[j];
				if (games[j][i] == '1') {
					ttotal -= 1;
					twins -= 1;
				}
				else if (games[j][i] == '0') {
					ttotal -= 1;
					tloses -= 1;
				}
				owp[i] += (double)twins/(double)ttotal;
			}
			owp[i] /= (double)count;
		}
	
		REP(i,N) {
			count = 0;
			REP(j, N) {
				if (i != j && games[i][j] != '.') {
					oowp[i] += owp[j];
					count++;
				}
			}	
			oowp[i] /= (double)count;
		}

		printf("Case #%d:\n", t);
		REP(i,N) cout << 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i] << endl;
	}
	return 0;
}
