#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

#pragma comment(linker,"/STACK:10000000")

using std :: vector;

const int D = 6000;
const int L = 30;

char word[D][L];

int l, d, n;

struct ElemTrie {
	int next[26];
};

struct Trie {
private:
	int cnt;
public:
	ElemTrie arr[D * L];
	int root;

	void build(char s[][L], int d)
	{
		cnt = 1;
		root = 0;
		memset(arr, 0, sizeof(arr));
		for (int i = 0; i < d; ++i)
			addWord(s[i]);
	}

	void addWord(char * s)
	{
		int i = root;
		int j = 0;
		while (s[j] && arr[i].next[s[j] - 'a'] != 0)
		{
			i = arr[i].next[s[j] - 'a'];
			++j;
		}

		while (s[j])
		{
			i = arr[i].next[s[j] - 'a'] = cnt++;
			++j;
		}
	}
};

Trie t;

int Brute(char * s, const Trie & t, int j)
{
	if (s[0] == 0)
		return 1;

	if (s[0] == '(')
	{
		int i = 1;
		vector <char> p;
		while (s[i] != ')')
		{
			p.push_back(s[i] - 'a');
			++i;
		}

		std :: sort(p.begin(), p.end());

		int res = 0;
		for (int ii = 0; ii < p.size(); ++ii)
			if ((ii == 0 || p[ii] != p[ii-1]) && t.arr[j].next[p[ii]] != 0)
				res += Brute(s + i + 1, t, t.arr[j].next[p[ii]]);
		 return res;
	}
	else
	{
		if (t.arr[j].next[s[0] - 'a'] != 0)
			return Brute(s + 1, t, t.arr[j].next[s[0] - 'a']);
		return 0;
	}
}

int Solve(char * s)
{
	return Brute(s, t, 0);
}

char s[L * 1000];

int main()
{
	scanf("%d%d%d\n", &l, &d, &n);
	for (int i = 0; i < d; ++i)
		gets(word[i]);

	t.build(word, d);

	for (int i = 0; i < n; ++i)
	{
		gets(s);
		printf("Case #%d: %d\n", i+1, Solve(s));
	}

	return 0;
}