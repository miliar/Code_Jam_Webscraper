#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int t,tt,u1,u2,d1,d2;
char ch[10][10];
int ux[5],uy[5],dx[5],dy[5];
bool bj,bb;

void work()
{
	memset(ux,0,sizeof(ux));
	memset(uy,0,sizeof(uy));
	memset(dx,0,sizeof(dx));
	memset(dy,0,sizeof(dy));
	u1=u2=d1=d2=0;
	
	bj=false;
	for (int i=0;i<4;++i) 
		for (int j=0;j<4;++j) 
			{
				cin >>ch[i][j];
				if (ch[i][j]=='.') bj=true;
			}
	
	for (int i=0;i<4;++i)
		for (int j=0;j<4;++j)
		{
			if (ch[i][j]=='X') ux[i]++;
			if (ch[i][j]=='O') uy[i]++;
			if (ch[i][j]=='T')
			{
				ux[i]++;
				uy[i]++;
			}
		}
		
	for (int j=0;j<4;++j)
		for (int i=0;i<4;++i)
		{
			if (ch[i][j]=='X') dx[j]++;
			if (ch[i][j]=='O') dy[j]++;
			if (ch[i][j]=='T')
			{
				dx[j]++;
				dy[j]++;
			}
		}
	
	for (int i=0;i<4;++i)
	{
		if (ch[i][i]=='X') u1++;
		if (ch[i][i]=='O') u2++;
		if (ch[i][i]=='T')
		{
			u1++;
			u2++;
		}
	}
	
	for (int i=0;i<4;++i)
	{
		if (ch[i][3-i]=='X') d1++;
		if (ch[i][3-i]=='O') d2++;
		if (ch[i][3-i]=='T')
		{
			d1++;
			d2++;
		}
	}
	
	printf("Case #%d: ",tt); 
	bb=(u1==4)|(d1==4);
	for (int i=0;i<4;++i) bb=bb|(ux[i]==4);
	for (int i=0;i<4;++i) bb=bb|(dx[i]==4);
	if (bb)
	{
		printf("X won\n");
		return;
	}
	
	bb=(u2==4)|(d2==4);
	for (int i=0;i<4;++i) bb=bb|(uy[i]==4);
	for (int i=0;i<4;++i) bb=bb|(dy[i]==4);
	if (bb)
	{
		printf("O won\n");
		return;
	}
	
	if (bj) printf("Game has not completed\n");
	else printf("Draw\n");
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);


	scanf("%d",&t);
	for (tt=1;tt<=t;++tt) 
	{
		work();
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
