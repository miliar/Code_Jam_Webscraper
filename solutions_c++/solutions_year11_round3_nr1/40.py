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
		int N, M;
		cin >> N >> M;
		char B[200][200], R[200][200];
		FOR(i, 0, N) cin >> B[i];
		FOR(i, 0, N) strcpy(R[i], B[i]);
		bool ok = 1;
		int dx[3] = {0, 1, 1}, dy[3] = {1, 0, 1};
		FORc(i, 0, N, ok)
			FORc(j, 0, M, ok)
				if (R[i][j] == '#'){
					FORc(k, 0, 3, ok){
						int nx = i + dx[k], ny = j + dy[k];
						if (nx < 0 || nx >= N || ny <0 || ny >= M){ ok = 0; break;}
						ok = R[nx][ny] == '#';
					}
					if (ok){
						R[i][j] = R[i+1][j+1] = '/';
						R[i+1][j] = R[i][j+1] = '\\';
					}
				}
		if (!ok) puts("\nImpossible");
		else{
			puts("");
			FOR(i, 0, N) puts(R[i]);
		}
	}
	return 0;
}
