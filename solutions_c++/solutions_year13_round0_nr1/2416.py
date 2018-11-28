#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <vector>

using namespace std;

typedef long long LL;

int t;
char s[10][10];

int solve()
{
	int i,j;
	int flag;
	char tem;
	flag = 0;
	for(i = 0; i < 4; i++)
		for(j = 0; j < 4; j++)
			if(s[i][j] == '.') flag = 1;
	for(i = 0; i < 4; i++)
	{
		j = 0;
		while(s[i][j] == 'T') j++;
		tem = s[i][j];
		for(j++; j < 4; j++)
		{
			if(s[i][j] == '.') break;
			if(!(s[i][j] == tem || s[i][j] == 'T')) break;
		}
		if(j == 4) return (tem == 'X') ? 1 : 2;
	}
	for(i = 0; i < 4; i++)
	{
		j = 0;
		while(s[j][i] == 'T')  j++;
		tem = s[j][i];
		for(j++; j < 4; j++)
		{
			if(s[i][j] == '.') break;
			if(!(s[j][i] == tem || s[j][i] == 'T')) break;
		}
		if(j == 4) return (tem == 'X') ? 1 : 2;
	}
	i = j = 0;
	while(s[i][j] == 'T') i++,j++;
	tem = s[i][j];
	for(; i < 4; i++,j++)
	{
		if(s[i][j]  == '.') break;
		if(!(s[i][j] == tem || s[i][j] == 'T')) break;
	}
	if(i == 4) return (tem == 'X') ? 1 : 2;
	i = 0;
	j = 3;
	while(s[i][j] == 'T')
	{
		i++;
		j--;
	}
	tem = s[i][j];
	for(; i < 4; i++,j--)
	{
		if(s[i][j] == '.') break;
		if(!(s[i][j] == tem || s[i][j] == 'T')) break;
	}
	if(i == 4) return (tem == 'X') ? 1 : 2;
	return flag ? 4 : 3;
}

int main()
{
//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("A-small-attempt0.out", "w", stdout);
	int i;
	int cnt;
	scanf("%d", &t);
	for(cnt = 1; cnt <= t; cnt++)
	{
		for(i = 0 ; i < 4; i++)
			scanf("%s", s[i]);
		i = solve();
		printf("Case #%d: ", cnt);
		if(i == 1) puts("X won");
		else if(i == 2) puts("O won");
		else if(i == 3) puts("Draw");
		else puts("Game has not completed");
	}
	return 0;
}