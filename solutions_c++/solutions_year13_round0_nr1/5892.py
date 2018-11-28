#include <cstdio>

int main()
{
	int t,x;
	freopen("date.in","r",stdin);
	freopen("date.out","w",stdout);
	scanf("%d\n",&t);
	for (x=1;x<=t;++x)
	{
		char a[10][10];
		int i,j,win=0;
		for (i=1;i<5;++i)
			scanf("%s",&a[i]);
		
		for (i=1;i<5;++i)
		{
			for (j=0;j<4;++j)
				if (a[i][j]!='X' && a[i][j]!='T')
					break;
			if (j==4) 
				{win=1;break;}
		}
		if (!win)
		for (j=0;j<4;++j)
		{
			for (i=1;i<5;++i)
				if (a[i][j]!='X' && a[i][j]!='T')
					break;
			if (i==5)
			{win=1;break;}
		}
		if (!win)
		for (i=0;i<4;++i)
			if (a[i+1][i]!='X' && a[i+1][i]!='T')
				break;
		if (i==4)
			win=1; 
		
		if (!win)
		for (i=0;i<4;++i)
			if (a[4-i][i]!='X' && a[4-i][i]!='T')
				break;
		if (i==4)
			win=1; 	
		
		if (!win)
		for (i=1;i<5;++i)
		{
			for (j=0;j<4;++j)
				if (a[i][j]!='O' && a[i][j]!='T')
					break;
			if (j==4) 
				{win=2;break;}
		}
		if (!win)
		for (j=0;j<4;++j)
		{
			for (i=1;i<5;++i)
				if (a[i][j]!='O' && a[i][j]!='T')
					break;
			if (i==5)
			{win=2;break;}
		}
		if (!win)
		for (i=0;i<4;++i)
			if (a[i+1][i]!='O' && a[i+1][i]!='T')
				break;
		if (i==4)
			win=2; 	
		
		if (!win)
		for (i=0;i<4;++i)
			if (a[4-i][i]!='O' && a[4-i][i]!='T')
				break;
		if (i==4)
			win=2;	
		
		int nrp=0;
		if (!win)
			for (i=1;i<5;++i)
				for (j=0;j<4;++j)
					if (a[i][j]=='.')
						++nrp,j=5,i=6;
		
		if (win==1)
			printf("Case #%d: X won\n",x); else
				if (win==2)
					printf("Case #%d: O won\n",x); else
						if (nrp==0)
							printf("Case #%d: Draw\n",x); else
								printf("Case #%d: Game has not completed\n",x);
	
	}					
			
				
	return 0;
}