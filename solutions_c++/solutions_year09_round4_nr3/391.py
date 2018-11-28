#include <iostream>
#include <cstring>
using namespace std;

const int NMAX = 16;
const int KMAX = 25;

int h[NMAX][KMAX];
int mat[NMAX][NMAX];
int sol[NMAX + 2][1<<(NMAX + 1)];


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n, t;
	cin>>t;
	for (int nt = 1; nt <= t; ++nt) {
		int k;
		cin>>n>>k;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < k; ++j)
				cin>>h[i][j];

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) 
			if (i != j) {
				bool ok = true;
				for (int l = 0; l < k && ok; ++l) 
					if (h[i][l] <= h[j][l]) 
						ok = false;
				mat[i][j] = ok;
			}
		}

		memset(sol, -1, sizeof(sol));
		for (int i = 0; i< n; ++i)
			sol[i][1<<i] = 1;

		for (int i = 0; i < (1<<n); ++i) {
			for (int j = 0; j < n; ++j) {
				if (sol[j][i] != -1) {
					for (int k = 0; k < n; ++k) {
						if ((i & (1<<k)) == 0) {
							int nc = i ^ (1<<k);
							if (mat[k][j]) {
								if (sol[k][nc] == -1 || sol[k][nc] > sol[j][i])
									sol[k][nc] = sol[j][i];
							} else {
								if (sol[k][nc] == -1 || sol[k][nc] > sol[j][i] + 1)
									sol[k][nc] = sol[j][i] + 1;
							}
						}
					}
				}
			}
		}
		
		int ret = 100;
		for (int i = 0; i < n; ++i)
			if (sol[i][(1<<n) - 1] != -1)
				ret = min(ret, sol[i][(1<<n) - 1]);
		if (n <= 6) {
			cerr<<"***"<<endl;
			cerr<<n<<endl;
			for (int i = 0; i < n; ++i, cerr<<endl)
				for (int j = 0; j < k; ++j)
					cerr<<h[i][j]<<" ";
			cerr<<ret;
		}
		cout<<"Case #"<<nt<<": "<<ret<<endl;
	}
	return 0;
}