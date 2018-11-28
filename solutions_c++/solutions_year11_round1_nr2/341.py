#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;
typedef vector<string> VS;
typedef VS::iterator VS_I;
typedef pair<char,int> PCI;
typedef vector<PCI> VPCI;
typedef pair<VPCI,int> PVPCI;
typedef vector<PVPCI> VPVPCI;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef map<VI,int> MVI;

VS dic;
VS orig;
int n,m;
bool contains(string &str,int ch)
{
		for(int j=0;j<str.length();j++)
		{
			if(str[j]==ch)
			{
				return true;
			}
		}
	return false;
}
int solve()
{
	VPVPCI list(n);
	for(int i=0;i<n;i++)
	{
		list[i].second=i;
		list[i].first.push_back(make_pair('\0',(int)dic[i].length()));
	}
	for(char ch='a';ch<='z';ch++)
	{
		MVI pat;
		for(int i=0;i<n;i++)
		{
			int len=dic[i].length();
			VI tmp;
			for(int j=0;j<len;j++)
				if(dic[i][j]==ch) tmp.push_back(j);
			//if(tmp.size()==0) continue;
			MVI::iterator it=pat.find(tmp);
			int id;
			if(it==pat.end())
			{
				id=(int)pat.size();
				pat.insert(make_pair(tmp,id));
			}
			else
			{
				id=it->second;
			}
			list[i].first.push_back(make_pair(ch,id));
		}
	}
	sort(list.begin(),list.end());
	vector<int> height(n);
	for(int i=1;i<n;i++)
	{
		int t=0;
		for(;t<26;t++)
		{
			if(list[i-1].first[t]!=list[i].first[t]) break;
		}
		height[i]=t;
	}
	/*for(int i=0;i<n;i++)
	{
		printf("%s,%s: %d\n",dic[list[i].second].c_str(),orig[list[i].second].c_str(),height[i]);
	}*/
	vector<int> gap(n);
	vector<vector<int> > gan(n);
	for(int i=1;i<n;i++)
	{
		gan[i]=gan[i-1];
		while(!gan[i].empty()&&gan[i].back()>=height[i]) gan[i].pop_back();
		gan[i].push_back(height[i]);
	}
	vector<vector<int> > gao(n);
	for(int i=n-1;i>0;i--)
	{
		gao[i-1]=gao[i];
		while(!gao[i-1].empty()&&gao[i-1].back()>=height[i]) gao[i-1].pop_back();
		gao[i-1].push_back(height[i]);
	}
	pair<int,int> ans(1,n);
	for(int i=0;i<n;i++)
	{
		//printf("i=%d\n",i);
		bool u[30]={};
		int xx=0;
		string str=dic[list[i].second];
		for(vector<int>::iterator it=gan[i].begin();it!=gan[i].end();it++)
		{
			//printf("a %d\n",*it);
			if(!contains(str,*it+'a'-1)) u[*it]=true;
			xx=max(xx,*it);
		}
		for(vector<int>::iterator it=gao[i].begin();it!=gao[i].end();it++)
		{
			//printf("b %d\n",*it);
			if(!contains(str,*it+'a'-1)) u[*it]=true;
			xx=max(xx,*it);
		}
		int t=0;
		for(int j=0;j<=26;j++)
		{
			if(u[j]) t++;
		}
		/*for(int j=0;j<str.length();j++)
		{
			if(str[j]==xx+'a'-1)
			{
				t--;
				break;
			}
		}*/
		//printf("%d: %d,%d %d %d\n",i,gan[i].size(),gao[i].size(),t,list[i].second);
		ans=min(make_pair(-t,list[i].second),ans);
	}
	//printf("%d,%d\n",ans.first,ans.second);
	return ans.second;
}
int main()
{
	int t;
	scanf("%d",&t);
	for(int cs=1;cs<=t;cs++)
	{
		scanf("%d%d",&n,&m);
		orig.clear();
		for(int i=0;i<n;i++)
		{
			char str[1024];
			scanf("%s",str);
			orig.push_back(string(str));
		}
		printf("Case #%d:",cs);
		for(int i=0;i<m;i++)
		{
			char str[1024];
			char per[30];
			scanf("%s",str);
			for(int i=0;i<26;i++)
			{
				per[str[i]-'a']=i+'a';
			}
			dic.clear();
			for(int i=0;i<n;i++)
			{
				string temp=orig[i];
				int len=temp.length();
				for(int j=0;j<len;j++)
					temp[j]=per[temp[j]-'a'];
				dic.push_back(temp);
			}
			printf(" %s",orig[solve()].c_str());
		}
		putchar('\n');
	}
	return 0;
}
