#include<cstdio>
#include<cstring>
#include<queue>
using namespace std;
struct trietype
{
	trietype *c[26];
	int no;
} trie[80000];

int total,l,d,n;
queue<int> q,next;
bool can[26];
int check[5000];
char str[10000];
bool reach[80000];
void cal(int &i)
{
	if (str[i] == '(')
	{
		++i;
		while (str[i] != ')')
			can[str[i++] - 'a'] = true;
	} else can[str[i] -'a'] = true;
	++i;
}

int solve()
{
	memset(reach, false, sizeof(reach));
	q.push(0); reach[0] = true;
	int posi = 0;
	while (str[posi])
	{
		memset( can , false, sizeof(can) );
		cal(posi);
		while (!q.empty())
		{
			int now = q.front();
			q.pop();
			for (int i = 0 ; i < 26; ++i)
				if (can[i] && trie[now].c[i] && !reach[trie[now].c[i] -> no])
				{
					reach[trie[now].c[i] -> no] = true;
					next.push(trie[now].c[i] -> no);
				}
		}
		while (!next.empty())
		{
			q.push(next.front()); next.pop();
		}
	}
	int ans = 0;
	for (int i = 0; i < d; ++i)
		if (reach[check[i]]) ++ans;
	return ans;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	scanf("%d%d%d", &l , &d, &n);
	total = 1;
	for (int i = 0; i < d; ++i)
	{
		scanf("%s" ,str);
		trietype * now = trie;
		for (int j = 0; str[j]; ++j)
		{
			if (!now -> c[str[j] - 'a'])
			{
				now -> c[str[j] - 'a'] = trie + total;
				trie[total].no = total;
				++total;
			}
			now = now -> c[str[j] - 'a'];
		}
		check[i] = now -> no;
	}
	for (int cases = 1; cases <= n; ++cases)
	{
		scanf("%s" ,str);
		printf("Case #%d: %d\n" , cases , solve());		
	}
}
