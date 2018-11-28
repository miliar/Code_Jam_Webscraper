#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>

using namespace std;

int main() 
{
    freopen("C-large.in", "r", stdin);
    ofstream fp("C-large.out");

	int g[1001] = {};
	int f[1001][2] = {};
	bool mark[1001] = {};

	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		int R, k, N;
		scanf("%d%d%d", &R, &k, &N);
		for(int j = 0; j < N; j++) {
			scanf("%d", &(g[j]));
		}
		for(int j = 0; j < N; j++) {
			int val = g[j], p = j;
			while(true) {
				if(++p >= N) {
					p -= N;
				}
				if(p == j) break;
				if(val + g[p] <= k) {
					val += g[p];
				}
				else {
					break;
				}
			}
			f[j][0] = p;	
			f[j][1] = val;
			//cout << i << " " << f[j][0] << " " << f[j][1] << endl;
		}

		memset(mark, 0, sizeof(mark));
		int p = 0;
		long long res = 0; 
		while(R > 0) {
			res += f[p][1];
			mark[p] = 1;
			R--;
			p = f[p][0];

			if(mark[p]) {
				long long price = f[p][1];
				int cnt = 1;
				int q = f[p][0];
				while(q != p) {
					price += f[q][1];
					q = f[q][0];
					cnt++;
				}
				int d = R / cnt;
				res += price * d;
				R -= d * cnt;

				while(R > 0) {
					res += f[p][1];
					p = f[p][0];
					R--;
				}
			}

		}
		
		fp << "Case #" << i+1 << ": " << res << endl;
	}

    fp.close();
    return 0;
}
