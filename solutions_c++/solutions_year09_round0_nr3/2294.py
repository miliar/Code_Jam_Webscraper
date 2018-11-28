#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
using namespace std;
int N;
string pattern("welcome to code jam");
int main()
{
	string tmp;
	cin>>N;
	getline(cin,tmp);

	for(int i=0;i<N;i++)
	{
		getline(cin,tmp);
		vector <int> p;
		p.resize(tmp.size(),0);
		for(int j=0;j<pattern.size();j++)
		{
			int s=0;
			for(int k=0;k<tmp.size();k++)
			{
				s+=p[k]%10000;
				p[k]=0;
				if(tmp[k]==pattern[j])
					if(j!=0)
						p[k]=s;
					else p[k]=1;
			}
			
		}
		int s=0;
		for(int j=0;j<tmp.size();j++) s+=p[j]%10000;
		s%=10000;
		printf("Case #%d: %0*4d\n",i+1,s);
//		cout<<"Case #"<<i+1<<": "<<s<<endl;
		
		
	}
	
	return 0;
}

