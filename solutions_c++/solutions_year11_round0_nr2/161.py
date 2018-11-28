#include<iostream>
#include<string>
#include<cstdio>
#include<vector>
using namespace std;
char a[500][500];

bool find(vector<char>& v,char c)
{
	for(int i=0;i<v.size();i++)
		if(v[i] == c) return true;
	return false;
}
int main()
{
	freopen("in.txt","rt",stdin);
	freopen("B_large.txt","wt",stdout);
	int TC,c,i;
	string s;
	cin>>TC;
	for(int tc = 0;tc<TC;tc++)
	{
		memset(a,0,sizeof(a));
		cin>>c;
		for(i=0;i<c;i++)
		{
			cin>>s;
			a[s[0]][s[1]] = s[2];
			a[s[1]][s[0]] = s[2];
		}
		cin>>c;
		vector<string> opp;
		for(i=0;i<c;i++)
		{
			cin>>s;
			opp.push_back(s);
		}
		cin>>c;
		cin>>s;
		vector<char> out;
		for(int i=0;i<s.size();i++)
		{
			if(!out.size())
			{
				out.push_back(s[i]);
				continue;
			}
			if( a[out.back()][s[i]] != 0 )
			{
				char cc = out.back();
				out.pop_back();
				out.push_back(a[cc][s[i]]);
			}
			else
			{
				for(int j=0;j<(int)opp.size();j++)
				{
					if(s[i] == opp[j][0] && find(out,opp[j][1]))
						out.clear();
					if(s[i] == opp[j][1] && find(out,opp[j][0]))
						out.clear();
				}
				if(out.size())
					out.push_back(s[i]);
			}
			

		}
		cout<<"Case #"<<tc+1<<": [";
		s = "";
		for(i=0;i<out.size();i++)
		{
			cout<<s<<out[i];
			s = ", ";
		}
		cout<<"]\n";
	}
	return 0;
}