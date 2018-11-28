#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long LL;


void solve(int TT) {
	int R;
	cin >> R;
	const int n = 300;
	VVI a(n, VI(n, 0));
	for(int i=0; i<R; i++) {
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		for(int x=x1; x<=x2; x++)
			for(int y=y1; y<=y2; y++)
				a[y+100][x+100] = 1;
	}
	int total = 0;
	while(true) {
		int count = 0;
		for(int y=n-1; y>0; y--)
			for(int x=n-1; x>0; x--) 
				if (a[y][x]==1)
					count++;
		if (count == 0)
			break;
		total++;
		for(int y=n-1; y>0; y--)
			for(int x=n-1; x>0; x--) {
				if (a[y][x]==0) { // 0
					if (a[y-1][x] + a[y][x-1] == 2) 
						a[y][x] = 1;
				} else { // 1
					if (a[y-1][x] + a[y][x-1] == 0)
						a[y][x] = 0;
				}
			}
	}
	cout << "Case #" << TT << ": " << total << endl;
}


int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin.sync_with_stdio(false);
	int n;
	cin >> n;
	for(int i=0; i<n; i++)
		solve(i+1);
	return 0;
}