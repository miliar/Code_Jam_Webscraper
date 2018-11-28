#include<iostream>
#include<vector>
#include<string>
#include<cmath>
using namespace std;


main()
{
	int cases;
	string str;
	vector<int> numb(10,0),cha(26,0);
	cin >> cases;
		
	for(int l=0;l<cases;l++)
	{
		for(int i=0;i<10;i++)numb[i]=0;
		for(int i=0;i<26;i++)cha[i]=0;
		cin >> str;
		
		int len=str.length();
		for(int i=0;i<len;i++)
		{
			if(str[i] >='0' && str[i]<='9')numb[str[i]-'0']=1;
			else if(str[i]>='a' && str[i]<='z')cha[str[i]-'a']=1;
		}
		
		int base=0;
		for(int i=0;i<10;i++)if(numb[i]==1)base++;
		for(int i=0;i<26;i++)if(cha[i]==1)base++;
		
		if(base==1)base++;
		vector<int> seq;
		seq.push_back(1);
		seq.push_back(0);
		for(int i=2;i<base;i++)seq.push_back(i);
		
		for(int i=0;i<10;i++)numb[i]=-1;
		for(int i=0;i<26;i++)cha[i]=-1;

		int cur=0;
		long long int ans=0;
		for(int i=0;i<len;i++)
		{
			if(str[i]>='0' && str[i]<='9')
			{
				if(numb[str[i]-'0']!=-1)
				{
					//ans=ans+ pow(base,len-1-i)*numb[str[i]-'0'];
				}
				else
				{
					numb[str[i]-'0']=seq[cur];
					cur++;
					
				}				
				ans=ans+ pow(base,len-1-i)*numb[str[i]-'0'];
			}
			else
			{
				if(cha[str[i]-'a']!=-1)
				{
					//ans=ans+ pow(base,len-1-i)*cha[str[i]-'a'];
				}
				else
				{
					cha[str[i]-'a']=seq[cur];
					cur++;
					
				}				
				ans=ans+ pow(base,len-1-i)*cha[str[i]-'a'];
			}
		//cout<<ans<<'\n';
		
				
		}
		cout<<"Case #"<<l+1<<": ";
		cout<<ans<<'\n';
	}
}

		
			
			
