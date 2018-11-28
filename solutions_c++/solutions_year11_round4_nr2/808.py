#include <cstdio>
#include <deque>
#include <vector>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <set>
#include <map>

using namespace std;
typedef long long ll;
int T;

char inp[512][512];
ll in[512][512];
ll dp[512][512];
int R, C, D;

inline ll get_reg(int r1, int c1, int r2, int c2){
	ll tr = dp[r2][c2];
	if (r1) tr -= dp[r1-1][c2];
	if (c1) tr -= dp[r2][c1-1];
	if (r1 && c1) tr += dp[r1-1][c1-1];
	return tr;
}
bool validate(int r, int c, int k){
	ll x, y;
	x = y = 0;

	for (int i=r-k;i<=r+k;++i){
	for (int j=c-k;j<=c+k;++j){
		if (i < 0 || j < 0 || i >= R || j >= C) return false;
		if (j == c-k && i == r-k) continue;
		if (j == c+k && i == r-k) continue;
		if (j == c+k && i == r+k) continue;
		if (j == c-k && i == r+k) continue;
		x += in[i][j] * (r-i);
		y += in[i][j] * (c-j);
	}
	}
	return (x == 0 && y == 0);
}
bool validate2(int r, int c, int k){
	ll x, y;
	x = y = 0;
	for (int i=r-k+1;i<=r+k;++i){
	for (int j=c-k+1;j<=c+k;++j){
		if (i < 0 || j < 0 || i >= R || j >= C) return false;

		if (j == c-k+1 && i == r-k+1) continue;
		if (j == c+k && i == r-k+1) continue;
		if (j == c+k && i == r+k) continue;
		if (j == c-k+1 && i == r+k) continue;
		
		if (i <= r) x += in[i][j] * (r-i+1);
		else x += in[i][j] * (r-i);
		
		if (j <= c) y += in[i][j] * (c-j+1);
		else y += in[i][j] * (c-j);
	}
	}
	return (x == 0 && y == 0);
}
void solve(){
	int bk = 0;
	scanf ("%d %d %d", &R, &C, &D);
	for (int i=0;i<R;++i){
		scanf(" %s", inp[i]);
		for (int j=0;j<C;++j){
			in[i][j] = D+(inp[i][j] - '0');
		}
	}
	
	for(int i=0;i<R;++i){
		for (int j=0;j<C;++j){
			dp[i][j] = in[i][j];
			if (i) dp[i][j] += dp[i-1][j];
			if (j) dp[i][j] += dp[i][j-1];
			if (i && j) dp[i][j] -= dp[i-1][j-1];
		}
	}
	
	int mk = min(R, C);
	
	for (int i=0;i<R;++i){
	for (int j=0;j<C;++j){
		ll x = 0, y = 0;
		for (int k=max(bk/2,1);k<mk;k++){
			if ( i-k < 0 || i+k >= R) break;
			if ( j-k < 0 || j+k >= C) break;
	
			for (int l=i-k;l<=i+k;++l){
				ll sum;
				if (l == i-k || l==i+k){
					sum = get_reg(l,j-k+1, l, j+k-1);
				}else if (l == i-k+1 || l == i+k-1){
					sum = get_reg(l,j-k, l, j+k);
					sum -= get_reg(l,j-k+2,l,j+k-2);
				}else{
					sum = in[l][j-k] + in[l][j+k];
				}
				sum *= (i-l);
				x += sum;
			}

			for (int l=j-k;l<=j+k;++l){
				ll sum;
				if (l == j-k || l==j+k){
					sum = get_reg(i-k+1,l,i+k-1,l);
				}else if (l == j-k+1 || l == j+k-1){
					sum = get_reg(i-k,l,i+k,l);
					sum -= get_reg(i-k+2, l, i+k-2,l);
				}else{
					sum = in[i-k][l] + in[i+k][l];
				}
				sum *= (j-l);
				y += sum;
			}
			
			if (x == 0 && y == 0){
				bk = max(bk,k * 2 + 1);
			}
		}
		
		x = y = 0;
		for (int k=max((bk+1)/2,2);k<mk;++k){
			if ( i-k+1 < 0 || i+k >= R) break;
			if ( j-k+1 < 0 || j+k >= C) break;

			for (int l=i-k+1;l<=i+k;++l){
				ll sum;
				if (l == i-k+1 || l==i+k){
					sum = get_reg(l,j-k+2, l, j+k-1);
				}else if (l == i-k+2 || l == i+k-1){
					sum = get_reg(l,j-k+1, l, j+k);
					sum -= get_reg(l,j-k+3,l,j+k-2);
				}else{
					sum = in[l][j-k+1] + in[l][j+k];
				}
				if (l <= i) sum *= (i-l+1);
				else sum *= (i-l);
				x += sum;
			}

			for (int l=j-k+1;l<=j+k;++l){
				ll sum;
				if (l == j-k+1 || l==j+k){
					sum = get_reg(i-k+2,l,i+k-1,l);
				}else if (l == j-k+2 || l == j+k-1){
					sum = get_reg(i-k+1,l,i+k,l);
					sum -= get_reg(i-k+3, l, i+k-2,l);
				}else{
					sum = in[i-k+1][l] + in[i+k][l];
				}
				if (l <= j) sum *= (j-l+1);
				else sum *= (j-l);
				y += sum;
			}
			
			if (x == 0 && y == 0){
				bk = max(bk,k * 2);
			}

			//if (i==j && i == 3){
				//printf("%d %lld %lld\n", k, x, y);
			//}
		}
	}
	}
	
	
	if (bk == 0){
		printf("IMPOSSIBLE\n");
	}else{
		printf("%d\n", bk);
	}
}

void solve2(){
	int bk = 0;
	scanf ("%d %d %d", &R, &C, &D);
	for (int i=0;i<R;++i){
		scanf(" %s", inp[i]);
		for (int j=0;j<C;++j){
			in[i][j] = D+(inp[i][j] - '0');
		}
	}
	
	int mk = min(R, C);
	
	for (int i=0;i<R;++i){
	for (int j=0;j<C;++j){
		for (int k=1;k<mk;++k){
			if (validate(i, j,k)) bk = max(bk, k*2+1);
			if (k>1) if (validate2(i, j,k)) bk = max(bk, k*2);
		}
	}
	}
	
	
	if (bk == 0){
		printf("IMPOSSIBLE\n");
	}else{
		printf("%d\n", bk);
	}
}

int main(){
	scanf("%d", &T);

	for (int tc=1;tc<=T;++tc){
		printf("Case #%d: ", tc);
		solve2();
	}

	return 0;
}

