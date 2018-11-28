#include <algorithm>  
#include <string>
#include <cstring>  
#include <cstdlib>  
#include <cstdio>  
#include <vector>  
#include <cmath>  
#include <queue>  
#include <map>

using namespace std;  

typedef vector<int> VI;  
typedef vector<string> VS;  
typedef long long ll;  

#define sz size()   
#define pb push_back  
#define all(x) (x).begin(),(x).end()  
#define For(i,n) for(int i=0, _n=(n);i<_n;++i)  
#define For2(i,a,b) for(int i=(a), _n=(b);i<_n;++i)  
#define MAX 0x3FFFFFFF

class tree
{
public:
	map<string, tree*> child;
};

void del(tree* node)
{
	if(node->child.sz)
		for(map<string,tree *>::iterator it = node->child.begin(); it != node->child.end(); ++it) 
			del(it->second);
	node->child.clear();
}

vector<string> a[128];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ti=0,tn;
	char p[128];
	scanf("%d",&tn);
	tree *root = new tree();
	root->child.clear();
	while(tn--)
	{
		int n, m;
		del(root);
		scanf("%d %d",&n,&m);
		For(i,n) 
		{
			scanf("%s",p);
			string str = string(p);
			int index = 1, len = str.sz;
			tree *cur = root;
			For2(j,1,len) if(str[j]=='/' || j == len-1) 
			{
				string dir;
				if(j == len-1) dir = str.substr(index, j-index+1);
				else dir = str.substr(index, j-index);
				if(cur->child.find(dir) != cur->child.end()) cur = cur->child[dir];
				else
				{
					tree *tmp = new tree();
					tmp->child.clear();
					cur->child[dir] = tmp;
					cur = tmp;
				}
				index = j + 1;
			}
		}
		For(i,m) 
		{
			scanf("%s",p);
			string str = string(p);
			int index = 1;
			a[i].clear();
			For2(j,1,str.sz) if(str[j]=='/') 
			{
				a[i].pb(str.substr(index, j-index)); 
				index = j + 1;
			}
			if(index < str.sz) a[i].pb(str.substr(index, str.sz-index));
		}
		sort(a,a+m);
		int ans = 0;
		For(i,m)
		{
			tree *cur = root;
			For(j,a[i].sz)
			{
				if(cur->child.find(a[i][j]) == cur->child.end())
				{
					++ans;
					tree *tmp = new tree();
					tmp->child.clear();
					cur->child[a[i][j]] = tmp;
					cur = tmp;
				}
				else cur = cur->child[a[i][j]];
			}
		}
		printf("Case #%d: %d\n",++ti,ans);
	}
}
/*
3
0 2
/home/gcj/finals
/home/gcj/quals
2 1
/chicken
/chicken/egg
/chicken
1 3
/a
/a/b
/a/c
/b/b
*/