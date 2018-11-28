#include<stdio.h>
#include<memory.h>
#include<map>
#include<string>
using namespace std;
map < string , bool > M;
char need[1000], s[100];
int hash[1000000];
struct node
{
	int sun[2];
	char fea[13];
	double val;
}tree[600000];
double ans;
int n;
int id;
int all;
void build(int now)
{
	char ss[20],ch;
	while(true)
	{
		ch = getchar();
		if (ch == '(')
			break;
	}
	scanf("%lf", &tree[now].val);
	while(true)
	{
		ch = getchar();
		if (ch == ')')
		{
			tree[now].sun[0] = -1;
			return ;
		}
		else
		{
			if (ch >= 'a' && ch <= 'z')
			{
				ss[0] = ch;
				int len = 1;
				while(true)
				{
					ch = getchar();
					if (ch >= 'a' && ch <= 'z')
						ss[len++] = ch;
					else
						break;
				}
				ss[len] = '\0';
				break;
			}
		}
	}
	memcpy(tree[now].fea, ss, sizeof(ss));
	tree[now].sun[0] = id + 1;
	build(++id);
	tree[now].sun[1] = id + 1;
	build(++id);
	while(true)
	{
		ch = getchar();
		if (ch == ')')
			break;
	}
}
void dfs(int now)
{
	ans *= tree[now].val;
	if (tree[now].sun[0] == -1)
		return ;
	if (M[tree[now].fea])
	{
		dfs(tree[now].sun[0]);
	}
	else
	{
		dfs(tree[now].sun[1]);
	}
}
int main()
{
	int  len, i , j, p ;
	freopen("111.in","r",stdin);
	freopen("a1.txt","w",stdout);
	int cas, nca;
	scanf("%d",&cas);
	nca = 0;
	while(cas--)
	{
		nca++;
		if (nca == 63)
			int tt = 1;
		scanf("%d",&n);
		id = 0;
		all = 0;
		build(0);
		printf("Case #%d:\n",nca);
		int m;
		scanf("%d",&m);
		for(i = 1; i <= m; i++)
		{
			M.clear();
			scanf("%s",need);
			scanf("%d",&p);
			for(j = 1; j <= p; j++)
			{
				scanf("%s",need);
				M[need] = 1;
			}
			ans = 1.0;
			dfs(0);
			printf("%.7lf\n",ans);
		}
	}

}