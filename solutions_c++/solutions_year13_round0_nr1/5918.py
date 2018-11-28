#include <stdio.h>
char ha[10][10];

int main()
{
	int i,j,t,ii,f1,f2,f3;
	freopen("D:\\11.in","r",stdin);
	freopen("D:\\out.out","w",stdout);
	scanf("%d",&t);
	ii=1;
	while (t--)
	{
		for (i=0;i<4;i++)
			scanf("%s",ha[i]);
		
		f1=f2=f3=0;
		for (i=0;i<4;i++)
		{
			f1=0;f2=0;
			for(j=0;j<4;j++)
			{
				if (ha[i][j]=='X')
				{f1++;f3++;}
				else if(ha[i][j]=='O')
				{f2++;f3++;}
				else if(ha[i][j]=='T')
				{
					f1++;
					f2++;
					f3++;

				}
			}
			if(f1==4||f2==4)break;
			f1=f2=0;
			for(j=0;j<4;j++)
			{
				if (ha[j][i]=='X')
				{f1++;}
				else if(ha[j][i]=='O')
				{f2++;}
				else if(ha[j][i]=='T')
				{
					f1++;
					f2++;
				}
			}
			if(f1==4||f2==4) break;
		}
		if(f1!=4&&f2!=4)
		{
			f1=f2=0;
			for (i=0;i<4;i++)
			{
				if (ha[i][i]=='X')
				{f1++;}
				else if(ha[i][i]=='O')
				{f2++;}
				else if(ha[i][i]=='T')
				{
					f1++;
					f2++;
				}
			}
		}
		if(f1!=4&&f2!=4)
		{
			f1=f2=0;
			for (i=0;i<4;i++)
			{
				if (ha[i][3-i]=='X')
				{f1++;}
				else if(ha[i][3-i]=='O')
				{f2++;}
				else if(ha[i][3-i]=='T')
				{
					f1++;
					f2++;
				}
			}
		}
		printf("Case #%d: ",ii++);
		if(f1==4)
			printf("X won\n");
		else if(f2==4)
			printf("O won\n");
		else if(f3==16)
			printf("Draw\n");
		else printf("Game has not completed\n");
		
	}
	return 0;
}