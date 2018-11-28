#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<queue>
#include<set>
#include<algorithm>
#include<sstream>
#include<cmath>
#include<cstdlib>
#include<deque>
#include<list>
#include<stack>
using namespace std;

#define INF 0x7fffffff
#define PI acos(-1.0)
#define EPS (1e-10)
#define SZ(a) int((a).size())

typedef long long LL;

int gcd(int a,int b){return b>0?gcd(b,a%b):a;}

struct node
{
	map<string,node*> v;
};

int insert(node* root,string s)
{
	int ans=0,i;
	string t;
	if(s=="")
		return 0;
	if(s.find("/")!=-1)
	{
		t=s.substr(0,s.find("/"));
		s=s.substr(s.find("/")+1);
	}
	else
	{
		t=s;
		s="";
	}
	if(root->v.find(t)==root->v.end())
	{
		root->v[t]=new node;
		ans++;
	}
	return ans+insert(root->v[t],s);
}

int main()
{
	freopen("C:\\Users\\LL\\Desktop\\GCJ\\1.in","r",stdin);
	freopen("C:\\Users\\LL\\Desktop\\GCJ\\1.out","w",stdout);

	int csNum,cs;
	scanf("%d",&csNum);
	for(cs=1;cs<=csNum;cs++)
	{
		int n,m,i;
		char s[10005];
		scanf("%d%d",&n,&m);
		node root;
		while(n--)
		{
			scanf("%s",s);
			insert(&root,s+1);
		}
		int ans=0;
		while(m--)
		{
			scanf("%s",s);
			ans+=insert(&root,s+1);
		}
		printf("Case #%d: ",cs);
		printf("%d\n",ans);
	}
}