#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<map>
#include<cstring>
using namespace std;

struct Node
{
	Node *c[110000];
};

int N,M,k;
int num,ans;
char path[110][110];
Node *root;
map<string,int> Map;

void add(Node *p,int level)
{
	if(level >= k) return ;
	if(Map.find(path[level])==Map.end())
		Map[path[level]] = num++;
	int id = Map[path[level]];
	if(!p->c[id])
	{	
		p->c[id] = (Node*)malloc(sizeof(Node));
		memset(p->c[id]->c,0,sizeof(p->c[id]->c));
	}
	add(p->c[id],level+1);
}

void Count(Node *p,int level)
{
	if(level >= k) return ;
	if(Map.find(path[level])==Map.end())
		Map[path[level]] = num++;
	int id = Map[path[level]];
	if(!p->c[id])
	{	
		ans++;
		p->c[id] = (Node*)malloc(sizeof(Node));
		memset(p->c[id]->c,0,sizeof(p->c[id]->c));
	}
	Count(p->c[id],level+1);
}


int main()
{
	int i;
	int T,Case=1;
	char s[110],*p;
	freopen("A-small-attempt0.in","r",stdin);
	freopen("Output.txt","w",stdout);
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&N,&M);
		num = 0 , Map.clear();
		root = (Node*)malloc(sizeof(Node));
		memset(root->c,0,sizeof(root->c));
		for(i=0;i<N;i++)
		{
			scanf("%s",s);
			k = 0;
			for(p=strtok(s+1,"/");p;p=strtok(NULL,"/"))
			{
				strcpy( path[k++], p );
			}
			add(root,0);
		}
		ans = 0;
		for(i=0;i<M;i++)
		{
			scanf("%s",s);
			k = 0;
			for(p=strtok(s,"/");p;p=strtok(NULL,"/"))
			{
				strcpy( path[k++], p );
			}
			Count(root,0);
		}
		printf("Case #%d: %d\n",Case++,ans);
	}
	return 0;
}
		
