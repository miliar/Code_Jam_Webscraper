#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define reps(i,f,n) for(int i=f; i<int(n); ++i)
#define rep(i,n) reps(i,0,n)

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;

const int INF = 1001001001;
const double EPS = 1e-10;

string solve()
{
	char board[5][5];
	rep(i, 4)
		scanf("%s", board[i]);
	
	const int dy[] = {0, 0, 0, 0, 1, 1, 1, 1, 1, 1};
	const int dx[] = {1, 1, 1, 1, 0, 0, 0, 0, 1, -1};
	const int sy[] = {0, 1, 2, 3, 0, 0, 0, 0, 0, 0};
	const int sx[] = {0, 0, 0, 0, 0, 1, 2, 3, 0, 3};
	rep(i, 10){
		int cnt[4] = {0};
		int y = sy[i], x = sx[i];
		rep(j, 4){
			if(board[y][x] == 'T')
				cnt[0]++;
			else if(board[y][x] == 'X')
				cnt[1]++;
			else if(board[y][x] == 'O')
				cnt[2]++;
			else
				cnt[3]++;
			y += dy[i];
			x += dx[i];
		}
		if(cnt[3] != 0 || cnt[1]*cnt[2] != 0)
			continue;
		if(cnt[1])
			return "X won";
		if(cnt[2])
			return "O won";
	}
	
	rep(i, 4) rep(j, 4){
		if(board[i][j] == '.')
			return "Game has not completed";
	}
	return "Draw";
}

int main()
{
	int t;
	scanf("%d", &t);
	rep(i, t){
		printf("Case #%d: %s\n", i+1, solve().c_str());
	}
	return 0;
}
