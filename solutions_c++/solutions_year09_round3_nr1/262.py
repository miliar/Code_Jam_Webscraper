#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<string>
#include<cctype>
#include<fstream>

using namespace std;

int main()
{
	int T;
	cin>>T;
	int K=T;
	ofstream fout("out.txt");
	while(T--)
	{
		string s;
		cin>>s;
		vector <int> st;
		st.resize(26+10,-1);
		if(s[0]>='a'&&s[0]<='z')
			st[int(s[0]-'a')+10]=1;
		else if(s[0]>='0'&&s[0]<='9')
			st[int(s[0]-'0')]=1;
		int counter=0;
		for(int i=1;i<s.size();i++)
		{
			if(counter==1)
				counter++;
			if(s[i]>='a'&&s[i]<='z'&&st[int(s[i]-'a')+10]==-1)
			{
				st[int(s[i]-'a')+10]=counter;
				counter++;
			}
			else if(s[i]>='0'&&s[i]<='9'&&st[int(s[i]-'0')]==-1)
			{
				st[int(s[i]-'0')]=counter;
				counter++;
			}
		}
		if(counter<2)
			counter=2;
		vector <int> ans;
		ans.resize(s.size());
		long long int base=1;
		for(int i=0;i<ans.size();i++)
		{
			if(s[i]>='a'&&s[i]<='z')
				ans[i]=st[int(s[i]-'a')+10];
			else
				ans[i]=st[int(s[i]-'0')];
		}
		long long int answer=0;
		for(int i=ans.size()-1;i>=0;i--)
		{
			answer+=ans[i]*base;
			base*=counter;
		}
		fout<<"Case #"<<K-T<<": "<<answer<<endl;
	}
	return 0;
}   

