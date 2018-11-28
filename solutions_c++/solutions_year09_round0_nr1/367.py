//Alien Language

#include<iostream>
using namespace std;

const int MAXL = 16;
const int MAXD = 5005;
const int MAXN = 500;

struct DictNode
{
	int link[26];
}dn[MAXL*MAXD];
int ptr;

int d, l, n;
char word[10000];
char ans[30];
int len;

void BuildTree(int w, int pos)
{
	if(pos == l-1)return;
	int ww = word[pos+1] - 'a';
	if(dn[w].link[ww] == -1)
	{
		dn[w].link[ww] = ptr;
		memset(dn[ptr].link, -1, sizeof(dn[ptr].link));
		++ptr;
	}
	BuildTree(dn[w].link[ww], pos+1);
}



void Init()
{
	int i;
	ptr = 27;
	for(i=1; i<=26; ++i)memset(dn[i].link, -1, sizeof(dn[i].link));
	for(i=0; i<d; ++i)
	{
		scanf("%s", &word);
		BuildTree(word[0]-'a'+1, 0);
	}
}

int dfs(int pos, int now, int cnt)
{
	if(cnt == l)return 1;
	if(pos >= len)return 0;
	int e, i, ans = 0, m = 0;
	if(word[pos] == '(')
	{
		m = 1;
		++pos;
		for(e=pos; word[e]!=')'; ++e);
	}
	else e = pos + 1;
	for(i=pos; i<e; ++i)
	{
		if(dn[now].link[word[i]-'a'] == -1)continue;
		ans += dfs(e+m, dn[now].link[word[i]-'a'], cnt+1);
	}
	return ans;
}

void Solve()
{
	int i;
	for(i=1; i<=n; ++i)
	{
		scanf("%s", &word);
		len = strlen(word);
//		for(j=9; j<len; ++j)word[j] -= 'a';
		printf("Case #%d: %d\n", i, dfs(0, 0, 0));
	}
}

int main()
{
	for(int i=0; i<26; ++i)dn[0].link[i] = i+1;
	scanf("%d%d%d", &l, &d, &n);
	Init();
	Solve();
	return 0;
}
