#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<map>
using namespace std;
int main()
{
	ofstream fout("A.out");
	int T;
	cin>>T;
	string s;
	vector<int> v(70);
	vector<int> mp(200);
	int i,j,cnt;
	long long base;
	for(i=0;i<T;++i)
	{
		cin>>s;
		if(s.length()==1)
		{
			fout<<"Case #"<<(i+1)<<": "<<1<<endl;
			continue;
		}
		//cout<<"in: "<<s<<endl;		
		for(j=0;j<200;++j)
			mp[j]=-1;
		mp[s[0]]=1;
		v[0]=1;
		if(s[1]==s[0])
		{
			v[1]=1;
			cnt=0;
			base=2;
		}
		else
		{
			v[1]=(mp[s[1]]=0);
			cnt=2;
			base=-1;
		}
		//cnt=2;
		for(j=2;j<s.length();++j)
		{
			if(cnt==1)++cnt;
			if(mp[s[j]]==-1)
				mp[s[j]]=cnt++;
			v[j]=mp[s[j]];
			//cout<<v[j]<<endl;
		}
		if(base<cnt)
			base=(long long)cnt;
		
		long long ans=0;
		for(j=0;j<s.length();++j)
		{
			ans=ans*base+(long long)v[j];
		}
		fout<<"Case #"<<(i+1)<<": "<<ans<<endl;
	}
			
			
		
	//ifstream fin("A.in");
	return 0;
}
