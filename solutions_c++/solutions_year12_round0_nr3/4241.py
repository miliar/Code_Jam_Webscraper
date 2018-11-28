#include <stdio.h>

FILE *fin=fopen("c.in","r"),
	*fout=fopen("c.out","w");

bool yes[1010][1010];

int main()
{
	int i,j;
	int a1,a2,a3,b1,b2,b3;
	for (i=1; i<=1000; ++i)
		for (j=1; j<=1000; ++j)
			yes[i][j]=false;
	for (i=1; i<=9; ++i)
		yes[i][i]=true;
	for (i=10; i<=99; ++i)
		for (j=10; j<=99; ++j)
			if (i==j)
				yes[i][j]=true;
			else {
				if ((i%10==j/10)&&(i/10==j%10))
					yes[i][j]=true;
			}
	for (i=100; i<=999; ++i)
		for (j=100; j<=999; ++j)
			if (i==j)
				yes[i][j]=true;
			else {
				a1=i%10;
				a2=(i/10)%10;
				a3=i/100;
				b1=j%10;
				b2=(j/10)%10;
				b3=j/100;
				if ((a1==b3)&&(a2==b1)&&(a3==b2))
					yes[i][j]=true;
				else if ((a1==b2)&&(a2==b3)&&(a3==b1))
					yes[i][j]=true;
			}
	yes[1000][1000]=true;
	int t;
	fscanf(fin,"%d",&t);
	for (i=1; i<=t; ++i)
	{
		int result=0;
		int x,y,a,b;
		fscanf(fin,"%d%d",&x,&y);
		for (a=x; a<=y; ++a)
			for (b=a+1; b<=y; ++b)
				if (yes[a][b])
					++result;
		fprintf(fout,"Case #%d: %d\n",i,result);
	}
	return 0;
}