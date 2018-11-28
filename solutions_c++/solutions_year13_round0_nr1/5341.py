#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main()
{
	int t,x=0,o=0;
	int i,j,k;
	char arr[4][4];
	
	freopen("ain.in","r",stdin);
	freopen("aout.txt","w",stdout);
	
	scanf("%d",&t);
	
	for(k=1;k<=t;k++)
	{
		fgetc(stdin);
		int complete=1;
		x=o=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)	
			{
				scanf("%c",&arr[i][j]);
			}
			fgetc(stdin);
		}

		//row check
		for(i=0;i<4;i++)
		{
			x=o=0;
			for(j=0;j<4;j++)
			{
				if(arr[i][j]=='.')
					complete=0;
				if(arr[i][j] != 'O' && arr[i][j] != '.')
				{
					x++;
				}
				if(arr[i][j] != 'X' && arr[i][j] != '.')
				{
					o++;
				}
			}
			if(x==4 || o==4)
				break;
		}
		if(x==4)
		{
			printf("Case #%d: X won\n",k);
			continue;
		}
		else if(o==4)
		{
			printf("Case #%d: O won\n",k);
			continue;
		}
		//column check
		for(i=0;i<4;i++)
		{
			x=o=0;
			for(j=0;j<4;j++)
			{
				if(arr[j][i]=='.')
					complete=0;
				if(arr[j][i] != 'O' && arr[j][i] != '.')
				{
					x++;
				}
				if(arr[j][i] != 'X' && arr[j][i] != '.')
				{
					o++;
				}
			}
			if(x==4 || o==4)
				break;
		}
		if(x==4)
		{
			printf("Case #%d: X won\n",k);
			continue;
		}
		else if(o==4)
		{
			printf("Case #%d: O won\n",k);
			continue;
		}

		//diagonal check
		x=o=0;
		for(i=0;i<4;i++)
		{	
			if(arr[i][i]=='.')
				complete=0;
			if(arr[i][i] != 'O' && arr[i][i] != '.')
			{
				x++;
			}
			if(arr[i][i] != 'X' && arr[i][i] != '.')
			{
				o++;
			}			
		}
		if(x==4)
		{
			printf("Case #%d: X won\n",k);
			continue;
		}
		else if(o==4)
		{
			printf("Case #%d: O won\n",k);
			continue;
		}

		x=o=0;
		for(i=0;i<4;i++)
		{	
			if(arr[i][3-i]=='.')
				complete=0;
			if(arr[i][3-i] != 'O' && arr[i][3-i] != '.')
			{
				x++;
			}
			if(arr[i][3-i] != 'X' && arr[i][3-i] != '.')
			{
				o++;
			}
		}
		if(x==4)
		{
			printf("Case #%d: X won\n",k);
			continue;
		}
		else if(o==4)
		{
			printf("Case #%d: O won\n",k);
			continue;
		}
		else if(!complete)
		{
			printf("Case #%d: Game has not completed\n",k);
		}
		else
		{
			printf("Case #%d: Draw\n",k);
		}
	}
	return 0;
}