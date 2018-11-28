#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

bool isWin(char a[4],char c)
{
	int i,j;int f=0;char q;
	for(i=0;i<4;i++)
	{
		if(a[i]!=c)
		{
			f++;
			q=a[i];
		}

	}
	if(f==0)
	return true;
	else if(f==1 && q=='T')
	return true;
	else return false;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out1_large.txt","w",stdout);
	char a[5][5],b[5][5],c[5],d[5];
	int i,j,k,r=1,t;bool flag1,flag2;
	scanf("%d",&t);
	while(t--)
	{
		flag1=false;flag2=false;
		for(i=0;i<4;++i)
		scanf("%s",a[i]);



		for(i=0;i<4;i++)
		{
			if(isWin(a[i],'X'))
			{
				printf("Case #%d: X won\n",r++);
				flag1=1;
				break;
			}
			else if(isWin(a[i],'O'))
			{
				printf("Case #%d: O won\n",r++);
				flag1=1;
				break;
			}
		}
		if(flag1)
		continue;

		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		b[j][i]=a[i][j];

		for(i=0;i<4;i++)
		{
			if(isWin(b[i],'X'))
			{
				printf("Case #%d: X won\n",r++);
				flag1=1;
				break;
			}
			else if(isWin(b[i],'O'))
			{
				printf("Case #%d: O won\n",r++);
				flag1=1;
				break;
			}
		}
		if(flag1)
		continue;

		for(i=0,j=3;i<4;i++)
		{
			c[i]=a[i][i];
			d[i]=a[j-i][i];
		}

		if(isWin(c,'X'))
			{
				printf("Case #%d: X won\n",r++);
				continue;
			}
		else if(isWin(c,'O'))
			{
				printf("Case #%d: O won\n",r++);
				continue;
			}


		if(isWin(d,'X'))
			{
				printf("Case #%d: X won\n",r++);
				continue;
			}
		else if(isWin(d,'O'))
			{
				printf("Case #%d: O won\n",r++);
				continue;
			}


		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[i][j]=='.')
				{
					flag2=1;
					break;
				}
			}
		}
		if(flag2)
		{
				printf("Case #%d: Game has not completed\n",r);
		}
		else
		{
			printf("Case #%d: Draw\n",r);
		}
		r++;
	}

	return 0;
}
