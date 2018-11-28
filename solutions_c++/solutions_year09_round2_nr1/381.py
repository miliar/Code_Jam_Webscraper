#include <iostream>
#include <map>
#include <stack>
using namespace std;

struct node
{
	char name[100];
	bool flag;
	int next;
	int next1;
	int fa;
	double num;
}date[30000];

char s[1000000] , a[110][110];

stack <int>num;

int k;

void input(int now)
{
	while(scanf("%c" , &s[0]) == 1 && s[0] != '(');
	scanf("%lf" , &date[now].num);
	while(scanf("%c" , &s[0]) == 1)
	{
		if(s[0] == ')')
			break;
		if(s[0] >= 'a' && s[0] <= 'z')
			break;
	}
	if(s[0] == ')')
	{
		date[now].next = -1;
		return ;
	}
	else
	{
		date[now].name[0] = s[0];
		int i = 1;
		while(scanf("%c" , &date[now].name[i]) == 1 && date[now].name[i] >= 'a' && date[now].name[i] <= 'z')
		{
			i ++;
		}
		date[now].name[i] = '\0';
		date[now].next = k + 1;
		input(++k);
		date[now].next1 = k + 1;
		input(++k);
		while(scanf("%c" , &s[0]) == 1 && s[0] != ')');
	} 
}

double ans;

int m;

void dfs(int now)
{
	int i , j;
	ans *= date[now].num;
	if(date[now].next == -1)
		return ;
	for(i = 0 ; i < m ; i ++)
	{
		if(strcmp(a[i] , date[now].name) == 0)
			break;
	}
	if(i == m)
	{
		dfs(date[now].next1);
	}
	else
	{
		dfs(date[now].next);
	}
}

int main()
{
	int i , j , t , n , now , cas = 0;
	freopen("1.txt" , "w" , stdout);
	scanf("%d" , &t);
	while(t --)
	{
		cas ++;
		scanf("%d" , &n);
		now = -1;
		getchar();
		k = 0;
		input(0);
		scanf("%d" , &n);
		printf("Case #%d:\n" , cas);
		while(n --)
		{
			ans = 1;
			scanf("%s" , s);
			scanf("%d" , &m);
			for(i = 0 ; i < m ; i ++)
			{
				scanf("%s" , a[i]);
			}
			dfs(0);
			printf("%.6lf\n" , ans);
		}
	}
	return 0;
}