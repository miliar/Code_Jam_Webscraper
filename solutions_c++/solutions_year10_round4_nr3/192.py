#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
using namespace std;
bool hash[113][113];
bool tp1[113][113];
int i,j,k,n,m;
int main() {
	int cas;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("Czl.out","w",stdout);
	scanf("%d",&cas);
	int b = 1;
	while (cas--){
		scanf("%d", &n);
		while (n--){
			int x0,x1,y0,y1;
			scanf("%d%d%d%d",&x0, &y0, &x1, &y1);
			for ( i = x0; i <= x1; ++i) {
				for (j = y0; j<= y1; ++j) {
					hash[j][i] = true;
				}
			}
		}
		int T = 0;
		while (1)
		{
			bool flag=true;
			for (i =1;i<=100;++i) {
				for (j=1;j<=100;++j) {
					if (hash[i][j]) {
						flag=false;
						break;
					}
					if (!flag) break; 
				}
			}
			if (flag) {
				break;
			}
			memset(tp1,0, sizeof(tp1));
			for ( i = 1; i <= 100; ++i) {
				for ( j = 1 ; j<= 100; ++j) {
					if (hash[i][j]) {
						if (hash[i-1][j]||hash[i][j-1]) {
							tp1[i][j]=true;
						}
					} else {
						if (hash[i-1][j] && hash[i][j-1]) {
							tp1[i][j]=true;
						}
					}
				}
			}
			++T;
			memcpy(hash,tp1,sizeof(hash));
		}
		printf("Case #%d: ",b);
		printf("%d\n", T);
		++b;
	}
}
