// qa.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include "cstdio"
#include "cstring"
#include "algorithm"
using namespace std;

const int maxBranch = 26;
const int MAXN = 500001;

struct TrieNode
{
	TrieNode *link[maxBranch];
	int v;

	TrieNode()
	{
		v = MAXN;
		for (int i = 0; i < maxBranch; i++)
			link[i] = NULL;
	}

	~TrieNode()
	{
		for (int i = 0; i < maxBranch; i++)
			if (link[i] != NULL)
			{
				delete link[i];
				link[i] = NULL;
			}
	}
};

TrieNode root;

int insert(char *word,int t)
{
	TrieNode *cur = &root;
	int i = 0,re;

	while (word[i] != '\0')
	{
		if (cur->link[word[i] - 'a'] == NULL)
			cur->link[word[i] - 'a'] = new TrieNode;

		cur = cur->link[word[i] - 'a'];
		i++;
	}
	re = cur->v;
	if (re == MAXN) cur->v = t;

	return re;
}

char dict[5001][20];
char letter[1000],word[1000];
bool f[5001];
int len;
int ans;
int l,d,n;
int beg[20];
int end[20];

void solve(TrieNode *p,int t)
{
	TrieNode * q = p;

	if (t == l)
	{
		f[p->v] = true;
		return;
	}
	
	for (int i = beg[t]; i <= end[t]; i++)
	{
		if (p->link[letter[i] - 'a'] != NULL)
		{
			solve(p->link[letter[i] - 'a'],t+1);
		}
	}
}

int main()
{
	freopen("e:\\A-large.txt","r",stdin);
	freopen("e:\\a.txt","w",stdout);

	scanf("%d%d%d",&l,&d,&n);
	for (int i = 0; i < d; i++)
	{
		scanf("%s",dict[i]);
		insert(dict[i],i);		
	}

	for (int z = 1; z <= n; z++)
	{
		for (int i = 0; i < 5001; i++)
			f[i] = false;
		ans = 0;

		scanf("%s",letter);
		len = strlen(letter);

		bool h = letter[0] == '(' ? true : false;
		for (int i = 0,j = 0; i < len; i++)
		{
			if (letter[i] == '(')
				beg[j] = i + 1;
			else if (letter[i] == ')')
			{
				end[j] = i - 1;
				h = letter[i+1] == '(' ? true : false;
				j++;
			}
			else
			{
				if (h == false)
				{
					beg[j] = end[j] = i;
					h = letter[i+1] == '(' ? true : false;
					j++;
				}
			}
		}

		solve(&root,0);

		for (int i = 0; i < d; i++)
			ans = f[i] == true ? ans + 1 : ans;
		printf("Case #%d: %d\n",z,ans);
	}

	return 0;
}

/*

bool find()
{
int l = 0,h = d,mid;
int ret;

while (l <= h)
{
mid = (l + h) >> 1;
ret = strcmp(word,dict[mid].ch);

if (ret == 0)
{
f[mid] = true;
return true;
}
else if (ret < 0)
h = mid - 1;
else
l = mid + 1;
}
return false;
}

void solve(int t)
{
if (t == l)
{
word[l] = '\0';
find();
return;
}

for (int i = beg[t]; i <= end[t]; i++)
{
word[t] = letter[i];
solve(t+1);
}
}
*/