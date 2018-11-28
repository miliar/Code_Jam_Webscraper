#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
using namespace std;

bool isWin(char c);

char s[5][5];
bool isComplete = false, owin = false, xwin = false;
int xcnt, ocnt, tcnt;
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int cas;
	scanf("%d", &cas);
	for (int t=1; t<=cas; t++)
	{
		memset(s, 0, sizeof(s));
		for (int i=0; i<4; i++) scanf("%s", s[i]);
		xcnt = ocnt = tcnt = 0;
		for (int i=0; i<4; i++)
		{
			for (int j=0; j<4; j++)
			{
				if (s[i][j] == 'O') ocnt++;
				else if (s[i][j] == 'X') xcnt++;
				else if (s[i][j] == 'T') tcnt++;
			}
		}
		if (tcnt+ocnt+xcnt == 16) isComplete = true;
		else isComplete = false;
		owin = isWin('O');
		xwin = isWin('X');
		printf("Case #%d: ", t);
		if (owin) printf("O won\n");
		else if (xwin) printf("X won\n");
		else if (isComplete) printf("Draw\n");
		else printf("Game has not completed\n");
	}
	return 0;
}

bool isWin(char c)
{
	bool flag;
	for (int i=0; i<4; i++)
	{
		flag = true;
		for (int j=0; j<4; j++)
		{
			if (s[i][j]!=c && s[i][j]!='T')
			{
				flag = false;
				break;
			}
		}
		if (flag) return true;
		flag = true;
		for (int j=0; j<4; j++)
		{
			if (s[j][i]!=c && s[j][i]!='T')
			{
				flag = false;
				break;
			}
		}
		if (flag) return true;
	}
	flag = true;
	for (int i=0; i<4; i++)
	{
		if (s[i][i]!=c && s[i][i]!='T')
		{
			flag = false;
			break;
		}
	}
	if (flag) return true;
	flag = true;
	for (int i=0; i<4; i++)
	{
		if (s[i][3-i]!=c && s[i][3-i]!='T')
		{
			flag = false;
			break;
		}
	}
	if (flag) return true;
	return false;
}