#include <iostream>
#include <cmath>
using namespace std;

int main(){
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B.out","w",stdout);
	int test;
	int Area;
	int Case = 0;
	scanf("%d", &test);
	while (test--){
		Case++;
		int n ,m;
		scanf("%d%d%d", &n, &m, &Area);
		bool flag = false;
		int i , j, k, l;
		printf("Case #%d:", Case);
		for (i = 0; i <= n; i ++){
			for (j = 0; j <= n; j ++){
				for (k = 0; k <= m; k ++){
					for (l = 0; l <= m; l ++){
						if (abs(i * l - j * k) == Area){
							flag = 1;
							printf(" 0 0 %d %d %d %d\n", i, k, j, l);
							break;
						}
					}
					if (flag == 1)
						break;
				}
				if (flag == 1)
					break;
			}
			if (flag == 1)
				break;
		}
		if (flag == 0)
			printf(" IMPOSSIBLE\n");
	}
	return 0;
}