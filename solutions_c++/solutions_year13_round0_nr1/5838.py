#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;

#define debug(x) cout << #x << "=" << x << endl
#define sqr(x) ((x)*(x))

int tests,cnt1,cnt2;
char s[4][5];

int all(char a1, char a2, char a3, char a4, char sign)
{
	if (a1==sign||a1=='T')
		if (a2==sign||a2=='T')
		if (a3==sign||a3=='T')
		if (a4==sign||a4=='T')
		return 1;
	return 0;
}

int check(char sign)
{
	for (int i=0;i<4;i++)
		if (all(s[i][0],s[i][1],s[i][2],s[i][3],sign))
			return 1;
	for (int j=0;j<4;j++)
		if (all(s[0][j],s[1][j],s[2][j],s[3][j],sign))
			return 1;
	if (all(s[0][0],s[1][1],s[2][2],s[3][3],sign))
		return 1;
	if (all(s[0][3],s[1][2],s[2][1],s[3][0],sign))
		return 1;
	return 0;
}

int main()
{
	freopen("a1.in","r",stdin);
	freopen("a1.out","w",stdout);
	
	scanf("%d",&tests);
	for (int test=1;test<=tests;test++)
	{
		for (int i=0;i<4;i++) scanf("%s",s[i]);
		cnt1 = cnt2 = 0;
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++)
				if (s[i][j]=='X')
					cnt1++;
				else if (s[i][j]=='O')
					cnt2++;
		printf("Case #%d: ",test);
		if (cnt1>cnt2)  // X
		{
			if (check('X'))
				printf("X won\n");
			else if (cnt1+cnt2+1<16)
				printf("Game has not completed\n");
			else printf("Draw\n");
		}
		if (cnt1==cnt2)  // O
		{
			if (check('O'))
				printf("O won\n");
			else if (cnt1+cnt2+1<16)
				printf("Game has not completed\n");
			else printf("Draw\n");
		}
	}
	
	return 0;
}
