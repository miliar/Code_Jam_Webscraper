#include <stdio.h>
#include <conio.h>

char a[51][51];
int r,c;

int pl(int x, int y)
{
	bool ok=true;
	int xx=0,yy=0;

	if(x+2>r||y+2>c) return 1;
	else
	for(int ii=x;ii<x+2;ii++)
	{
		for(int iii=y;iii<y+2;iii++)
		{
			if(a[ii][iii]=='.') ok=false;
			else if(xx==0&&yy==0) a[ii][iii]='/';
			else if(xx==1&&yy==0) a[ii][iii]='\\';
			else if(xx==0&&yy==1) a[ii][iii]='\\';
			else if(xx==1&&yy==1) a[ii][iii]='/';

			yy++;
		}
		yy=0;
		xx++;
	}

	if(ok) return 0; else return 1;
}

int main()
 {
    freopen("input.txt","rt",stdin);
    freopen("output.txt","wt",stdout);
    
	int nn;
	scanf("%d",&nn);

	for(int ni=0;ni<nn;ni++)
{
	printf("Case #%d:\n",ni+1);
	scanf("%d %d",&r,&c);
	getchar();
	for(int i=0;i<r;i++)
	{
		gets(a[i]);
	}
	int t=0;
	bool good=true;
	for(int i=0;i<r;i++)
	{
		for(int ii=0;ii<c;ii++)
		{
			if(a[i][ii]=='#') t=pl(i,ii);
			if(t==1) {good=false; break;}
		}
		if(!good) break;
	}

	if(!good)
	printf("Impossible\n");
	else
	for(int i=0;i<r;i++)
	{
		for(int ii=0;ii<c;ii++)
			printf("%c",a[i][ii]);
		printf("\n");
	}
}
	return 0;
 }