#include<stdio.h>
char a[4][4];
bool draw;
void input()
{
	int i, j, k=0;
	for(i=0; i<4; i++)
		scanf("%s",a[i]);
	for(i=0;i<4; i++)
		for(j=0;j<4;j++)	
		{
			if(a[i][j]=='X')
				a[i][j]=1;
			else if(a[i][j]=='O')
				a[i][j] = 2;
			else if(a[i][j] == 'T')
				a[i][j] = 3;
			else{
				a[i][j] = 0;
				k++;
			}
		}
	if(k)
		draw = false;
	else
		draw = true;
}
void process()
{
	int i, j, k, l,o,p,q;
	k = l = 0;

	for(i=0; i<4; i++)
		for(j=0; j<4; j++)
		{
			p=q=0;
			for(o=0; i+o<4; o++)
			{
				if(a[o+i][j]&1)
					p++;
				if(a[o+i][j]&2)
					q++;
			}
			if(q!=4 && p == 4)
				k=1;
			if(p!=4 && q==4)
				l=1;
			p=q=0;
			for(o=0; j+o<4; o++)
			{
				if(a[i][j+o]&1)
					p++;
				if(a[i][j+o]&2)
					q++;
			}
			if(q!=4 && p == 4)
				k=1;
			if(p!=4 && q==4)
				l=1;
			p=q=0;
			for(o=0; j+o<4 && i-o>=0; o++)
			{
				if(a[i-o][j+o]&1)
					p++;
				if(a[i-o][j+o]&2)
					q++;
			}
			if(q!=4 && p == 4)
				k=1;
			if(p!=4 && q==4)
				l=1;
			
			p=q=0;
			for(o=0; j+o<4 && i+o<4; o++)
			{
				if(a[i+o][j+o]&1)
					p++;
				if(a[i+o][j+o]&2)
					q++;
			}
			if(q!=4 && p == 4)
				k=1;
			if(p!=4 && q==4)
				l=1;
		}
	if(k & l)
		printf("Draw");
	else if(k)
		printf("X won");
	else if(l)
		printf("O won");
	else
	{
		if(draw)printf("Draw");
		else printf("Game has not completed");
	}
	printf("\n");
}
void output()
{
}
int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("output.txt","wt",stdout);

	int t,v;
	scanf("%d",&t);
	for(v=1; v<=t; v++)
	{
		printf("Case #%d: ",v);
		input();
		process();
		output();
	}
}