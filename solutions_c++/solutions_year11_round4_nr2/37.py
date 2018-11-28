//be name oo
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <utility>
#include <cstring>
#include <sstream>
#include <complex>
#include <vector>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define F first
#define S second

using namespace std;
typedef pair<int, int> joft;
typedef complex<double> point;

const int MAX_N = 500 + 10;

int r, c, d;
char tab[3][MAX_N][MAX_N];
long long sum[3][MAX_N][MAX_N];

long long finds(long long a[MAX_N][MAX_N], char tab[MAX_N][MAX_N], int i, int j, int k){
	long long ret = a[i + k - 1][j + k - 1];
	if(i > 0)
		ret -= a[i - 1][j + k - 1];
	if(j > 0)
		ret -= a[i + k - 1][j - 1];
	if(i > 0 && j > 0)
		ret += a[i - 1][j - 1];
	
	//cerr<< ret << endl;
	
	ret -= tab[i][j];
	ret -= tab[i][j + k - 1];
	ret -= tab[i + k - 1][j];
	ret -= tab[i + k - 1][j + k - 1];
	return ret;
}

int main(){
	int testN;
	cin >> testN;
	FOR(test, testN){
		scanf("%d %d %d", &r, &c, &d);
		FOR(i, r){
			scanf(" %s", tab[0][i]);
			FOR(j, c){
				tab[0][i][j] -= '0';
				tab[1][i][j] = tab[0][i][j] * i;
				tab[2][i][j] = tab[0][i][j] * j;
			}
		}
		FOR(cnt, 3)
			FOR(i, r)
				FOR(j, c){
					sum[cnt][i][j] = tab[cnt][i][j];
					if(i)
						sum[cnt][i][j] += sum[cnt][i - 1][j];
					if(j)
						sum[cnt][i][j] += sum[cnt][i][j - 1];
					if(i && j)
						sum[cnt][i][j] -= sum[cnt][i - 1][j - 1];
				}
				
		int ans = -1;
		for(int k = min(r, c); k >= 3 && ans == -1; k--)
			for(int i = 0; i + k <= r; i++)
				for(int j = 0; j + k <= c; j++){
					long long alls = finds(sum[0], tab[0], i, j, k);
					long long sumx = 2 * finds(sum[1], tab[1], i, j, k);
					long long sumy = 2 * finds(sum[2], tab[2], i, j, k);
					long long tarx = alls * (2 * i + k - 1);
					long long tary = alls * (2 * j + k - 1);
					if(sumx == tarx && sumy == tary)
						ans = k;
				}
		if(ans == -1)
			printf("Case #%d: IMPOSSIBLE\n", test + 1);
		else	printf("Case #%d: %d\n", test + 1, ans);

	}
	return 0;
}
