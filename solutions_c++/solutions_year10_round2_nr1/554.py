#include <stdio.h>
#include <vector>
#include <string>
#include <string.h>
#include <map>
using namespace std;

char s[100000];
vector<string> dir(char *s)
{
	vector<string> res;
	char *p=strtok(s,"/");
	if(p==0) return res;
	res.push_back(p);
	for(;;)
	{
		p=strtok(0,"/");
		if(p==0) break;
		res.push_back(p);
	}
	return res;
}
struct tree
{
	map<string,tree*> child;
}empty,root;
int counter=0;
void ins(vector<string> &vs)
{
	int i,j,k;
	tree *now=&root;
	for(i=0;i<vs.size();i++)
	{
		string t=vs[i];
		if(now->child.find(t)==now->child.end() )
		{
			counter++;
			tree *node=new tree;
			now->child.insert(pair<string,tree*>(t,node));
		}
		now=now->child.find(t)->second;
	}
}
int main()
{
	int i,j,k;
	int n,m;
	int cas;
	freopen("e:\\1.txt","r",stdin);
	freopen("e:\\2.txt","w",stdout);
	scanf("%d",&cas);
	for(int x=1;x<=cas;x++)
	{
		scanf("%d%d",&n,&m);
		root.child.clear();
		for(i=0;i<n;i++)
		{
			scanf("%s",s);
			//dir(s);
			ins( dir(s) );
		}
		counter=0;
		for(i=0;i<m;i++)
		{
			scanf("%s",s);
			//dir(s);
			ins( dir(s) );
		}
		printf("Case #%d: %d\n",x,counter);
	}
	return 0;
}