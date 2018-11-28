#include <iostream>
using namespace std;

const int MAXN=510;
const int len=20;
char tp[MAXN];
char key[MAXN];



int dp[MAXN][len];

int main()
{
 	freopen("c2.txt","r",stdin);
 	freopen("cs2.txt","w",stdout);
	int T;
	scanf("%d",&T);
	gets(tp);
	int b=1;

	while (T--)
	{
		gets(tp);

		int i,j;

		for (i=0,j=1;tp[i]!='\0';++i)
		{
			if (
				  tp[i]=='w'||tp[i]=='e'||tp[i]=='l'
				||tp[i]=='c'||tp[i]=='o'||tp[i]=='m'
				||tp[i]=='t'||tp[i]=='d'||tp[i]=='j'
				||tp[i]=='a'||tp[i]==' '
				)
			{
				key[j]=tp[i];
				++j;
			}
		}

		key[j]='\0';

		strcpy(tp,"welcome to code jam");

		memset(dp,0,sizeof(dp));

		for (i=1;key[i]!='\0';++i)
		{
			for (j=0;tp[j]!='\0';++j)
			{
				dp[i][j]=dp[i-1][j];

				if (key[i]==tp[j])
				{
					if (j==0)
					{
						dp[i][j]=dp[i-1][j]+1;
					}
					else
					{
						dp[i][j]+=dp[i-1][j-1];
					}
				}
				dp[i][j]%=10000;
			}
		}

		printf("Case #%d: %04d\n",b++,dp[i-1][len-2]);

	}
	return 0;
}