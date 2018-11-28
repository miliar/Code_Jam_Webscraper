#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

int n;
int pl[110][110];

int ile(int x){
	return x*x;
}

bool check(int x, int y){
	if(y < 1 || y > 2*n-1) return false;
	int l, p, g, d;
	if(x >= n){ l = x+1; p = 2*n-1; }
	else{ l = 1; p = x-1; }
	if(y >= n){ d = y+1; g = 2*n-1; }
	else{ d = 1; g = y-1; }
	for(int i=l; i<=p; ++i){
		for(int j=1; j<2*n; ++j)
			if(pl[i][j] != pl[2*x-i][j] && pl[i][j] != -1 && pl[2*x-i][j] != -1) return false;
	}
	for(int i=d; i<=g; ++i){
		for(int j=1; j<2*n; ++j)
			if(pl[j][i] != pl[j][2*y-i] && pl[i][j] != -1 && pl[j][2*y-i] != -1) return false;
	}
	return true;
}

int main()
{
	int cases;
	scanf("%d", &cases);
	for(int iii=1; iii<=cases; ++iii){
		scanf("%d", &n);
		for(int i=0; i<=2*n+2; ++i) for(int j=0; j<=2*n+2; ++j) pl[i][j] = -1;
		for(int i=1; i<=2*n-1; ++i){
			int d = n-i;
			if(i > n) d = i-n;
			for(int j=0, pos = d+1; j<n-d; pos+=2, ++j) scanf("%d", &pl[i][pos]);// printf("::%d\n", pl[i][pos]); }
		}
		//printf("wczytalem\n");
		int res;
		int x, y;
		for(int d=0; d<=2*n-2; ++d){
			for(int i=n-d; i<=n+d; ++i){
				if(i < 1 || i > 2*n-1) continue;
				int dlt = d-abs(n-i);
				if(check(i,n+dlt) || check(i,n-dlt)){
					res = d;
					x = i;
					y = n+dlt;
					goto koniec;
				}
			}
		}
		koniec:
		printf("Case #%d: %d\n", iii, ile(n+res) - ile(n));
	}
	return 0;
}
