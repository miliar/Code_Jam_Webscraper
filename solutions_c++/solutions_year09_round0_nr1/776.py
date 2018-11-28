#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<queue>
#include<cmath>
#include<map>
using namespace std;
int l,d,n;
int ans;
vector<string>v;
class trie
{
public:
	trie * next[26];
	trie()
	{
		for(int i=0;i<26;i++)
			next[i]=0;
	}
}root;
void insert(const string & s)
{
	trie * now=&root;
	int k=0;
	while(k<s.length())
	{
		if(now->next[s[k]-'a']==NULL)
			now->next[s[k]-'a']=new trie;
		now=now->next[s[k]-'a'];
		k++;
	}
}
void split(const string & s)
{
	for(int i=0;s[i]!='\0';i++)
	{
		if(s[i]>='a' && s[i]<='z')
		{
			v.push_back(s.substr(i,1));
		}
		else if(s[i]=='(')
		{
			int tmp=++i;
			for(;s[i]!=')';i++);
			v.push_back(s.substr(tmp,i-tmp));
		}
	}
}
void dfs(trie * now,int cnt)
{
	if(cnt==l) 
	{
		ans++;
		return;
	}
	for(int i=0;i<v[cnt].size();i++)
	{
		if(now->next[v[cnt][i]-'a'])
			dfs(now->next[v[cnt][i]-'a'],cnt+1);
	}
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	string s;
	cin>>l>>d>>n;
	while(d--)
	{
		cin>>s;
		insert(s);
	}
	for(int i=1;i<=n;i++)
	{
		cin>>s;
		ans=0;
		v.clear();
		split(s);
		dfs(&root,0);
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
}