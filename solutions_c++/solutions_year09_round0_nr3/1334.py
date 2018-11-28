#include<stdio.h>
#include<string>

using namespace std;

int mic[20][500];

void print(int ans)
{
	if(ans < 10)
		printf("000%d\n",ans);
	else if(ans <100)
		printf("00%d\n",ans);
	else if(ans <1000)
		printf("0%d\n",ans);
	else
		printf("%d\n",ans);
}

int main()
{
	char pattern[]="welcome to code jam";
	char para[503];
	int N;
	scanf("%d\n",&N);
	for(int round=1;round<=N;round++)
	{
		gets(para);
		//printf("%s\n",para);
		int l = strlen(para);
		for(int i=18;i>=0;i--)
			for(int j=l-1;j>=0;j--)
				mic[i][j] = 0;
		for(int i=18;i>=0;i--)
			for(int j=l-1;j>=0;j--)
			{
				if(pattern[i] == para[j])
				{
					
					if(j==l-1 && i == 18)
						mic[i][j] = 1;
					else if(j==l-1)
						mic[i][j] = 0;
					else if(i == 18)
						mic[i][j] = (mic[i][j+1]+1)%10000;
					else
						mic[i][j] = (mic[i][j+1] + mic[i+1][j+1])%10000;
				}
				else
				{
					if(j == l-1)
						mic[i][j] = 0;
					else	
						mic[i][j] = (mic[i][j+1])%10000;
				}
			}
		/*for(int i=0;i<19;printf("\n"),i++)
			for(int j=0;j<l;j++)
				printf("%d\t",mic[i][j]);*/
		printf("Case #%d: ",round);
		print(mic[0][0]);
	}
	return 0;
}
