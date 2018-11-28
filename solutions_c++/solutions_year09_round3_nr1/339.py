#include<iostream>
#include<map>
#include<string>
using namespace std;

map<char ,int> my;
int main()
{
	freopen("G:\\A-large.in","r",stdin);
	freopen("G:\\A-large.out","w",stdout);
	string s;
	int t;
	bool fl[1000];
	scanf("%d",&t);
	for(int kk=1;kk<=t;++kk)
	{
		my.clear();
		cin>>s;
		if(s.size()==1)
		{
			printf("Case #%d: ",kk);
			printf("1\n");
			continue;
		}
		int n=0;
		memset(fl,0,sizeof(fl));
		for(int i=0;i<s.size();++i)
		{
			if(s[i]>='0'&&s[i]<='9')
			{
				if(fl[s[i]-'0']==0)
					n++;
				fl[s[i]-'0']=1;
			}
			else
			{
				if(fl[s[i]-'a'+10]==0)
					n++;
				fl[s[i]-'a'+10]=1;
			}
		}
		int cnt=3;
		bool sta=0;
		for(int i=0;i<s.size();++i)
		{
			if(i==0)
				my[s[i]]=2;
			else if(sta==0&&i!=0&&s[i]!=s[0])
			{
				my[s[i]]=1;
				sta=1;
			}
			else
			{
				if(my[s[i]]==0)
					my[s[i]]=cnt++;
			}
		}
		long long ans=0;
		string res="";
		for(int i=0;i<s.size();++i)
			res+=my[s[i]]-1+'0';
		long long jz=my.size();
		if(jz==1)
			jz=2;
		long long tt=1;
		for(int i=res.size()-1;i>=0;--i)
		{
			ans+=(res[i]-'0')*tt;
			tt*=jz;
		}
		printf("Case #%d: ",kk);
		printf("%lld\n",ans);

	}
	return 0;
}