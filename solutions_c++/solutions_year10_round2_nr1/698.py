#include <stdio.h>
#include <algorithm>
#include <map>
#include <string>
#include <cstring>
using namespace std;

struct node
{
	int n;
	int d[110];
	bool operator < (const node &big) const
	{
		return n<big.n;
	}
} a[110];

bool tree[110][110];
map<string, int> name;
char str[100010];
char temp[100010];
int ans, t, n, m;

void  read(int x)
{	
	int i, j;
	i=j=0;
	gets(str);
	while (str[i]!='\0')
	{
		do
		{
			temp[j++]=str[i++];
		}
		while (str[i]!='\0' && str[i]!='/') ;
		temp[j]='\0';
		if (name[temp]==0) name[temp]=++t;
		a[x].d[a[x].n++]=name[temp];
	}
}

int add(int x)
{
	int root, i, j, ans=0;;
	root=0;
	for (i=0; i<a[x].n; i++)
	{
		j=a[x].d[i];
		if (!tree[root][j])
		{
			tree[root][j]=true;
			ans++;
		}
		root=j;
	}
	return ans;
}


int main()
{
	int T, ti, i;
	freopen("a.in", "r", stdin);
	freopen("out.txt", "w", stdout);	
	scanf("%d", &T);
	for (ti=1; ti<=T; ti++)
	{
		memset(a, 0, sizeof(a));
		memset(tree, false, sizeof(tree));
		scanf("%d%d\n", &n, &m);
		name.clear();
		t=0;
		for (i=0; i<n+m; i++)
		  read(i);	  
		for (i=0; i<n; i++)
		  add(i);  
		sort(a+n, a+n+m);	
		ans=0;	  
		for (i=n; i<n+m; i++)
		{
			int temp=add(i);
//			printf("%d:%d\n",i, temp);
		 	ans+=temp;
		}
		printf("Case #%d: %d\n", ti, ans);
	}
	return 0;
}
