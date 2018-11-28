#include<cstdio>
#include<cstring>
#include<cmath>

bool dp[31][11][2];

void cal(int x, int y, int z){
	if(abs(x - y) > 2 || abs(x - z) > 2 || abs(y - z) > 2) return;

	int max = x > y ? x : y;
	max = max > z ? max : z;
	if(abs(x - y) == 2 || abs(x - z) == 2 || abs(y - z) == 2){
		for(int i = 0;i <= max;i++){
			dp[x + y + z][i][1] = true;
		}
	}else{
		for(int i = 0;i <= max;i++){
			dp[x + y + z][i][0] = true;
		}
	}
}

void init(){
	for(int i = 0;i <= 10;i++){
		for(int j = 0;j <= 10;j++){
			for(int k = 0;k <= 10;k++){
				cal(i , j, k);
			}
		}
	}
}

int a[100];

int main(){
//	freopen("in.txt" , "r" , stdin);
//	freopen("out.txt" , "w" , stdout);
	init();
	int t;
	scanf("%d" , &t);
	for(int ii = 1;ii <= t;ii++){
		int n, s, p;
		scanf("%d%d%d" , &n, &s, &p);
		int i;
		for(i = 0;i < n;i++){
			scanf("%d" , &a[i]);
		}
		int b[4];memset(b, 0, sizeof(b));
		int ret = 0;
		for(i = 0;i < n;i++){
			if(dp[a[i]][p][0] && dp[a[i]][p][1]) b[0]++;
			if(!dp[a[i]][p][0] && !dp[a[i]][p][1]) b[1]++;
			if(!dp[a[i]][p][0] && dp[a[i]][p][1]) b[2]++;
			if(dp[a[i]][p][0] && !dp[a[i]][p][1]) b[3]++;
		}
		if(s <= b[2]){
			ret = b[0] + b[3] + s;
		}else if(s <= b[2] + b[0] + b[1]){
			ret = b[0] + b[3] + b[2];
		}else{
			ret = b[0] + b[3] + b[2] - (s - b[2] - b[0] - b[1]);
		}

		printf("Case #%d: %d\n" , ii, ret);
	}
	return 0;
}