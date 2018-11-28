 //FUCK

#include<stdio.h>

int zu[4][4];
char s[100];

char output[4][100]={"Game has not completed","Draw","O won","X won"};

int test(int a,int b,int c,int d)
{
	int state=d+c*4+b*16+a*64;
	if(state==0 || state==2 || state==8 || state==32 || state==128)
	{
		return 2;
	}
	if(state==85 || state==86 || state==89 || state==101 || state==149)
	{
		return 3;
	}
	return 0;

}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	
	int t;
	scanf("%d",&t);

	for(int tt=0;tt<t;tt++)
	{
		int flag=1;
		for(int i=0;i<4;i++)
		{
			scanf("%s",&s);
			for(int j=0;j<4;j++)
			{
				if(s[j]=='O')
				{
					zu[i][j]=0;
				}
				else if(s[j]=='X')
				{
					zu[i][j]=1;
				}
				else if(s[j]=='T')
				{
					zu[i][j]=2;
				}
				else
				{
					flag=0;
					zu[i][j]=3;
				}
			}
		}

		for(int i=0;i<4;i++)
		{
			int ran=test(zu[i][0],zu[i][1],zu[i][2],zu[i][3]);
			if(ran>=2)
			{
				flag=ran;
			}
		}
		for(int i=0;i<4;i++)
		{
			int ran=test(zu[0][i],zu[1][i],zu[2][i],zu[3][i]);
			if(ran>=2)
			{
				flag=ran;
			}
		}
		int ran=test(zu[0][0],zu[1][1],zu[2][2],zu[3][3]);
		if(ran>=2)
		{
			flag=ran;
		}
		ran=test(zu[0][3],zu[1][2],zu[2][1],zu[3][0]);
		if(ran>=2)
		{
			flag=ran;
		}

		printf("Case #%d: %s\n",tt+1,output[flag]);
	}

}
