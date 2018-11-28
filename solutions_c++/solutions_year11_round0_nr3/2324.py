#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

const int inf = 2147483647;

int m[1005], g[1005][50];
int maxsize;

void getbinary(int ch, int ind){
	int i = 0;
	while (ch){
		g[ind][i] = ch % 2;
		ch /= 2;
		i++;
	}
	if (i > maxsize){
		maxsize = i;
	}
}

int main(){
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int test, t, i, j, n, sum, mn;
	bool flag = false;
	scanf("%d",&test);
	for (t = 0;t < test;t++){
		if (t)
			printf("\n");
		scanf("%d",&n);
		for (i = 0;i < n;i++){
			for (j = 0;j < 30;j++){
				g[i][j] = 0;
			}
		}
		maxsize = 0;
		for (i = 0;i < n;i++){
			scanf("%d",&m[i]);
			getbinary(m[i], i);
		}
		for (i = 0;i < maxsize;i++){
			sum = 0;
			for (j = 0;j < n;j++){
				sum += g[j][i];
			}
			if (sum % 2){
				printf("Case #%d: NO",t + 1);
				flag = true;
				break;
			}
		}
		if (!flag){
			mn = inf;
			sum = 0;
			for (i = 0;i < n;i++){
				sum += m[i];
				mn = min(mn, m[i]);
			}
			printf("Case #%d: %d",t + 1,sum - mn);
		}else
		{
			flag = false;
		}
	}
	return 0;
}