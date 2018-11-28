#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;

int main(void)
{
	int  a[5][5];
	int x;
	int o;
	char b[5][5];
	int T;
	int i,j,k;
	scanf("%d",&T);
	for(i=1;i<=T;i++)
	{
		memset(a,0,sizeof(a));
		x = 0;
		o = 0;
		for(j=0;j<4;j++)
		{
			scanf("%s",b[j]);
			for(k=0;k<4;k++)
			{
				if(b[j][k]=='O')
					a[j][k] = 1;
				else if(b[j][k]=='X')
					a[j][k] = -1;
				else if(b[j][k]=='T')
					a[j][k] = 2;
			}
		}
		int tx,to;
		
		for(j=0;j<4;j++)
		{
			to = 0;
			for(k = 0;k<4;k++)
				if(a[j][k]==1||a[j][k]==2)
					to++;
			if(to==4)
				o= 1;
		}
		for(j=0;j<4;j++)
		{
			tx = 0;
			for(k = 0;k<4;k++)
				if(a[j][k]==-1||a[j][k]==2)
					tx++;
			if(tx==4)
				x= 1;
		}
		for(j=0;j<4;j++)
		{
			tx = 0;
			for(k = 0;k<4;k++)
				if(a[k][j]==-1||a[k][j]==2)
					tx++;
			if(tx==4)
				x= 1;
		}
		
		for(j=0;j<4;j++)
		{
			to = 0;
			for(k = 0;k<4;k++)
				if(a[k][j]==1||a[k][j]==2)
					to++;
			if(to==4)
				o = 1;
		}
		to = 0;
		for(j=0;j<4;j++)
			if(a[j][j]==1||a[j][j]==2)
				to++;
		if(to==4)
			o = 1;
		to = 0;
		for(j=0;j<4;j++)
			if(a[j][3-j]==1||a[j][3-j]==2)
				to++;
		if(to==4)
			o = 1;
		tx = 0;
		for(j=0;j<4;j++)
			if(a[j][j]==-1||a[j][j]==2)
				tx++;
		if(tx==4)
			x = 1;
		tx = 0;
		for(j=0;j<4;j++)
			if(a[j][3-j]==-1||a[j][3-j]==2)
				tx++;
		if(tx==4)
			x = 1;
		
		int notend = 0;
		for(j=0;j<4;j++)
			for(k=0;k<4;k++)
				if(b[j][k]=='.')
					notend = 1;
		if(x==1)
		{
			printf("Case #%d: X won\n",i);
		}
		else if(o==1)
		{
			printf("Case #%d: O won\n",i);
		}
		else if(notend==1)
		{
			printf("Case #%d: Game has not completed\n",i);
		}
		else
		{
			printf("Case #%d: Draw\n",i);
		}
			
	}
	
	
	return 0;
}
