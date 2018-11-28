#include<stdio.h>
#include<string.h>
char c[5][5];
int main()
{
	//freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
	int i,j,T,f,cnt;
	while(scanf("%d",&T)!=EOF)
	{
		cnt=0;
		while(T--)
		{
			cnt++;
			f=0;
			for(i=0;i<4;i++)
			{
				scanf("\n%s",c[i]);
			}
			for(i=0;i<4;i++)
			{
				if((c[i][0]=='X'||c[i][0]=='T')&&(c[i][1]=='X'||c[i][1]=='T')&&(c[i][2]=='X'||c[i][2]=='T')&&(c[i][3]=='X'||c[i][3]=='T'))
				{
					f=1;
					goto loop;
				}
				if((c[i][0]=='O'||c[i][0]=='T')&&(c[i][1]=='O'||c[i][1]=='T')&&(c[i][2]=='O'||c[i][2]=='T')&&(c[i][3]=='O'||c[i][3]=='T'))
				{
					f=2;
					goto loop;
				}
			}
			for(i=0;i<4;i++)
			{
				if((c[0][i]=='X'||c[0][i]=='T')&&(c[1][i]=='X'||c[1][i]=='T')&&(c[2][i]=='X'||c[2][i]=='T')&&(c[3][i]=='X'||c[3][i]=='T'))
				{
					f=1;
					goto loop;
				}
				if((c[0][i]=='O'||c[0][i]=='T')&&(c[1][i]=='O'||c[1][i]=='T')&&(c[2][i]=='O'||c[2][i]=='T')&&(c[3][i]=='O'||c[3][i]=='T'))
				{
					f=2;
					goto loop;
				}
			}
			if(f==0)
			{
				if((c[0][0]=='X'||c[0][0]=='T')&&(c[1][1]=='X'||c[1][1]=='T')&&(c[2][2]=='X'||c[2][2]=='T')&&(c[3][3]=='X'||c[3][3]=='T'))
				{
					f=1;
					goto loop;
				}
				if((c[0][3]=='X'||c[0][3]=='T')&&(c[1][2]=='X'||c[1][2]=='T')&&(c[2][1]=='X'||c[2][1]=='T')&&(c[3][0]=='X'||c[3][0]=='T'))
				{
					f=1;
					goto loop;
				}
				if((c[0][0]=='O'||c[0][0]=='T')&&(c[1][1]=='O'||c[1][1]=='T')&&(c[2][2]=='O'||c[2][2]=='T')&&(c[3][3]=='O'||c[3][3]=='T'))
				{
					f=2;
					goto loop;
				}
				if((c[0][3]=='O'||c[0][3]=='T')&&(c[1][2]=='O'||c[1][2]=='T')&&(c[2][1]=='O'||c[2][1]=='T')&&(c[3][0]=='O'||c[3][0]=='T'))
				{
					f=2;
					goto loop;
				}
				for(i=0;i<4;i++)
				{
					for(j=0;j<4;j++)
					{
						if(c[i][j]=='.')
						{
							f=4;
							goto loop;
						}
					}
				}
				if(f==0) f=3;
			}
			loop:if(f==1) printf("Case #%d: X won\n",cnt);
			else if(f==2) printf("Case #%d: O won\n",cnt);
			else if(f==3) printf("Case #%d: Draw\n",cnt);
			else printf("Case #%d: Game has not completed\n",cnt);
		}
	}
	return 0;
} 
