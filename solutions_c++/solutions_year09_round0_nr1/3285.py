#include<iostream>
#include<string>
#include<map>
#include<queue>
#include<vector>
using namespace std;
map<string,int>hash;
vector<string>words;
queue<string>que;
vector<string>vec;
int D,ans;
void solve(int depth,string str)
{
	if(depth==vec.size())
	{
		ans+=hash[str];
		return;
	}
	bool flag=false;
	for(int i=0;i<words.size();i++)
	{
		string tmp=words[i].substr(0,str.size());
		if(tmp==str)
		{
			flag=true;
			break;
		}
	}
	if(!flag)return;
	for(int i=0;i<vec[depth].size();i++)
	{
		str+=vec[depth][i];
		solve(depth+1,str);
		str.erase(str.size()-1);
	}
}
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int L,N;
	string str;
	scanf("%d%d%d",&L,&D,&N);
	hash.clear();
	words.clear();
	for(int i=0;i<D;i++)
	{
		cin>>str;
		words.push_back(str);
		hash[str]++;
	}
	for(int i=1;i<=D;i++)
	{
		cin>>str;
		int cnt=0;
		vec.clear();
		for(int j=0;j<str.size();j++)
		{
			string tmp="";
			if(str[j]=='(')
			{
				j++;
				while(str[j]!=')'){tmp+=str[j];j++;}
			}
			else tmp+=str[j];
			vec.push_back(tmp);
		}
		ans=0;
		solve(0,"");
		printf("Case #%d: %d\n",i,ans);
	}
}