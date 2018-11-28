#include <stdio.h>
#include <string.h>
#define MAX 12000000

int list[10],lNum,j;
char dp[MAX][11];
bool u[MAX];
bool check(int x,int b){
	if (dp[x][b] > -1) return dp[x][b];
	dp[x][b] = 0,u[x] = true;
	int cr = 0,fx = x,d;
//	printf("%d %d=> ",x,b);
	while (x){
		d = x % b;
		cr += d*d;
		x /= b;
	}
//	printf("%d\n",cr);getchar();
	if (cr == 1) return dp[fx][b] = 1;
	if (u[cr]) return dp[fx][b] = dp[cr][b];
	return dp[fx][b] = check(cr,b);
}
int main(){
	int T,t,i,len,d;
	char st[32];
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	memset(dp,-1,sizeof(dp));
	for (i = 2;i <= 10;i++){
		memset(u,0,sizeof(u));
		for (j = 2;j < MAX;j++)
			check(j,i);
	}
	scanf("%d",&T);
	gets(st);
	for (t = 1;t <= T;t++){
		gets(st);
		i = 0,lNum = 0;
		len = strlen(st);
		while (i < len){
			while (i < len && st[i] == ' ') i++;
			if (i < len){
				d = 0;
				while (i < len && st[i] >= '0' && st[i] <= '9')
					d = d*10+st[i++]-'0';
				list[lNum++] = d;
			}
		}
		printf("Case #%d: ",t);
		for (j = 2;j < MAX;j++)
			if (dp[j][list[0]]){
	//			printf("j = %d : ",j);for (i = 0;i < lNum;i++) printf("%d ",dp[j][list[i]]);puts("");
				for (i = 0;i < lNum;i++)
					if (dp[j][list[i]] == 0)
						break;
				if (i == lNum){
					printf("%d\n",j);
					break;
				}
			}
	}
	fclose(stdout);
}
