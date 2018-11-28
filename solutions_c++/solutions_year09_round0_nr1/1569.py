#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
#define MAXNODE 100000
#define MAXCHILD 26

struct part
{
	int has;
	char tmp[50];
}p[1000];

int pn;
int cn=1,L,n,m;
int trie,mp[MAXNODE][MAXCHILD],danger[MAXNODE];
int node,ans,tn;
char s[1000],tmp[1000];

void insert(int t,char *s)
{
	if(*s == '\0') {danger[t] = 1;return;}
	int d = *s-'a';
	if(mp[t][d] == -1)
	{
		mp[t][d] = node++;
	}
	insert(mp[t][d],s+1);
}

bool find_in_trie(int t,char *s)
{
	while(*s)
	{
		int d = *s-'a';
		if(mp[t][d] == -1) return 0;
		t = mp[t][d];
		s++;
	}
	if(danger[t]) return 1;
	return 0;
}

bool check(int t,char *s)
{
	while(*s)
	{
		int d = *s-'a';
		if(mp[t][d] == -1) return 0;
		t = mp[t][d];
		s++;
	}
	return 1;
}

void dfs(int st,int get,int pa)
{
	tmp[get] = '\0';
	if(st!=0 && !check(trie,tmp)) return;
	if(get == L)
	{
		tmp[get] = '\0';
		if(find_in_trie(trie,tmp)) ans++;
		return;
	}
	int j;
	for(j=0;j<p[st].has;j++)
	{
		tmp[get] = p[st].tmp[j];
		dfs(st+1,get+1,pa);
	}
	return;
}

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-out.txt","w",stdout);
	int i,j,slen;
	scanf("%d%d%d",&L,&n,&m);
	memset(mp,-1,sizeof(mp));
	memset(danger,0,sizeof(danger));
	trie = 0;
	node = 1;
	for(i=0;i<n;i++)
	{
		scanf("%s",s);
		insert(trie,s);
	}
	while(m--)
	{
		scanf("%s",s);
		slen = strlen(s);
		pn = 0;
		int tt = 0;
		for(i=0;i<slen;i++)
		{
			if(s[i]=='(')
			{
				j = i+1;
				while(s[j]!=')')
				{
					p[pn].tmp[tt++] = s[j++];
				}
				i = j;
				p[pn].has = tt;
				pn++;
				tt = 0;
			}
			else if(s[i]>='a' && s[i]<='z')
			{
				p[pn].tmp[tt++] = s[i];
				p[pn].has = tt;
				pn++;
				tt = 0;
			}
		}
		//printf("part:%d\n",pn);
		if(pn > L || pn<L)
		{
			printf("Case #%d: 0\n",cn++);
			continue;
		}
		ans = 0;
		dfs(0,0,pn);
		printf("Case #%d: %d\n",cn++,ans);
	}
	return 0;
}

