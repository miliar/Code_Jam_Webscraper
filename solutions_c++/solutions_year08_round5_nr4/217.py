#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <list>
#include <string>
#include <algorithm>
#include <functional>
#include <utility>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <cstdio>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
#define pb push_back
#define MP make_pair
#define For(a,b,c) for(typeof(b)a=(b); a<(c); ++a)
#define ALL(a) (a).begin(),(a).end()
#define DBG(a) cout << #a << ": " << a << endl
#define FORE(i, v) for(typeof(v.begin()) i = v.begin(); i != v.end(); ++i)

int dr[4] = {1, 2};
int dc[4] = {2, 1};
int H, W, R;
int nways[110][110];

int go(int r, int c)
{
	if (nways[r][c] != -1) return nways[r][c];

	nways[r][c] = 0;
	for (int i = 0; i < 2; i++)
	{
		int nr = r + dr[i], nc = c + dc[i];
		if (nr < H && nc < W)
			(nways[r][c] += go(nr, nc)) %= 10007;
	}
	return nways[r][c];
}

int main()
{
	freopen("D.in", "r", stdin);
	
	int T;
	cin >> T;
	For (LOL, 1, T+1)
	{
		 cin >> H >> W >> R;
		 memset(nways, -1, sizeof nways);
		For (i, 0, R)
			{
				int a, b; cin >> a >> b;
				nways[a-1][b-1] = 0;
			}
			
		nways[H-1][W-1] = 1;
			
		printf("Case #%d: ", LOL);
		cout << go(0,0) << endl;
	}
	
	return 0;
}