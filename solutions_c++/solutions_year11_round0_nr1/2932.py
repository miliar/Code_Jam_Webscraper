#include <stdafx.h>
#include <stdio.h>

const long maxn=205;

long amount[3];
long mas[3][maxn];
long answer,n,m,q,k,t;
char c1,c2;
long color[maxn];

void solve()
{
	long pur1,pur2;
	long now1=1;
	long now2=1;
	long process=1;

	if (amount[1]!=0)
		pur1=1;
	else pur1=-1;
	if (amount[2]!=0)
		pur2=1;
	else pur2=-1;

	answer=0;
	while(process<=amount[1]+amount[2])
	{
		bool pp=false;
		answer++;
		if (pur1!=-1)
		{
			if (now1==mas[1][pur1])
			{
				if (color[process]==1)
				{
					pp=true;
					pur1++;
					if (pur1>amount[1])
						pur1=-1;
					process++;
				}
			}
			else if (now1>mas[1][pur1])
				now1--;
			else now1++;
		}

		if (pur2!=-1)
		{
			if (now2==mas[2][pur2])
			{
				if ((color[process]==2)&&(pp==false))
				{
					pur2++;
					if (pur2>amount[2])
						pur2=-1;
					process++;
				}
			}
			else if (now2>mas[2][pur2])
				now2--;
			else now2++;
		}
	}
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%ld",&n);
	for (q=1;q<=n;q++)
	{
		scanf("%ld",&m);
		amount[1]=0;
		amount[2]=0;
		for (k=1;k<=m;k++)
		{
			scanf("%c%c%ld",&c2,&c1,&t);
			if (c1=='O')
			{
				amount[1]++;
				color[k]=1;
				mas[1][amount[1]]=t;
			}
			else
			{
				amount[2]++;
				color[k]=2;
				mas[2][amount[2]]=t;
			}
		}
		scanf("\n");

		solve();

		printf("Case #%ld: %ld\n",q,answer);
	}
}