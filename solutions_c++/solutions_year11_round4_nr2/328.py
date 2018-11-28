#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define EPS 1e-8

int T;

long long sumx[505][505];
long long sumy[505][505];
long long sum[505][505];
int arr[505][505];
char buf[505][505];

int prev(int x){
	return x & (x - 1);
}

int next(int x){
	return (x<<1) - prev(x);
}

void modify(int x, int y, int val){
	while (x < 505){
		int y1 = y;
		while (y1 < 505){
			sum[x][y1] += val;
			y1 = next(y1);
		}
		x = next(x);
	}
}

void modify_x(int x, int y, int val){
	while (x < 505){
		int y1 = y;
		while (y1 < 505){
			sumx[x][y1] += val;
			y1 = next(y1);
		}
		x = next(x);
	}
}

void modify_y(int x, int y, int val){
	while (x < 505){
		int y1 = y;
		while (y1 < 505){
			sumy[x][y1] += val;
			y1 = next(y1);
		}
		x = next(x);
	}
}

long long find_sum(int x, int y){
	long long ret = 0;
	while (x > 0){
		int y1 = y;
		while (y1 > 0){
			ret += sum[x][y1];
			y1 = prev(y1);
		}
		x = prev(x);
	}
	return ret;
}

long long find_sumx(int x, int y){
	long long ret = 0;
	while (x > 0){
		int y1 = y;
		while (y1 > 0){
			ret += sumx[x][y1];
			y1 = prev(y1);
		}
		x = prev(x);
	}
	return ret;
}

long long find_sumy(int x, int y){
	long long ret = 0;
	while (x > 0){
		int y1 = y;
		while (y1 > 0){
			ret += sumy[x][y1];
			y1 = prev(y1);
		}
		x = prev(x);
	}
	return ret;
}

long long find_sum(int l, int t, int r, int b){
	return find_sum(r, b) - find_sum(r, t-1) - find_sum(l-1, b) + find_sum(l-1, t-1);
}

long long find_sumx(int l, int t, int r, int b){
	return find_sumx(r, b) - find_sumx(r, t-1) - find_sumx(l-1, b) + find_sumx(l-1, t-1);
}

long long find_sumy(int l, int t, int r, int b){
	return find_sumy(r, b) - find_sumy(r, t-1) - find_sumy(l-1, b) + find_sumy(l-1, t-1);
}

int main(){
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	cin >> T;
	for (int I=0; I<T; I++){
		cout << "Case #" << I+1 << ": ";
		memset(sum, 0, sizeof sum);
		memset(sumx, 0, sizeof sumx);
		memset(sumy, 0, sizeof sumy);
		int r, c, d;
		cin >> r >> c >> d;
		for (int i=0; i<r; i++){
			cin >> buf[i];
		}
		for (int i=0; i<r; i++){
			for (int j=0; j<c; j++){
				arr[i][j] = d + buf[i][j] - '0';
				modify_x(i+1, j+1, arr[i][j]*(i+1));
				modify_y(i+1, j+1, arr[i][j]*(j+1));
				modify(i+1, j+1, arr[i][j]);
			}
		}

		bool good = false;

		for (int k=min(r, c); k>2; k--){
			for (int i=k; i<=r; i++){
				for (int j=k; j<=c; j++){
					long long vx = find_sumx(i-k+1, j-k+1, i, j) - find_sumx(i-k+1, j-k+1, i-k+1, j-k+1) 
						- find_sumx(i-k+1, j, i-k+1, j) - find_sumx(i, j-k+1, i, j-k+1)
						- find_sumx(i, j, i, j);
					long long vy = find_sumy(i-k+1, j-k+1, i, j) - find_sumy(i-k+1, j-k+1, i-k+1, j-k+1) 
						- find_sumy(i-k+1, j, i-k+1, j) - find_sumy(i, j-k+1, i, j-k+1)
						- find_sumy(i, j, i, j);
					long long v = find_sum(i-k+1, j-k+1, i, j) - find_sum(i-k+1, j-k+1, i-k+1, j-k+1) 
						- find_sum(i-k+1, j, i-k+1, j) - find_sum(i, j-k+1, i, j-k+1)
						- find_sum(i, j, i, j);
					if (k & 1){
						long long vvx = v*(i - k/2);
						long long vvy = v*(j - k/2);
						if (vx == vvx && vy == vvy){
							cout << k << endl;
							good = true;
							i = r;
							j = c;
							k = 0;
							break;
						}
					} else {
						long long vvx = v*(2*i - k+1);
						long long vvy = v*(2*j - k+1);
						if (2*vx == vvx && 2*vy == vvy){
							cout << k << endl;
							good = true;
							i = r;
							j = c;
							k = 0;
							break;
						}
					}
				}
			}
		}

		if (!good){
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}