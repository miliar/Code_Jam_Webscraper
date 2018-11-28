#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <math.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#pragma comment (linker, "/STACK:256000000")
using namespace std;
const int maxn = 510;
char str[maxn]={0};
int a[maxn][maxn]={{0}};
void solve() {
	int i,j,n,m,d;
	scanf("%d %d %d\n",&n,&m,&d);
	for (int i = 1; i <= n; ++i) {
		gets(str);
		for (j=0;j<m;++j) {
			a[i][j+1] = str[j] - '0';
		}
	}
	int to = min(n,m);
	int res = -1,xx,yy,len;
	double cx, cy, sx, sy ;
	const double eps = 1e-8;
	int ii;
	for (len = to; len >= 3; --len) {
		for (ii=1;ii<=n-len+1;++ii) {
			for (j=1;j<=m-len+1;++j) {
				
//				cout << len << " " <<  i << " " << j << "\n";
				if (len & 1) {
					cx = ii + (len + 0) / 2;
					cy = j + (len + 0) / 2;
				}
				else {
					cx = ii + len / 2 - 0.5;
					cy = j + len / 2 - 0.5;
				}
				sx = 0;
				sy = 0;
				for (xx=0;xx<len;++xx) {
					for (yy=0;yy<len;++yy) {
						if (xx==0 && (yy==0 || yy==len-1))
							continue;
						if (xx==len-1 && (yy==0 || yy==len-1))
							continue;
						sx += ((ii + xx) - cx) * (a[ii+xx][j+yy] + d);
						sy += ((j + yy) - cy) * (a[ii+xx][j+yy] + d);
					}
				}
				if (fabs(sx) <= eps && fabs(sy) <= eps ) {
					res= len;
					printf("%d\n",res);
					return;
				}
			}
		}
	}

	if (res==-1)
		printf("IMPOSSIBLE\n");
	else printf("%d\n",res);
}
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, tst;
	cin >> t;
	for (tst = 1; tst <= t; ++tst) {
		cout << "Case #" << tst << ": ";
		solve();
	}
	
	return 0;
}