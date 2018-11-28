#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

const int	maxN = 2000;
const int	maxL = 110;

unsigned int	ELF[maxN];
char		st[maxN][maxL];
int		idx[maxN], rank[maxN], S, Q;

bool	compareStr(int i, int j)
{
	if (ELF[i] > ELF[j]) return 1;
	if (ELF[i] < ELF[j]) return 0;
	return strcmp(st[i], st[j]) > 0;
}

unsigned int getELF(char *a)
{
	unsigned int ret = 0;
	unsigned int x = 0;
	while (*a)
	{
		ret = (ret << 4) + (*a++);
		if ((x = ret & 0xF0000000L) > 0)
		{
			ret ^= (x >> 24);
			ret &= ~x;
		}
	}
	return ret;
}

set<int> engSet, used;

int	main()
{
	int nCase;
	scanf("%d\n", &nCase);
	for (int nowCase = 1; nowCase <= nCase; ++nowCase)
	{
		scanf("%d\n", &S);
		for (int i = 0; i < S; ++i) gets(st[i]);
		scanf("%d\n", &Q);
		for (int i = S; i < S + Q; ++i) gets(st[i]);
		
		for (int i = 0; i < S + Q; ++i)
			ELF[i] = getELF(st[i]);

		for (int i = 0; i < S + Q; ++i) idx[i] = i;
		sort(idx, idx + S + Q, compareStr);
		
		rank[idx[0]] = 0;
		for (int i = 1; i < S + Q; ++i)
			rank[idx[i]] = rank[idx[i - 1]] + compareStr(idx[i - 1], idx[i]);

		engSet.clear(); used.clear();
		int answer = 0;
		for (int i = 0; i < S; ++i) engSet.insert(rank[i]);
		for (int i = S; i < S + Q; ++i) if (engSet.count(rank[i]))
		{
			used.insert(rank[i]);
			if (used.size() == S)
			{
				used.clear();
				used.insert(rank[i]);
				++answer;
			}
		}
		printf("Case #%d: %d\n", nowCase, answer);
	}
	return 0;
}
