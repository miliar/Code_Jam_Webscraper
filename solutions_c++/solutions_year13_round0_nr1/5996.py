#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
char mm[5][5];
int cx[5][5];
int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	int t,i,j,cas=0;
	scanf("%d",&t);
	while(t--)
	{
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cx[i][j]=-100;
		int cc=0;
		for(i=0;i<4;i++)
		{
			scanf("%s",mm[i]);
			for(j=0;j<4;j++)
				if(mm[i][j]=='T')
					cx[i][j]=0;
				else if(mm[i][j]=='O')
					cx[i][j]=1;
				else if(mm[i][j]=='X')
					cx[i][j]=5;
				else
					cc=1;
		}
		printf("Case #%d: ",++cas);
		int sum,flag=0;
		for(i=0;i<4;i++)
		{
			sum=0;
			for(j=0;j<4;j++)
				sum+=cx[i][j];
			if(sum==4||sum==3)
			{
				flag=1;
				break;
			}
			else if(sum==20||sum==15)
			{
				flag=2;
				break;
			}
			sum=0;
			for(j=0;j<4;j++)
				sum+=cx[j][i];
			if(sum==4||sum==3)
			{
				flag=1;
				break;
			}
			else if(sum==20||sum==15)
			{
				flag=2;
				break;
			}
		}
		sum=0;
		for(i=0;i<4;i++)
			sum+=cx[i][i];
		if(sum==4||sum==3)
		{
			flag=1;
		}
		else if(sum==20||sum==15)
		{
			flag=2;
		}
		sum=0;
		for(i=0;i<4;i++)
			sum+=cx[i][3-i];
		if(sum==4||sum==3)
		{
			flag=1;
		}
		else if(sum==20||sum==15)
		{
			flag=2;
		}
		if(flag==1)
			puts("O won");
		else if(flag==2)
			puts("X won");
		else
		{
			if(cc==1)
				puts("Game has not completed");
			else
				puts("Draw");
		}
	}
	return 0;
}