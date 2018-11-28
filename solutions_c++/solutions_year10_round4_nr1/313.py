#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

int n;
int a[64][64];                                       

bool good2(int x, int y, int xx, int yy){
	for (int i=0; i<=xx-x; ++i){
		for (int j=0; j<=yy-y; ++j){
			if (a[x+i][y+j] != a[x+j][y+i])
				return 0;
//			if (a[x+i][y+j] != a[xx-i][yy-j])
//				return 0;                  
		}
	}
	return 1;
}


bool good1(int x, int y, int xx, int yy){
	for (int i=0; i<=xx-x; ++i){
		for (int j=0; j<=yy-y; ++j){
//			if (a[x+i][y+j] != a[x+j][y+i])
//				return 0;
			if (a[x+i][y+j] != a[xx-j][yy-i])
				return 0;                  
		}
	}
	return 1;
}


int main(){
#ifndef ONLINE_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int ntest;
	scanf("%d", &ntest);

	for (int itest=0; itest<ntest; ++itest){
		printf("Case #%d: ", itest+1);
		scanf("%d", &n);
		for (int i=0; i<2*n-1; ++i){
			int x = i, y = 0;
			              
			if (i>=n){
				x = n-1;
				y = i-n+1;			
			}
			while (x>=0 && y<n){
				scanf("%d", &a[x][y]);
				--x; ++y;
			}
		}
//		return 0;

		int l1 = 1;
		int l2 = 1;     
		for (int i=n-1; i>=1; --i){         
			if (good1(0, 0, i, i) || good1(n-i-1, n-i-1 ,n-1, n-1)){
				l1 = i+1;
				break;
			}
		}

		for (int i=n-1; i>=1; --i){         
			if (good2(0, n-i-1, i, n-1) || good2(n-i-1, 0 ,n-1, i)){
				l2 = i+1;
				break;
			}
		}

//        long long ans = min(3*n-l1-l2, 2*n-max(l1, l2));

		long long ans = 3*n-l1-l2;


        ans = ans * ans - n * n;

		printf("%lld\n", ans);	
	}

	return 0;
}
