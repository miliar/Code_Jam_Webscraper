#include <iostream>
using namespace std;
#define tiao system("pause")

const int mod = 10000;
char a[555]; //从1开始，为了方便计数 
char tmp[555];
char p[50] = "welcome to code jam"; 
int n;
int len;
int ans[30][555];

int main(void)
{
	int i,j,k,ci,cici,cicici,up;
	
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	scanf("%d",&n); gets(tmp);
	for (int cb=1; cb<=n; cb++)
	{
		gets(tmp);
		a[0] = ' ';
		strcpy(a+1,tmp);
		
		len = strlen(a);
		up = strlen(p);
		memset(ans,0,sizeof(ans));
		
		for (i=1; i<len; i++)
			if (a[i] == p[0])
				ans[0][i] = ans[0][i-1] + 1;
			else 
				ans[0][i] = ans[0][i-1];
				
		for (i=1; i<up; i++)
		{
			for (j=1; j<len; j++)
				if (a[j] == p[i])
					ans[i][j] = (ans[i][j-1] + ans[i-1][j-1]) % mod;
				else
					ans[i][j] = ans[i][j-1];
		}
		
		printf("Case #%d: %04d\n",cb,ans[up-1][len-1]);
	}	
//	tiao;
	return 0;
}
