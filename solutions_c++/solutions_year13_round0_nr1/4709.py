#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <map>
#include <set>
#include <sstream>

using namespace std;

char a[5][5];

int cal(char a,char b)
{
	if (a==b || a=='T') return 1;
	return 0;
}

void check()
{
	int t3=0;
	for (int i=0;i<4;++i)
	{
		int t1=0,t2=0;
		for (int j=0;j<4;++j)
			if (a[i][j]=='X') t1++;
			else if (a[i][j]=='O') t2++;
			else if (a[i][j]=='T') t1++,t2++;
			else if (a[i][j]=='.') t3++;
		if (t1==4)
		{
			printf("X won\n");
			return;
		}
		if (t2==4)
		{
			printf("O won\n");
			return;
		}
		t1=0,t2=0;
		for (int j=0;j<4;++j)
			if (a[j][i]=='X') t1++;
			else if (a[j][i]=='O') t2++;
			else if (a[j][i]=='T') t1++,t2++;
		if (t1==4)
		{
			printf("X won\n");
			return;
		}
		if (t2==4)
		{
			printf("O won\n");
			return;
		}
	}
	if (cal(a[0][0],'X')+cal(a[1][1],'X')+cal(a[2][2],'X')+cal(a[3][3],'X')==4)
	{
		printf("X won\n");
		return;
	}
	if (cal(a[1][1],'O')+cal(a[2][2],'O')+cal(a[3][3],'O')+cal(a[0][0],'O')==4)
	{
		printf("O won\n");
		return;
	}if (cal(a[0][3],'X')+cal(a[1][2],'X')+cal(a[2][1],'X')+cal(a[3][0],'X')==4)
	{
		printf("X won\n");
		return;
	}
	if (cal(a[0][3],'O')+cal(a[1][2],'O')+cal(a[2][1],'O')+cal(a[3][0],'O')==4)
	{
		printf("O won\n");
		return;
	}
	if (t3!=0)
	{
		printf("Game has not completed\n");
		return;
	}
	printf("Draw\n");
}

int main()
{
	#ifdef LOCAL_TEST
		freopen("c.in","r",stdin);
		freopen("c.out","w",stdout);
	#endif
	int task;
	scanf("%d ",&task);
	for (int tt=1;tt<=task;++tt)
	{
		printf("Case #%d: ",tt);
		for (int i=0;i<4;++i)
			for (int j=0;j<4;++j) scanf("%c ",&a[i][j]);
		check();
	}
	return 0;
}
