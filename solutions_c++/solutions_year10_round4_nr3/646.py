#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <cassert>
#include <ctime>
#include <map>
#include <set>
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define X first
#define Y second
#define sz(s) (int)(s).size()
#define mp make_pair

using namespace std;

typedef long long li;
typedef pair<int, int> pt;
bool used[2][200][200];
bool check(int s, int i, int j){
	if(i < 0 || j < 0)
		return false;
	if(!used[s][i][j])
		return false;
	return true;
}
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	forn(q, t){
		int n;
		memset(used, false, sizeof(used));
		scanf("%d", &n);
		forn(i, n){
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			for(int x = x1; x <= x2; x++)
				for(int y = y1; y <= y2; y++)
					used[0][x][y] = true;
		}
		int ans = 0;
		bool good = true;
		int s = 0;
		while(good){
			good = false;
			forn(i, 200)
				forn(j, 200){
					used[(s + 1) & 1][i][j] = used[s][i][j];
					if(used[s][i][j] && !check(s, i - 1, j) && !check(s, i, j - 1))
						used[(s + 1) & 1][i][j] = false;
					if(!used[s][i][j] && i > 0 && j > 0 && used[s][i - 1][j] && used[s][i][j - 1])
						used[(s + 1) & 1][i][j] = true;
					if(used[s][i][j])
						good = true;
				}
			ans++;
			s = !s;
		}
		cout << "Case #" << q + 1 << ": " << ans - 1 << endl;
	}
	return 0;
}