#include<stdio.h>
char m[8][8];
int a[4];//X,O,T,.
int main()
{
//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("output","w",stdout);
	int t,cnt;
	scanf("%d",&t);
	for(cnt=1;cnt<=t;cnt++)
	{
		int i,j;
		for(i=1;i<=4;i++)
			scanf("%s",&m[i][1]);
		int win=0,not_finish=0;
		for(i=1;i<=4;i++)
		{
			a[0]=a[1]=a[2]=a[3]=0;
			for(j=1;j<=4;j++)
			{
				if(m[i][j]=='X')
					a[0]++;
				else if(m[i][j]=='O')
					a[1]++;
				else if(m[i][j]=='T')
					a[2]++;
				else
				{
					a[3]++;
					not_finish=1;
				}
			}
			if(a[0]==4||a[0]==3&&a[2]==1)
				win=1;
			if(a[1]==4||a[1]==3&&a[2]==1)
				win=2;


			a[0]=a[1]=a[2]=a[3]=0;
			for(j=1;j<=4;j++)
			{
				if(m[j][i]=='X')
					a[0]++;
				else if(m[j][i]=='O')
					a[1]++;
				else if(m[j][i]=='T')
					a[2]++;
				else
				{
					a[3]++;
					not_finish=1;
				}
			}
			if(a[0]==4||a[0]==3&&a[2]==1)
				win=1;
			if(a[1]==4||a[1]==3&&a[2]==1)
				win=2;
		}
		a[0]=a[1]=a[2]=a[3]=0;
		for(i=1;i<=4;i++)
			if(m[i][i]=='X')
				a[0]++;
			else if(m[i][i]=='O')
				a[1]++;
			else if(m[i][i]=='T')
				a[2]++;
		if(a[0]==4||a[0]==3&&a[2]==1)
			win=1;
		if(a[1]==4||a[1]==3&&a[2]==1)
			win=2;
		a[0]=a[1]=a[2]=a[3]=0;
		for(i=1;i<=4;i++)
			if(m[i][5-i]=='X')
				a[0]++;
			else if(m[i][5-i]=='O')
				a[1]++;
			else if(m[i][5-i]=='T')
				a[2]++;
		if(a[0]==4||a[0]==3&&a[2]==1)
			win=1;
		if(a[1]==4||a[1]==3&&a[2]==1)
			win=2;
		if(win==1)
			printf("Case #%d: X won\n",cnt);
		else if(win==2)
			printf("Case #%d: O won\n",cnt);
		else if(not_finish)
			printf("Case #%d: Game has not completed\n",cnt);
		else
			printf("Case #%d: Draw\n",cnt);
	}
	return 0;
}