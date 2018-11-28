#include <stdio.h>
#include <string>
#include <set>
using namespace std;

typedef set<string> sset;

struct tree
{
	tree()
	{
		p=0.0;
		name="";
		child[0]=0;
		child[1]=0;
	}
	double p;
	string name;
	tree* child[2];
};
int cnt;
void buildtree(const char* s, tree* des)
{
	while (s[cnt]!='(')
		cnt++;
	cnt++;
	while (s[cnt]==' ')
		cnt++;
	sscanf(s+cnt,"%lf",&(des->p));
	while (s[cnt]!=' ' && s[cnt]!=')')
		cnt++;
	while (s[cnt]==' ')
		cnt++;
	if (s[cnt]!=')')
	{
		char buf[80];
		sscanf(s+cnt,"%s",buf);
		des->name=buf;
		while (s[cnt]!=' ')
			cnt++;
		des->child[0] = new tree();
		des->child[1] = new tree();

		buildtree(s,des->child[0]);
		buildtree(s,des->child[1]);
	}
	while (s[cnt]!=')')
		cnt++;
	cnt++;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nt;
	scanf("%d",&nt);
	for (int t=0;t<nt;t++)
	{
		int nl;
		char line[100];
		scanf("%d",&nl);
		gets(line);
		string treeString;
		for (int l=0;l<nl;l++)
		{
			gets(line);
			treeString+=line;
			treeString+=" ";
		}

		cnt=0;
		tree* des = new tree();
		buildtree(treeString.c_str(), des);
		int na;
		scanf("%d",&na);
		printf("Case #%d:\n",t+1);
		for (int a=0;a<na;a++)
		{
			int n;
			sset prop;
			scanf("%s%d",line,&n);
			for (int i=0;i<n;i++)
			{
				scanf("%s",line);
				prop.insert(line);
			}

			double ans=1.0;
			tree* it = des;
			while(1)
			{
				ans*=it->p;
				if (it->name=="")
					break;
				if (prop.find(it->name)!=prop.end())
					it=it->child[0];
				else
					it=it->child[1];
			}
			printf("%.10lf\n",ans);
		}
	}
	return 0;
}
