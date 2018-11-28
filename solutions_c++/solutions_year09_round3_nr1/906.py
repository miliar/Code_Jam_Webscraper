#include <set>
#include <string>
#include <iostream>
#include <map>

using namespace std;
int main(void)
{
	int T;
	int i,j,k;
	string str;	
	int base;
	long long sum;

    
	set<char> s;
	map<char,int> m;

	cin>>T;

	for(i=1;i<=T;i++)
	{
		cin>>str;

		/*
		for(j=0;j<str.size();j++)
		{
			if(s.count(str[j])==1)
				continue;
			s.insert(str[j]);
		}

		base=s.size();	
		
		if(base==1)
			base=2;
		*/		

		for(j=1,k=0,m[str[0]]=1;j<str.size();j++)
		{
			if(m.count(str[j])==1)
				continue;
			m[str[j]]=k;
			k++;
			if(k==1)
				k=2;
		}

		base=m.size();
		if(base==1)
			base=2;

		sum=0;
		for(j=0;j<str.size();j++)
		{
			sum*=base;
			sum+=m[str[j]];
		}

		cout<<"Case #"<<i<<": "<<sum<<endl;

		m.clear();
		s.clear();
	

	}
    
	return 0;
}
