#include<iostream>
#include<cmath>
using namespace std;
const int inf=1000;
int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int zu;
	int g=1;
	scanf("%d",&zu);

	while(zu--)
	{
		int m;
		scanf("%d",&m);
		int x=m;
		int a=1;
		int d=2;
		while(x)
		{
			while(!(x&1))
				x>>=1,d=d*d%inf;
			x--;
			a=a*d%inf;
		}
		int b=a*2%inf;
		int c[2]={0,1};
		__int64 yy=m;
		yy=2*yy-1;
		int mat[2][2]={{0,1},{1,1}};
		int i,j,k;
		while(yy)
		{
			while(yy%2==0)
			{
				yy/=2;
				int temp[2][2];
				for(i=0;i<2;i++)
					for(j=0;j<2;j++)
					{
						temp[i][j]=0;
						for(k=0;k<2;k++)
							temp[i][j]=(temp[i][j]+mat[i][k]*mat[k][j])%inf;
					}
				for(i=0;i<2;i++)
					for(j=0;j<2;j++)
						mat[i][j]=temp[i][j];
			}
			int temp[2];
			for(i=0;i<2;i++)
			{
				temp[i]=0;
				for(j=0;j<2;j++)
					temp[i]=(temp[i]+c[j]*mat[j][i])%inf;
			}
			c[0]=temp[0];
			c[1]=temp[1];
			yy--;
		}
		int res=(c[0]*b+c[1]*a+999)%1000;
		printf("Case #%d: %03d\n",g++,res);
	}
}