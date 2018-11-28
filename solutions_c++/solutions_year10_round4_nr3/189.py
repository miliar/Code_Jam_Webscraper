#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;
const int maxn = 110;

bool a[maxn][maxn], b[maxn][maxn];
int task, T=0, r, x1, x2, y1, y2, ret;

int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("a.out","w",stdout);
	for (scanf("%d", &task); task--;){
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));

		scanf("%d", &r);
		for (int i=0; i<r; i++){
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			x1++; y1++; x2++; y2++;
			for (int x=x1; x<=x2; x++)
			for (int y=y1; y<=y2; y++)
					a[x][y] = true;
		}

		ret = 0;
		while (true){
			bool ok = 0;
			memset(b, 0, sizeof(b));
			for (int i=1; i<=101; i++)
			for (int j=1; j<=101; j++)
			if (a[i][j]){
				ok = true;
				b[i][j] = a[i-1][j] || a[i][j-1];
			}else b[i][j] = a[i-1][j] && a[i][j-1]; 

			if (!ok) break;

			ret++;
			for (int i=0; i<=101; i++)
			for (int j=0; j<=101; j++)
				a[i][j] = b[i][j];
		}
		printf("Case #%d: %d\n", ++T, ret);
	}
	return 0;
}
