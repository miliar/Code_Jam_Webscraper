#include<iostream>

using namespace std;

int T;
char ch;
int a[10][10];
int tmp[20];
bool kk,aa;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		for(int j=1;j<=4;j++)
		{
			for(int k=1;k<=4;k++)
			{
				scanf("%c",&ch);
				while(ch!='.' && ch!='X' && ch!='O' && ch!='T') scanf("%c",&ch);
				switch(ch)
				{
					case '.':a[j][k]=1000;break;
					case 'X':a[j][k]=1;break;
					case 'O':a[j][k]=10;break;
					case 'T':a[j][k]=100;break;
				};
			}
		}
		tmp[1]=a[1][1]+a[1][2]+a[1][3]+a[1][4];
		tmp[2]=a[2][1]+a[2][2]+a[2][3]+a[2][4];
		tmp[3]=a[3][1]+a[3][2]+a[3][3]+a[3][4];
		tmp[4]=a[4][1]+a[4][2]+a[4][3]+a[4][4];
		tmp[5]=a[1][1]+a[2][1]+a[3][1]+a[4][1];
		tmp[6]=a[1][2]+a[2][2]+a[3][2]+a[4][2];
		tmp[7]=a[1][3]+a[2][3]+a[3][3]+a[4][3];
		tmp[8]=a[1][4]+a[2][4]+a[3][4]+a[4][4];		
		tmp[9]=a[1][1]+a[2][2]+a[3][3]+a[4][4];
		tmp[10]=a[4][1]+a[2][3]+a[3][2]+a[1][4];
		kk=0;aa=0;
		printf("Case #%d: ",i);
		for(int j=1;j<=10;j++)
		{
			if(tmp[j]==4 || tmp[j]==103)
			{
				printf("X won\n");aa=1;break;
			}
			if(tmp[j]==40 || tmp[j]==130)
			{
				printf("O won\n");aa=1;break;
			}
			if(tmp[j]>1000) kk=1;
		}
		if(!aa)
		{
			if(kk)
			{
				printf("Game has not completed\n");
			}
			else
			{
				printf("Draw\n");
			}
		}
	}
	return 0;
}
