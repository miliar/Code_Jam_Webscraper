//Welcome to Code Jam

//welcome to code jam

#include <stdio.h>
#include <string.h>

const int N=510;
const int m=19;

int an[N][m];
char a[N];
char s[m+1]="welcome to code jam";

int main()
{
	freopen("C-large.in.txt","r",stdin);
	freopen("C.out","w",stdout);
	int max;
	scanf("%d\n",&max);
	int i,j,k,l;
	int t,n;
	int answer;
	for (t=1;t<=max;t++)
	{
		gets(a);
//		printf("%s\n",a);
		memset(an,0,sizeof(an));
		n=strlen(a);
		answer=0;
		for (i=0;i<n;i++)
		{
			for (j=0;j<m;j++)
			{
				if (a[i]==s[j])
				{
					if (j==0)
					{
						an[i][j]=1;
					}
					else
					{
						for (k=0;k<i;k++)
						if (an[k][j-1]>0)
						{
							an[i][j]+=an[k][j-1];
							if (an[i][j]>=10000)
							{
								an[i][j]%=10000;
							}
						}
					}
				}
			}
			answer+=an[i][m-1];
			if (answer>=10000)
			{
				answer%=10000;
			}
		}
		printf("Case #%d: ",t);
		if (answer<1000)
		{
			printf("0");
		}
		if (answer<100)
		{
			printf("0");
		}
		if (answer<10)
		{
			printf("0");
		}
		printf("%d\n",answer);

	}



	return 0;
}
