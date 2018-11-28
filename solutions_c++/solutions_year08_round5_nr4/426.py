#include <iostream>
#include <set>
#include <utility>
using namespace std;

int main() {
	
	int Ntc;
	cin >> Ntc;
	
	for(int Ntci = 1; Ntci <= Ntc; ++Ntci) {
		cout << "Case #" << Ntci << ": ";

		int H, W, R;
		cin >> H >> W >> R;
		set<pair<int, int> > rs;
		for(int i = 0; i != R; ++i) {
			int r, c;
			cin >> r >> c;
			rs.insert(make_pair(c-1, r-1));
		}
		
		int dp[100][100];
		for(int x = 0; x != W; ++x) {
			for(int y = 0; y != H; ++y) {
				if(x == 0) {
					dp[x][y] = (y == 0);
				}
				else {
					dp[x][y] = 0;
					if(y >= 2)
						dp[x][y] += dp[x-1][y-2];
					if(x >= 2 && y >= 1)
						dp[x][y] += dp[x-2][y-1];
					dp[x][y] %= 10007;
				}
				if(rs.count(make_pair(x, y))) dp[x][y] = 0;
			}
		}
		
		cout << dp[W-1][H-1];
		
		cout << endl;
	}
}
