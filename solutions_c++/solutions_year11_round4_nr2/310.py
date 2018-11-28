#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <memory.h>
#include <queue>
#include <string>
#include <string.h>
#include <cmath>
#include <utility>
#include <time.h>


typedef long long LL;
typedef unsigned long long ULL;

#define PI 3.1415926535897932384626433832795
#define sqr(x) ((x)*(x))
#define OUT_RT cerr << (float(clock()) / CLOCKS_PER_SEC) << endl

using namespace std;

int T;

#define S(s,x1,y1,x2,y2) (s[x2][y2] - s[(x1)-1][y2] - s[x2][(y1)-1] + s[(x1)-1][(y1)-1])

ULL sum[555][555], sumx[555][555], sumy[555][555];
char a[555][555];

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		
		int n,m,d;
		cin >> n >> m >> d;
		for(int i=1;i<=n;i++) cin >> (a[i] + 1);

		for(int i=0;i<=n;i++) sum[i][0] = sumx[i][0] = sumy[i][0] = 0;
		for(int j=0;j<=m;j++) sum[0][j] = sumx[0][j] = sumy[0][j] = 0;
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++){
				ULL mm = a[i][j] - 48 + d;
				sum[i][j] = sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1] + mm;
				sumx[i][j] = sumx[i-1][j] + sumx[i][j-1] - sumx[i-1][j-1] + mm * i;
				sumy[i][j] = sumy[i-1][j] + sumy[i][j-1] - sumy[i-1][j-1] + mm * j;
			}
			             
		int ans;
		for(ans = min(n, m);ans>2;ans--){
			bool found = false;
			ULL s1,s2,s3;
			for(int i=1;i<=n-ans+1 && !found;i++)
				for(int j=1;j<=m-ans+1;j++){
					s1 = S(sum, i+1, j, i+ans-2, j+ans-1) + S(sum, i, j+1, i+ans-1, j+ans-2) - S(sum, i+1, j+1, i+ans-2, j+ans-2);
					s2 = S(sumx, i+1, j, i+ans-2, j+ans-1) + S(sumx, i, j+1, i+ans-1, j+ans-2) - S(sumx, i+1, j+1, i+ans-2, j+ans-2);
					s3 = S(sumy, i+1, j, i+ans-2, j+ans-1) + S(sumy, i, j+1, i+ans-1, j+ans-2) - S(sumy, i+1, j+1, i+ans-2, j+ans-2);
					int cx = i + i + (ans - 1);
					int cy = j + j + (ans - 1);
					if(s2 + s2 == s1 * cx && s3 + s3 == s1 * cy){
						found = true;
						break;
					}
				}
			if(found) break;
		}

		printf("Case #%d: ",_);
		if(ans<3) puts("IMPOSSIBLE");else
			  cout << ans << endl;
		fflush(stdout);
	}
	return 0;
}
