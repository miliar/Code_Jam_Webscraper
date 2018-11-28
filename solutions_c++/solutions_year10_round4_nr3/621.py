#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;
                           
int a[128][128];
int b[128][128];

bool check(){
	for (int i=0; i<110; ++i){
		for (int j=0; j<110; ++j){
			if (a[i][j])
				return 1;
		}	
	}
	return 0;
}

void dostep(){                
    for (int i=0; i<110; ++i){
		for (int j=0; j<110; ++j){
			b[i][j] = a[i][j];
		}
	}

    for (int i=1; i<110; ++i){
		for (int j=1; j<110; ++j){
			a[i][j] = 0;
			if ((b[i-1][j] || b[i][j-1]) && b[i][j])
				a[i][j] = 1;
			if (b[i-1][j] && b[i][j-1])
				a[i][j] = 1;
		}
	}

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
		int n;
		scanf("%d", &n);
		memset(a, 0, sizeof(a));
		for (int i=0; i<n; ++i){
			int x, xx, y, yy;
			scanf("%d%d%d%d", &x, &y, &xx, &yy);
			for (int i=min(x, xx); i<=max(x, xx); ++i){
				for (int j=min(y, yy); j<=max(y, yy); ++j){
					a[i][j] = 1;
				}			
			}                   		
		}

		int ans = 0;

		while (check()){
			++ans;
			dostep();		
		}            

        printf("%d\n", ans);
	}

	return 0;
}
