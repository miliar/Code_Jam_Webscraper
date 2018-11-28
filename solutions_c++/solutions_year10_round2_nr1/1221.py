#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std;

struct dir
{
	string name;
	vector<dir> subdir;
	void mkdir(string);
	void clear();
};

int ans;

void dir::clear()
{
	int n = subdir.size();
	for(int i=0;i<n;++i)
		subdir[i].clear();
	subdir.clear();
}

void dir::mkdir( string s )
{
	if(s.size() > 0 && s[0] == '/')
		s = s.substr(1,s.size()-1);
	if(s == "")
		return;
	string folder;
	int i,j,n = s.size();
	for(i=0;i<n;++i)
		if(s[i] == '/')
			break;
		else
			folder+=s[i];
	string ss;
	for(j=i+1;j<n;++j)
		ss+=s[j];
	int k = subdir.size();
	for(i=0;i<k;++i)
		if(subdir[i].name == folder)
			break;
	if(i == k)
	{
		++ans;
		dir tmp;
		tmp.name = folder;
		subdir.push_back(tmp);
	}
	subdir[i].mkdir(ss);
}

dir home;

int main()
{
	freopen("output.txt","w",stdout);
	freopen("A-large.in","r",stdin);
	int t,i,j,k,n;
	string s;
	cin>>t;
	int l;
	for(l=1;l<=t;++l)
	{
		cin>>n>>k;
		home.clear();
		for(i=0;i<n;++i)
		{
			cin>>s;
			home.mkdir(s);
		}
		ans = 0;
		for(i=0;i<k;++i)
		{
			cin>>s;
			home.mkdir(s);
		}
		cout<<"Case #"<<l<<": "<<ans<<endl;
	}
	return 0;
}