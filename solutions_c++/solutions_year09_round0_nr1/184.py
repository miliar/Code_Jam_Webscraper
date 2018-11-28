#include <stdio.h>
struct trieNode
{
	int ind[26];
}trie[300000];
int L;
int trieN;
void insert(char word[], int cur, int dep)
{
	if (dep == L)
		return;
	int chr = word[dep] - 'a';
	if (trie[cur].ind[chr] != -1)
		insert(word, trie[cur].ind[chr], dep + 1);
	else
	{
		trie[cur].ind[chr] = trieN;
		for (int i = 0; i < 26; i++)
			trie[trieN].ind[i] = -1;
		trieN++;
		insert(word, trie[cur].ind[chr], dep + 1);
	}
}
char dword[16][30];
int dn;
int findAns(int cur, int dep)
{
	if (dep == L)
		return 1;
	int res = 0;
	for (int i = 0; i < 26; i++)
		if (trie[cur].ind[i] != -1 && dword[dep][i] == 1)
			res += findAns(trie[cur].ind[i], dep + 1);
	return res;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("a.txt", "w", stdout);
	int i, j, k;
	int D, N;
	scanf("%d%d%d", &L, &D, &N);
	trieN = 1;
	for (i = 0; i < 26; i++)
		trie[0].ind[i] = -1;
	char word[100];
	for (i = 0; i < D; i++)
	{
		scanf("%s", word);
		insert(word, 0, 0);
	}
	char in[1000];
	for (i = 0; i < N; i++)
	{
		scanf("%s", in);
		int cn = 0;
		dn = 0;
		for (j = 0; j < L; j++)
			for (k = 0; k < 26; k++)
				dword[j][k] = 0;
		for (j = 0; in[j];)
		{
			if (in[j] == '(')
			{
				j++;
				cn = 0;
				while (in[j] != ')')
				{
					dword[dn][in[j] - 'a'] = 1;
					j++;
					cn++;
				}
				j++;
				dn++;
			}
			else
			{
				dword[dn][in[j] - 'a'] = 1;
				j++;
				dn++;
			}
		}
		printf("Case #%d: %d\n", i + 1, findAns(0, 0));
	}
	return 0;
}
