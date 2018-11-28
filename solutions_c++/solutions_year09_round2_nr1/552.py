#pragma warning(disable:4786)
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <algorithm>
#include <set>
using namespace std;

struct node
{
	node *one, *second;
	double p;
	string name;
	node(){one=second=0;}
};
char g[500000],tp[200];
int n;
node *root;
set<string> st;
void next(int& i)
{
	for (; g[i] ; i++)if(g[i]!=' '&&g[i]!='\n')break;
}
void nextf(int& i)
{
	for (; g[i] && (g[i]<='9'&&g[i]>='0'||g[i]=='.') ; i++);
}
void dfsb(int& i, node *&fa)
{
	int d= i;
	next(i);
	i++;d= i;
	fa = new node();
	next(i);
	double t;
	sscanf(g+i,"%lf",&t);
	fa->p = t;
	nextf(i);
	next(i);d= i;
	if(g[i]==')') {i++; return;}

	for (d=0; g[i] && g[i]<='z' && g[i]>='a';i++,d++)tp[d]=g[i];
//	sscanf(g+i,"%s",tp);
	tp[d]=0;
	fa->name = tp;
//	i += strlen(tp);
	dfsb(i,fa->one);d= i;
	dfsb(i,fa->second);d= i;
	next(i);i++;
}

double dfs(node *root)
{
	if(root->name.empty()) return root->p;
	if(st.find(root->name)!=st.end()) return root->p * dfs(root->one);
	return root->p * dfs(root->second);
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca,i,j,p,v,ans,ar,ac,t;
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ca++)
	{
		scanf("%d",&n);gets(g);
		g[0]=0;
		for (i = 0 ; i < n ;i++)
		{
			gets(g+strlen(g));
		}
		n = strlen(g); i =0;
		root=0;
		dfsb(i,root);

		printf("Case #%d:\n",ca);
		scanf("%d",&n);
		while(n--)
		{
			scanf("%*s%d",&t);
			ans = 1;
			st.clear();
			while(t--)
			{
				scanf("%s",tp);
				st.insert(tp);
			}
			printf("%lf\n",dfs(root));
		}
	}

	return 0;
}
