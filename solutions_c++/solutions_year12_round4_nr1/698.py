#include<cstdio>
#include<algorithm>
#include<vector>
#include<queue>
#include<iostream>

#define N 10005
using namespace std;

int n,m;
int data[N][2], table[N];
int main(){
	int i,j,k;
	int tc;
	int ans;
	FILE *out = fopen("output.txt", "w");
	freopen("input.txt", "r", stdin);
	scanf("%d", &tc);
	for(int tcc = 1; tcc<=tc; tcc++){
		memset(table, 0, sizeof(table));
		ans = 0;
		scanf("%d", &n);
		data[0][0] = 0;
		for(i=1;i<=n;i++){
			scanf("%d %d", &data[i][0], &data[i][1]);
		}
		scanf("%d",&m);
		table[0] = data[1][0];
		for(i=0;i<=n;i++){
			if (data[i][0] + table[i] >= m){
				ans = 1;
				break;
			}
			for(j=i+1;j<=n;j++){
				if (data[i][0] + table[i] < data[j][0]) break;
				k = min(data[j][1], data[j][0]-data[i][0]);
				if (table[j] < k)
					table[j]=k;
			}
		}
		//if (table[n] + data[n][0] >= m) ans = 1;
		printf("case %d %d\n", tcc, n);
		fprintf(out, "Case #%d: %s\n", tcc, (ans==1)? "YES":"NO");
	}
	return 0;
}