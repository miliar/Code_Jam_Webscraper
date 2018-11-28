#include <cstdio>
#include <string>
#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <vector>
#include <ctime>
#include <iostream>
#include <sstream>
#define eps 1.0e-9
#define Lim 1000000
using namespace std;

int a[100][100];
char c[12][12],b[12][12];
int best;
int N,M;
void sub(int x,int y,int cou){
	if (y>N) { if (cou>best) best=cou; return ;}
	if (x>M) {sub(1,y+1,cou); return ; }
	if (b[x][y]=='.'&&b[x][y-1]!='y'&&b[x-1][y-1]!='y'&&b[x+1][y-1]!='y')
	{
	//	printf("%d %d\n",x,y);
		int i=x,cc=cou;
		while (b[i][y]=='.'&&b[i-1][y-1]!='y'&&b[i][y-1]!='y'&&b[i+1][y-1]!='y')
		{
			b[i][y]='y';
			i++;
			cc++;
		}
		if (cc>best) best=cc;
	//	printf("%d %d %d %d\n",i,y,cc,best);
		sub(i,y,cc);
		cc=i;
		i--;
		while (i>=x)
		{
			b[i][y]='.';
			i--;
		}
		sub(cc,y,cou);
		//b[x][y]='y';
		//sub(x+1,y,cou+1);
		//b[x][y]='.';
		//sub(x+1,y,cou);
	}
	else sub(x+1,y,cou);
}
int main()
{
	int test,TestN;
	int i,j,k,l;
//	int N,M;
	scanf("%d",&TestN);
	for (i=0;i<11;i++)
	{	b[i][0]='y';
		b[0][i]='y';
	}
	for (test=1;test<=TestN;test++)
	{
		scanf("%d %d\n",&M,&N);
		for (i=0;i<M;i++)
		scanf("%s",c[i]);
		for (i=0;i<M+2;i++)
		{
			for (j=0;j<N+2;j++)
			b[i][j]='o';
		}
		for (i=0;i<M;i++)
		{
			for (j=0;j<N;j++)
			b[i+1][j+1]=c[i][j];
		}
	/*	for (i=0;i<M+2;i++)
		{
			for (j=0;j<N+2;j++)
			printf("%c",b[i][j]);//=c[i][j];
			printf("\n");
		}
	*/	best=0;
		sub(1,1,0);
//		for (j=0;j<;j++)
//		memset(a,0,sizeof(a));
//		if (notfound)
//			printf("Case #%d: IMPOSSIBLE\n",test);
//		else
		printf("Case #%d: %d\n",test,best);
	//	break;
	//	fprintf(stderr,"%d\n",test);
	}
  	return 0;
}
