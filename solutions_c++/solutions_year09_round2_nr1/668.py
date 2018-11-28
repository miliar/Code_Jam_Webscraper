#include <cstdio>
#include <cstring>

typedef struct{char name[100], fea[102][100]; int top;}A;
struct T
{
	char ch[102];
	double n;
}tree[200];
A an[104];
double ans;

void dfs(int t)
{
	char c;
	int i;
	while(c = getchar())
		if(c != ' ' && c != '\n')
			break;
	if(c == '(')
		scanf("%lf", &tree[t].n);
	while(c = getchar())
		if(c != ' ' && c != '\n')
			break;
	if(c >= 'a' && c <= 'z')
	{
		i = 0;
		tree[t].ch[i++] = c;
		while((c = getchar()))
		{
			if(c != ' ' && c != '\n')
			tree[t].ch[i++] = c;
			else
				break;
		}
		dfs(t*2);
		dfs(t*2+1);
		while((c = getchar()) != ')');
	}
}

void Cal(int t, int k)
{
	int i;
	ans *= tree[t].n;
	if(tree[t].ch[0] == '\0')
		return ;
	for(i = 0; i < an[k].top; i++)
		if(!strcmp(an[k].fea[i], tree[t].ch))
			break;
	if(i < an[k].top)
		Cal(t*2, k);
	else
		Cal(t*2+1, k);
}

int main()
{
	int text, cs = 0, i, j;
	//freopen("a.in", "r", stdin);
	//freopen("a.out", "w", stdout);
	scanf("%d", &text);
	while(text--)
	{
		int n, m;
		scanf("%d", &n);
		getchar();
		for(i = 1; i <= n; i++)
			memset(tree[i].ch, '\0', sizeof(tree[i].ch));
		dfs(1);
		scanf("%d", &m);
		printf("Case #%d:\n", ++cs);
		for(i = 0; i < m; i++)
		{
			ans = 1;
			an[i].top = 0;
			scanf("%s %d", an[i].name, &an[i].top);
			for(j = 0; j < an[i].top; j++)
				scanf("%s", an[i].fea[j]);
			Cal(1, i);
			printf("%.7lf\n", ans);
		}
	}
	return 0;
}