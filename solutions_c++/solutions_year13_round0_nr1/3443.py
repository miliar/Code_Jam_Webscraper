#include <stdio.h>

int main()
{
	int tc,i,j,x,o,t,ctr,menang,zz;
	char arr[5][5];
	scanf("%d",&tc);
	for(ctr=1;ctr<=tc;ctr++)
	{
		menang = zz = 0;
		for(i=0;i<4;i++)
		{
			getchar();
			for(j=0;j<4;j++)
			{
				scanf("%c",&arr[i][j]);
			}
		}
		getchar();
		
		for(i=0;i<4;i++)
		{
			x=o=t=0;
			for(j=0;j<4;j++)
			{
				if(arr[i][j]=='X')x++;
				else if(arr[i][j]=='O')o++;
				else if(arr[i][j]=='T')t++;
				else zz=1;
			}
			if(x+t==4)
			{
				printf("Case #%d: X won\n",ctr);
				menang=1;
				break;
			}
			else if(o+t==4)
			{
				printf("Case #%d: O won\n",ctr);
				menang=1;
				break;
			}
		}
		
		if(menang)
		{
			continue;
		}
		
		for(i=0;i<4;i++)
		{
			x=o=t=0;
			for(j=0;j<4;j++)
			{
				if(arr[j][i]=='X')x++;
				else if(arr[j][i]=='O')o++;
				else if(arr[j][i]=='T')t++;
			}
			if(x+t==4)
			{
				printf("Case #%d: X won\n",ctr);
				menang=1;
				break;
			}
			else if(o+t==4)
			{
				printf("Case #%d: O won\n",ctr);
				menang=1;
				break;
			}
		}
		
		if(menang)
		{
			continue;
		}
		
			x=o=t=0;
			for(j=0;j<4;j++)
			{
				if(arr[j][j]=='X')x++;
				else if(arr[j][j]=='O')o++;
				else if(arr[j][j]=='T')t++;
			}
			if(x+t==4)
			{
				printf("Case #%d: X won\n",ctr);
				menang=1;
			}
			else if(o+t==4)
			{
				printf("Case #%d: O won\n",ctr);
				menang=1;
			}
		if(menang)
		{
			continue;
		}
		
		x=o=t=0;
			for(j=0;j<4;j++)
			{
				if(arr[j][3-j]=='X')x++;
				else if(arr[j][3-j]=='O')o++;
				else if(arr[j][3-j]=='T')t++;
			}
			if(x+t==4)
			{
				printf("Case #%d: X won\n",ctr);
				menang=1;
			}
			else if(o+t==4)
			{
				printf("Case #%d: O won\n",ctr);
				menang=1;
			}
		if(menang)
		{
			continue;
		}
		
		if(zz)
		{
			printf("Case #%d: Game has not completed\n",ctr);
		}
		else
		{
			printf("Case #%d: Draw\n",ctr);
		}
		
	}

return 0;
}

