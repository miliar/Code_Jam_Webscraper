#include<iostream>
#include<string>
#include<map>
#include<algorithm>
using namespace std;
const int maxn=100;
string s;
map<char,int> hash;
bool mark[maxn];
long long ans;
void solve()
{
	hash.clear();
	memset(mark,0,sizeof(mark));
	long long d=0;
	for (int i=0;i<s.size();i++)
	{
		if (hash.find(s[i])==hash.end())
		{
			int j;
			if (i)
				j=0;
			else
				j=1;
			while (mark[j])
				j++;
			mark[j]=true;
			hash[s[i]]=j;
			if (j>d)
				d=j;
		}				
	}
	d++;
	ans=0;
	for (int i=0;i<s.size();i++)
		ans=ans*d+(long long)hash[s[i]];
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int t;
	cin >>t;
	for (int i=1;i<=t;i++)
	{
		cin >>s;
		solve();
		cout <<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
