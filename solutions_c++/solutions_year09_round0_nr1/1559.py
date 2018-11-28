#include<iostream>
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;

int n,d,l;
vector < string > v;
string dic[5001],sol;

long long solve(int pos, int last)
{
	if(pos==l)
		return 1;
	
	long long x=0;
	for(int i=0;i<v[pos].size();i++)
	{
		if(dic[last][pos]==v[pos][i])
			x+=solve(pos+1,last);
	}
	return x;
}

int main()
{
	freopen("sm.in","r",stdin);
	freopen("sm.out","w",stdout);
	char t;
	int cnt;
	bool er;
	long long res;
	cin>>l>>d>>n;
	for(int i=0;i<d;i++)
		cin>>dic[i];
	v.resize(l);
	for(int i=0;i<n;i++)
	{
		cnt=0;
		v[cnt].clear();
		er=false;
		while(cnt<l)
		{
			cin>>t;
			if(t<='z' && t>='a')
			{
				v[cnt]+=t;
				if(!er)
				{
					cnt++;
					if(cnt!=l)
						v[cnt].clear();
				}
			}
			if(t=='(')
				er=true;
			if(t==')')
			{
				cnt++;
				er=false;
				if(cnt!=l)
				v[cnt].clear();
			}
		}
		sol.resize(l);
		res=0;
		for(int a=0;a<d;a++)
			res+=solve(0,a);
		
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}
	return 0;
}