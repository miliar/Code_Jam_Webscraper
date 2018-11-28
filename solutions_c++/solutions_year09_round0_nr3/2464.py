#include <stdio.h>
#include <string.h>

const int maxN = 500 + 50;

char str[maxN];
const char *welcome="welcome to code jam";
int len = strlen(welcome);
int f[15][maxN];

int main()
{
	int t;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);getchar();
	for(int Case = 1 ; Case <= t ; ++Case)
	{
		memset(f , 0 , sizeof(f));
		gets(str);
		int slen = strlen(str);
		for(int i = 0 ; i < slen ; ++i)
			if(str[i] == welcome[0]) 
			{
				if(i)
					f[0][i] = f[0][i-1]+1;
				else f[0][i] = 1;
			}else f[0][i] = f[0][i-1];
		for(int i = 1 ; i < len ; ++i)
			for(int j = i ; j < slen - len + i + 1 ; ++j)
			if(str[j] == welcome[i])
			{
				f[i][j] = f[i-1][j-1]+f[i][j-1];
			}
			else f[i][j] = f[i][j-1];
		int ans = f[len-1][slen-1];
		int k = 0;
		while(ans)
		{
			++k;
			ans/=10;
		}
		printf("Case #%d: ",Case);
		for(int i = 1 ; i <= 4 - k ; ++i)
			printf("0");
		if(k)printf("%d\n",f[len-1][slen-1]);else puts("");
	}
	return 0;
}
