#include<iostream>
#include<map>
#include<vector>
#include<string>
using namespace std;
struct node
{
	int f;
	map<string,int>mp;
	void init(){f=0;mp.clear();}
}s[100000],t[100000];
void dfs(int z,string w)
{
	cout<<w<<endl;
	for(map<string,int>::iterator it = s[z].mp.begin();it!=s[z].mp.end();it++)
	{
		dfs(it->second,w+"/"+it->first);
	}
}
void dfst(int z,string w)
{
	cout<<w<<endl;
	for(map<string,int>::iterator it = t[z].mp.begin();it!=t[z].mp.end();it++)
	{
		dfst(it->second,w+"/"+it->first);
	}
}
int res = 0;
void solve(int z1,int z2, int f)
{
	if(f)
	{
		for(map<string,int>::iterator it = t[z2].mp.begin();it!=t[z2].mp.end();it++)
		{
			if(s[z1].mp.find(it->first)==s[z1].mp.end())
			{
				solve(-1,it->second,0);
			}else
			{
				solve(s[z1].mp[it->first],it->second,1);
			}
		}
	}
	else
	{
		res++;
		for(map<string,int>::iterator it = t[z2].mp.begin();it!=t[z2].mp.end();it++)
		{
			solve(-1,it->second,0);
		}
	}
}
int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int zu;
	cin>>zu;
	for(int Cas =1 ; Cas<=zu;Cas++)
	{
		printf("Case #%d: ",Cas);
		int ind=0;
		int indt=0;
		int m,n;
		s[ind=0].init();
		cin>>m>>n;
		for(int i=0;i<m;i++)
		{
			string ss;
			cin>>ss;
			vector<string>a ;
			int pre = ss.length();
			for(int j=ss.length()-1;j>=0;j--)
			{
				if(ss[j]=='/')
				{
					a.push_back(ss.substr(j+1,pre-j-1));
					pre = j;
				}
			}
			int index=0;
			for(int j=a.size()-1;j>=0;j--)
			{
				if(s[index].mp.find(a[j])==s[index].mp.end())
				{
					s[++ind].init();
					s[index].mp[a[j]]=ind;
				}
				index=s[index].mp[a[j]];
			}
			s[index].f=1;
		}
		//dfs(0,"");

		t[indt=0].init();
		for(int i=0;i<n;i++)
		{
			string ss;
			cin>>ss;
			vector<string>a ;
			int pre = ss.length();
			for(int j=ss.length()-1;j>=0;j--)
			{
				if(ss[j]=='/')
				{
					a.push_back(ss.substr(j+1,pre-j-1));
					pre = j;
				}
			}
			int index=0;
			for(int j=a.size()-1;j>=0;j--)
			{
				if(t[index].mp.find(a[j])==t[index].mp.end())
				{
					t[++indt].init();
					t[index].mp[a[j]]=indt;
				}
				index=t[index].mp[a[j]];
			}
			t[index].f=1;
		}
		//dfst(0,"");
		res=0;
		solve(0,0,1);
		printf("%d\n",res);
	}
}