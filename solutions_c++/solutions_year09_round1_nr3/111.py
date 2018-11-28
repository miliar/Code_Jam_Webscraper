#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

const int maxn=41;

int C,N;
double c[maxn][maxn];
double f[maxn];

int main() {
	memset(c,0,sizeof(c));
	for (int i=0; i<=maxn; i++) {
		c[i][0] = 1.0;
		for (int j=1;j<=i; j++)
			c[i][j] = c[i-1][j-1] + c[i-1][j];
	}

	freopen( "input.txt", "r", stdin );
	freopen("output.txt","w",stdout);
	int t, task = 0;
	double temp;
	cin >> t;
	while (t!=0)
	{
		t--;
		task++;
		cin >> C >> N;
		memset(f, 0, sizeof(f));
		for (int i=C-1; i>=N; i--) {
			temp = 1.0;
			for (int j=i+1; j<=C; j++)
				if (j<=i+N)
					temp += ((j-i>N)?0:c[i][N-j+i] * c[C-i][j-i] / c[C][N]) * f[j];
			f[i] = temp/(1 - c[i][N] * c[C-i][0] / c[C][N]);
		}
		printf("Case #%d: %.6lf\n", task, f[N] + 1.0 );
	}

	return 0;
}


