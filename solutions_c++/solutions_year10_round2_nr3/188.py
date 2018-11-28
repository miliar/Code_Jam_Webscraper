#include <iostream>
#include <string>
#include <cstring>
#define M 100003
#define MAX 512

using namespace std;
typedef long long LL;
int C[MAX][MAX],r[MAX],a[MAX][MAX];
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T,t,i,j,k;
	C[0][0] = 1;
	for (i = 1;i < MAX;i++){
		C[i][0] = 1;
		for (j = 1;j <= i;j++){
			C[i][j] = C[i-1][j-1]+C[i-1][j];
			if (C[i][j] >= M) C[i][j] -= M;
		}
	}
	r[2] = a[2][1] = 1;
	for (i = 3;i < MAX;i++){
		r[i] = a[i][1] = 1;
		for (j = 2;j < i;j++){
			for (k = 1;k < j;k++){
				a[i][j] += (LL)a[j][k]*C[i-j-1][j-k-1] % M;
				if (a[i][j] >= M) a[i][j] -= M;
			}
			r[i] += a[i][j];
			if (r[i] >= M) r[i] -= M;
		}
	}
	scanf("%d",&T);
	for (t = 1;t <= T;t++){
		scanf("%d",&i);
		printf("Case #%d: %d\n",t,r[i]);
	}
	fclose(stdout);
}
