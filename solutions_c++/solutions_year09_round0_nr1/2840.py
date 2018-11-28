#include <stdio.h>
#include <string.h>

#include <iostream>
#include <vector>
using namespace std;

int	CAS = 0;
char		pattern[1000];
vector<char>		candid[15];

int		L, D, N;
char	words[5000][20];

void	parse(char *s)
{
	int	len = strlen(s);
	int	cL = 0;
	int	state = 1;		// 0 (..)  and 1 ()..

	for (int i=0; i<len; i++)
	{
		char	ch = s[i];
		if (ch != ')' && ch != '(')
		{
			candid[cL].push_back(ch);					
		}

		if (ch == ')')	state = 1;
		if (ch == '(')	state = 0;

		if (state)		cL++; 
	}
}


bool	match(int	W)
{
	for (int i=0; i<L; i++)
	{
		bool		find = false;
		for (int j=0; j<candid[i].size(); j++)
		{
			if (candid[i][j] == words[W][i])
			{
				find = true;
				break;
			}
		}

		if (!find)		return false;
	}
	return true;
}

int main()
{
	char	filepath[] = "D:/gcj/A-large.in";


	FILE*		fp = fopen("D:/gcj/alian_large.out", "w");
	freopen(filepath, "r", stdin);
	

	scanf("%d %d %d", &L, &D, &N);

	for (int i=0; i<D; i++)
	{
		scanf("%s", words[i]);
	}
	
	for (int i=0; i<N; i++)
	{
		for (int j=0; j<L; j++)
			candid[j].clear();

		scanf("%s", pattern);
		parse(pattern);

		int		ans = 0;
		for (int j=0; j<D; j++)
		{
			if (match(j))	ans++;
		}
		fprintf(fp, "Case #%d: %d\n", ++CAS, ans);
	}
	return 0;
}