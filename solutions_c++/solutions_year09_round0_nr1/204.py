#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int maxn = 20 * 5000;
struct snode
{
	int next[26];
	bool term;
	snode() { memset(next, -1, sizeof(next)); term = false; }
};

snode trie[maxn];
int triesz;
void trieInit()
{
	triesz = 1;
	trie[0] = snode();
}

void trieAdd(string s)
{
	int cur = 0;
	for(int i = 0; i < s.length(); ++i)
	{
		int ch = s[i] - 'a';
		if(trie[cur].next[ch] == -1)
			trie[cur].next[ch] = triesz,
			trie[triesz] = snode(),
			triesz++;
		cur = trie[cur].next[ch];
	}
	trie[cur].term = true;
}

int trieCount(string &s, int p = 0, int u = 0)
{
	if(trie[u].term) return 1;
	
	
	if(s[p] == '(')
	{
		int res = 0;
		int next = p + 1;
		while(s[next] != ')') next++; 
		for(int i = p + 1; i < next; ++i)
		{
			int ch = s[i] - 'a';
			if(trie[u].next[ch] != -1)
				res += trieCount(s, next + 1, trie[u].next[ch]);
		}
		if(res < 0)
		{
			cerr << "O_0" << endl;
		}
		return res;
	} else
		if(trie[u].next[s[p] - 'a'] != -1)
			return trieCount(s, p + 1, trie[u].next[s[p] - 'a']);
		else
			return 0;
}

int main()
{
	freopen("input.txt", "r", stdin); 
	freopen("output.txt", "w", stdout);
	int L, D, N;
	scanf("%d%d%d\n", &L, &D, &N);
	trieInit();
	for(int i = 0; i < D; ++i)
	{
		string s; getline(cin, s);
		trieAdd(s);
	}
	for(int i = 1; i <= N; ++i)
	{
		string s; getline(cin, s);
		int ans = trieCount(s);
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}