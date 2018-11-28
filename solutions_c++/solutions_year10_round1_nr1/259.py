#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:64000000")
#include<iostream>
#include<fstream>
#include<algorithm>
#include<math.h>
#include<vector>
#include<set>
#include<list>
#include<map>
#include<deque>
#include<stack>
#include<queue>
#include<string>
#include<cstring>
#include<bitset>
#include<sstream>
#include<time.h>
#include<numeric>
#include<functional>

using namespace std;
#define _CRT_SECURE_NO_WARNINGS
#define INF  ((1 << 31) - 1)
#define LLINF  ((ll)((1LL << 63) - 1))
#define eps (1e-9)
#define million 1000000
#define PI 3.14159265358979323846
#define sz(v) ((int)(v).size())
#define MP make_pair
#define PB push_back
#define all(v) (v).begin(), (v).end()
typedef long long ll;

int dx[] = {-1, -1, -1, 0, 0, +1, +1, +1};
int dy[] = {-1, 0, +1, -1, +1, -1, 0, +1};

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int id = 0; id < T; ++id) {
		cout << "Case #" << id + 1 << ": ";
		int n, k;
		cin >>  n>> k;
		vector<string> field(n);
		for (int i = 0; i < n; ++i)
			cin >> field[i];
		vector<string> rot_field(n, string(n, '%'));
		for (int i = 0 ;i < n; ++i)
			for (int j = 0; j < n; ++j)
				rot_field[i][j] = field[n - 1 - j][i];
		for (int i = 0; i < n; ++i) {
			for (int j = n - 1; j >= 0; --j) {
				int p = j;
				while(p < n - 1 && rot_field[p][i] != '.' && rot_field[p + 1][i] == '.') {
					swap(rot_field[p][i], rot_field[p + 1][i]);
					++p;
				}
			}
		}
		bool red = false;
		bool blue = false;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (rot_field[i][j] == '.')
					continue;
				for (int d = 0; d < 8; ++d) {
					char c = rot_field[i][j];
					int num = 0;
					int nx = i;
					int ny = j;
					for (int a = 0; a < k; ++a) {
						if (nx < 0 || nx == n ||
							ny < 0 || ny == n) break;
						if (rot_field[nx][ny] == c)
							++num;
						else
							break;
						nx += dx[d];
						ny += dy[d];
					}
					if (num == k) {
						if (c == 'R')
							red = true;
						if (c == 'B')
							blue = true;
					}
				}
			}
		}
		if (red && blue) 
			cout << "Both\n";
		if (red && !blue) 
			cout << "Red\n";
		if (!red && blue)
			cout << "Blue\n";
		if (!red && !blue)
			cout << "Neither\n";
	}
	return 0;
}