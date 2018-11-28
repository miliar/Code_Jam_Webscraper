#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>

const char sza[4][50]={"X won","O won","Draw","Game has not completed"};

inline int sgn(char a[4][5],int i,int j)
{
	char c;
	if(i<4)
		c=a[i][j];
	else if(i<8)
		c=a[j][7-i];
	else if(i==8)
		c=a[j][j];
	else
		c=a[j][3-j];
	switch(c)
	{
		case 'X':
			return 1;
		case 'T':
			return 0;
		case 'O':
			return -1;
		case '.':
			return 0105;
	}
}
int main()
{
	int tt,T;
	scanf("%d",&T);
	for(tt=1;tt<=T;tt++)
	{
		int ans=2;
		char a[4][5];
		int i,j;
		for(i=0;i<4;i++)
		{
			scanf("%s",a[i]);
		}
		for(i=0;i<10;i++)
		{
			int p=0;
			for(j=0;j<4;j++)
			{
				p+=sgn(a,i,j);
			}
			if(p<=-3)
				ans=1;
			else if(p<=2){}
			else if(p<=4)
				ans=0;
			else if(ans==2)
				ans++;
		}
	
		printf("Case #%d: %s\n",tt,sza[ans]);
	}
	return 0;
}
