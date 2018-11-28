#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main()
{
//	freopen("A-large.in","r",stdin);
//	freopen("out","w",stdout);
	int t;
	char a[4][4];
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++)
	{
		for(int i=0;i<4;i++)
			scanf("%s",a[i]);		
		int b[4][4],r[5]={0},c[5]={0};
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[i][j]=='X')
					b[i][j]=1;
				else if(a[i][j]=='O')
					b[i][j]=10;
				else if(a[i][j]=='.')
					b[i][j]=10000;
				else if(a[i][j]=='T')
					b[i][j]=1000;
				r[i]+=b[i][j];
				c[j]+=b[i][j];
			}
		}
		r[4]=b[0][0]+b[1][1]+b[2][2]+b[3][3];
		c[4]=b[0][3]+b[1][2]+b[2][1]+b[3][0];
		int x4=4,x3t=1003,o4=40,o3t=1030;
		int flag=0;
		for(int i=0;i<5;i++)
		{
			if(r[i]==x4||r[i]==x3t||c[i]==x4||c[i]==x3t)
			{
				printf("Case  #%d: X won\n",cas);
				flag=1;
				break;
			}	
			else if(r[i]==o4||r[i]==o3t||c[i]==o4||c[i]==o3t)
			{
				printf("Case  #%d: O won\n",cas);
				flag=1;
				break;
			}
			if(r[i]>=10000||c[i]>=10000)
				flag=2;	
		}
		if(flag!=1&&flag==2)
			printf("Case  #%d: Game has not completed\n",cas);
		else if(flag==0)
			printf("Case  #%d: Draw\n",cas);
	}
	return 0;
}