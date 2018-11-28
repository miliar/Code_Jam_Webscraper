#include<map>
#include<string>
#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;
vector<map<string,int> > vec;
vector<string> dir;
int n,m;
string str;
int ans;
void trans(string &str,vector<string> &dir)
{
	string acc;
	dir.resize(0);
	for(int i=1;i<str.size();++i)
	{
		if(str[i]=='/'){
			dir.push_back(acc);
			acc="";
		}else acc+=str[i];
	}
	dir.push_back(acc);
}
void add(vector<string> &dir,int cur,bool flag)
{
	for(int i=0;i<dir.size();++i)
	{
		if(vec[cur].count(dir[i])==0)
		{
			vec.push_back(map<string,int>());
			vec[cur][dir[i]]=vec.size()-1;
			cur=vec.size()-1;
			if(flag)  ans++;
		}else{
			cur=vec[cur][dir[i]];
		}
	}
}
int main()
{
	freopen("fix.in","r",stdin);
	freopen("fix.out","w",stdout);
	int cs;
	cin>>cs;
	for(int t=1;t<=cs;++t)
	{
		printf("Case #%d: ",t);
		ans=0;
		vec.resize(1);
		vec[0].clear();
		cin>>n>>m;
		for(int i=0;i<n;++i)
		{
			cin>>str;
			if(str=="/") continue;
			trans(str,dir);
			add(dir,0,false);
		}
		for(int i=0;i<m;++i)
		{
			cin>>str;
			if(str=="/") continue;
			trans(str,dir);
			add(dir,0,true);
		}
		cout<<ans<<endl;
	}
	return 0;
}
