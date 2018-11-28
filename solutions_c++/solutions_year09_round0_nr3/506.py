#include<stdio.h>
#include<string.h>
char str[505];

char st[30] = "welcome to code jam";
int len;
int f[505][22];
void solve()
{
	int ll = strlen(str);
	memset(f,0,sizeof(f));
	if(str[0] == 'w')f[0][0] = 1;
	for(int i = 1; i < ll; i++ ){
		if(str[i] == 'w')f[i][0] = 1;
		f[i][0] += f[i-1][0];
	}
	for(int i = 1; i < ll; i++ ){
		for(int j = 1; j < len; j++ ){
			if(f[i-1][j-1] >= 0 )
			{
				if(str[i] == st[j]){
					f[i][j] += f[i-1][j-1];
				}
			}
			f[i][j] += f[i-1][j];
			f[i][j] %= 10000;
		}
	}
	int ans = f[ll-1][len-1];
	if(ans < 10)printf("000%d\n",ans);
	else if(ans < 100)printf("00%d\n",ans);
	else if( ans < 1000)printf("0%d\n",ans);
	else printf("%d\n",ans);
}


int main()
{
	int n;
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	scanf("%d", &n);
	len = strlen(st);
	gets(str);
	for(int i = 0; i < n; i++){
		gets(str);
		printf("Case #%d: ",i+1);
		solve();
	}
}
