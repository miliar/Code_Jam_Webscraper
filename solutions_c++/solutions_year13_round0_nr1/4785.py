/*
* Problem: 
* Author: Leo Yu
* Time: 
* State: 
* Memo: 
*/
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
inline int   read()
{
    int x = 0;  char ch = getchar(); bool positive = 1;
    for (; ch < '0' || ch > '9'; ch = getchar())  if (ch == '-')  positive = 0;
    for (; ch >= '0' && ch <= '9'; ch = getchar())    x = x * 10 + ch - '0';
    return positive ? x : -x;
}

char s[5][5];
bool check(char ch)
{
	int flag;
	for (int i = 0; i < 4; ++ i)
	{
		flag = 1;
		for (int j = 0; j < 4; ++ j)
			if (s[i][j] != ch && s[i][j] != 'T') flag = 0;
		if (flag) return 1;
		flag = 1;
		for (int j = 0; j < 4; ++ j)
			if (s[j][i] != ch && s[j][i] != 'T') flag = 0;
		if (flag) return 1;
	}
	flag = 1;
	for (int i = 0; i < 4; ++ i)
		if (s[i][i] != ch && s[i][i] != 'T') flag = 0;
	if (flag) return 1;
	flag = 1;
	for (int i = 0; i < 4; ++ i)
		if (s[i][3 - i] != ch && s[i][3 - i] != 'T') flag = 0;
	return flag;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	int T = read(), t = 0;
	while (T --)
	{
		printf("Case #%d: ", ++ t);
		for (int i = 0; i < 4; ++ i)	scanf("%s", s[i]);
		int	tot = 0;
		for (int i = 0; i < 4; ++ i)
			for (int j = 0; j < 4; ++ j)
				tot += s[i][j] == '.';
		if (check('X'))	puts("X won");
		else if (check('O'))	puts("O won");
		else if (tot)	puts("Game has not completed");
		else	puts("Draw");
	}
	return 0;
}
