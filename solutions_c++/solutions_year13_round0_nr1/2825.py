#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

using namespace std;

#define rep(i, n) for(int i = 0; i < (n); i++)
#define For(i, a, b) for(int i = (a); i < (b); i++)
#define foreach(it, c) for(__typeof (c).begin() it = (c).begin(); it != (c).end(); ++it)
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define sz(v) (int)(v).size()
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define sqr(x) ((x) * (x))
#define clr(m, c) memset((m), (c), sizeof (m))
#define DBG(x) cout << #x << " = " << x << endl
#define EPS 1e-9
#define PI 3.14159265358979323846264338327950

template<class T> T abs(T x) { return x > 0 ? x : -x; }

typedef long long ll;
typedef long double ld;
typedef pair<int, int> ii;
typedef vector<int> vi;

const ll INF = 1LL<<60;
const ll MOD = 1000000007;

char M[4][4];
int cnt_O, cnt_X, cnt_T;

void dfs(int x, int y, int mx, int my){
	if(x < 0 or x > 3 or y < 0 or y > 3) return;
	if(M[x][y] == 'O') cnt_O++;
	if(M[x][y] == 'X') cnt_X++;
	if(M[x][y] == 'T') cnt_T++;
	dfs(x + mx, y + my, mx, my);
}

int main(){
	int tt;
	int movx[] = {1, -1, 0};
	int movy[] = {1, -1, 0};
	string res[] = {"X won", "O won", "Draw", "Game has not completed"};
	string s;
	cin >> tt;
	for(int t = 1; t <= tt; t++){
		for(int i = 0; i < 4; i++){
			cin >> s;
			for(int j = 0; j < 4; j++) M[i][j] = s[j];
		}
		int ind = -1;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				for(int mx = 0; mx < 3; mx++)
					for(int my = 0; my < 3; my++){
						if(movx[mx] == 0 and movy[my] == 0) continue;
						cnt_O = cnt_X = cnt_T = 0;
						dfs(i, j, movx[mx], movy[my]);
						if(cnt_O == 4 or (cnt_O == 3 and cnt_T == 1)) ind = 1;
						if(cnt_X == 4 or (cnt_X == 3 and cnt_T == 1)) ind = 0;
					}
		if(ind == -1){
			ind = 2;
			for(int i = 0; i < 4; i++)
				for(int j = 0; j < 4; j++)
					if(M[i][j] == '.') ind = 3;
		}
		cout << "Case #" << t << ": " << res[ind] << endl;
	}
	return 0;
}

