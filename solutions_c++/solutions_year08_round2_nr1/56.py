#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>

const long double eps = 1e-9;

using namespace std;


long long A, B, C, D;
long long x,y, M;

long long cnt[3][3];

int n;
void Load()
{
	cin >> n;
	cin >> A >> B >> C >> D;
	cin >> x >> y >> M;
	int i;
	memset(cnt, 0, sizeof(cnt));
	cnt[x %3][y%3] = 1;
	for (i = 1; i < n; i++) {
		x = (A * x + B) % M;
		y = (C * y + D) % M;
		cnt[x %3][y%3]++;
	}
}


void Solve()
{
	int i1, j1, i2, j2, i3, j3;
	long long res = 0;
	long long a, b, c;
	for (i1 = 0; i1 < 3; i1++) {
		for (j1 = 0; j1 < 3; j1++) {
//			cerr << i1 << " " << j1 << " " << cnt[i1][j1] << "\n";
			if (cnt[i1][j1] == 0) continue;
			a = cnt[i1][j1];
			cnt[i1][j1]--;
			for (i2 = 0; i2 < 3; i2++) {
				for (j2 = 0; j2 < 3; j2++) {
					if (cnt[i2][j2] == 0) continue;
					b = cnt[i2][j2];
					cnt[i2][j2]--;
					for (i3 = 0; i3 < 3; i3++) {
						for (j3 = 0; j3 < 3; j3++) {
			                if (cnt[i3][j3] == 0) continue;
			                if ((i1 + i2 + i3) % 3 != 0) continue;
			                if ((j1 + j2 + j3) % 3 != 0) continue;
			                res += b * a * cnt[i3][j3];
						}
					}
					cnt[i2][j2]++;
				}
			
			}
			cnt[i1][j1]++;
		}
	}
	res /= 6;
	cout << " " << res << "\n";
}
void Save()
{
}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t, tt;
	cin >> tt;
	for (t = 1; t <= tt; t++){ 
		cerr << t << "\n";
		cout << "Case #" << t << ":";                                                 
		Load();
		Solve();
		Save();
	}
	return 0;
}