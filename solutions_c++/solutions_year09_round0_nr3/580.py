#include <iostream>
#include <algorithm>
using namespace std;
#define MAXT 510
#define MAXP 25
char pattern[MAXP]="welcome to code jam";
char text[MAXT];
int f[MAXT][MAXP];
int sum[MAXT][MAXP];

int caseN;
int main()
{
	scanf("%d",&caseN);
	gets(text);
	for (int caseI=1;caseI<=caseN;caseI++)
	{
		gets(text);
		memset(f,0,sizeof(f));
		memset(sum,0,sizeof(sum));
		f[0][0]=sum[0][0]=1;
		for (int i=0;text[i];i++)
		{
			sum[i+1][0]=1;
			for (int j=0;pattern[j];j++)
			{
				if (text[i]==pattern[j])
					f[i+1][j+1]=sum[i][j];
				sum[i+1][j+1]=(sum[i][j+1]+f[i+1][j+1])%10000;
			}
		}
		printf("Case #%d: %04d\n",caseI,sum[strlen(text)][strlen(pattern)]);
	}
	return 0;
}

