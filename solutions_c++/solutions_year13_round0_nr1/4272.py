#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char mp[4][5];

bool check(char ch)
{
	bool flag;
	for (int i = 0; i < 4; i++)
	{
		flag = true;
		for (int j = 0; j < 4; j++)
			if (mp[i][j] != ch && mp[i][j] != 'T')
				flag = false;
		if (flag)	return true;
		
		flag = true;
		for (int j = 0; j < 4; j++)
			if (mp[j][i] != ch && mp[j][i] != 'T')
				flag = false;
		if (flag)	return true;
	}

	flag = true;
	for (int i = 0; i < 4; i++)
		if (mp[i][i] != ch && mp[i][i] != 'T')
			flag = false;
	if (flag)	return true;

	flag = true;
	for (int i = 0; i < 4; i++)
		if (mp[i][3 - i] != ch && mp[i][3 - i] != 'T')
			flag = false;
	if (flag)	return true;

	return false;
}

int main()
{
	int totCas;
	scanf("%d", &totCas);
	for (int cas = 1; cas <= totCas; cas++)
	{
		int cnt = 0;
		for (int i = 0; i < 4; i++)
		{
			scanf("%s", mp[i]);
			for (int j = 0; j < 4; j++)
				if (mp[i][j] != '.')
					cnt++;
		}
		printf("Case #%d: ", cas);
		if (check('X'))
			puts("X won");
		else if (check('O'))
			puts("O won");
		else if (cnt == 16)
			puts("Draw");
		else
			puts("Game has not completed");
	}
	return 0;
}

