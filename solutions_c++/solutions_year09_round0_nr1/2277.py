#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
using namespace std; 

struct node
{
	int val;

	node *next[26];

	node()
	{
		int i;
		val=-1;
		for(i=0;i<26;i++)
			next[i]=NULL;
	}
	~node()
	{
		int i;
		for(i=0;i<26;i++)
			delete next[i];
	}
};

node *root;

char s[2000];
vector<int> po[20];
int ans,len;

void update(node *now,int pos,int is)
{
	if(!is)
	{
		if(!s[pos])
		{
			now->val=1;
			return;
		}
		int v=s[pos]-'a';
		if(!now->next[v])
			now->next[v]=new node();
		update(now->next[v],pos+1,is);
		return;
	}
	int i;
	if(pos==len)
	{
		ans++;
		return;
	}
	for(i=0;i<po[pos].size();i++)
	{
		int v=po[pos][i];
		if(!now->next[v])
			continue;
		else
			update(now->next[v],pos+1,is);
	}
}

int main()
{
	freopen("alien.in","r",stdin);
	freopen("alien1.out","w",stdout);
	int n,d,i;
	while(scanf("%d%d%d",&len,&d,&n)==3)
	{
		root= new node;
		for(i=0;i<d;i++)
			scanf("%s",s),update(root,0,0);
		for(i=0;i<n;i++)
		{
			scanf("%s",s);
			
			int j=0,k=0;
			while(s[j])
			{
				po[k].clear();
				if(s[j]!='(')
					po[k].push_back(s[j]-'a');
				else
				{
					j++;
					while(s[j]!=')')
						po[k].push_back(s[j]-'a'),j++;
				}
				j++;
				k++;
			}
			ans=0;
			update(root,0,1);
			printf("Case #%d: %d\n",i+1,ans);
		}				
	}
	return 0;
}