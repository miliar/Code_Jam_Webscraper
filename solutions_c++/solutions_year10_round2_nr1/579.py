#include<stdio.h>
#include<vector>
#include<map>
#include<string>
#include<string.h>
using namespace std;

vector<string> v;

int countnum;
int ans;

struct Trie_node
{
	string name;
	map<string,int> my;
	Trie_node *next[10001];
	Trie_node()
	{
		my.clear();
		memset(next,NULL,sizeof(next));
	}
};

class Trie
{
public :
	Trie();
	void insert_node(const vector<string>,bool set);
private:
	Trie_node *root;
};

Trie::Trie()
{
	root=new Trie_node();
}

void Trie::insert_node(const vector<string> v,bool set)
{
	Trie_node *location=root;
	int len=v.size();
	int i=0;
	while(i<len)
	{
		if((*location).my[v[i]]==0)
		{
			Trie_node *tmp=new Trie_node();
			if(set==false)
			{
				ans++;
			}
			(*location).my[v[i]]=++countnum;
			(*location).next[(*location).my[v[i]]]=tmp;
		}
		location=(*location).next[(*location).my[v[i]]];
		i++;
	}
	return ;
}

int main(void)
{
	int t;
	int yy=0;
	freopen("A-large.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		int n,m;
		yy++;
		ans=countnum=0;
		char s[100001];
		char t[100001];
		Trie tree;
		scanf("%d%d",&n,&m);
		//printf("%d%d",n,m);
		int i,f;
		for(f=0;f<n;f++)
		{
			scanf("%s",s);
			//printf("%s\n",s);
			int len=strlen(s);
			int j,k=0;
			string tt;
			for(i=0;i<len;i++)
			{
				if(s[i]=='/')
				{
					for(j=0;j<i-k;j++)
					{
						t[j]=s[k+j];
					}
					t[j]='\0';
					if(strlen(t))
					{
						tt=t;
						v.push_back(tt);
					}
					k=i+1;
				}
			}
			for(j=0;j<i-k;j++)
			{
				t[j]=s[k+j];
			}
			t[j]='\0';
			if(strlen(t))
			{
				tt=t;
				v.push_back(tt);
			}
			tree.insert_node(v,true);
			v.clear();
		}
		for(f=0;f<m;f++)
		{
			scanf("%s",s);
			//printf("%s",s);
			int len=strlen(s);
			int j,k=0;
			string tt;
			for(i=0;i<len;i++)
			{
				if(s[i]=='/')
				{
					for(j=0;j<i-k;j++)
					{
						t[j]=s[k+j];
					}
					t[j]='\0';
					if(strlen(t))
					{
						tt=t;
						v.push_back(tt);
					}
					k=i+1;
				}
			}
			for(j=0;j<i-k;j++)
			{
				t[j]=s[k+j];
			}
			t[j]='\0';
			if(strlen(t))
			{
				tt=t;
				v.push_back(tt);
			}
			tree.insert_node(v,false);
			v.clear();
		}
		printf("Case #%d: %d\n",yy,ans);
	}
	return 0;
}
