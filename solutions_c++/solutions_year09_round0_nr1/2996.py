#include <iostream>
#include <string>
#include <set>
#include <vector>

using std::endl;
using std::cin;
using std::cout;

using std::string;
using std::set;
using std::vector;

int L,D,N;

int main()
{

	cin>>L>>D>>N;

	vector<string> language(D);
	set<char>  cs[15];
	int i,j,k,t;
	string s;

	for(i=0;i<D;i++)
		cin>>language[i];

	for(i=1;i<=N;i++)
	{
		cin>>s;
		for(t=0,j=0;j<s.size();j++,t++)
		{
			if(s[j]=='(')
			{
				for(k=j+1;s[k]!=')';k++)
					cs[t].insert(s[k]);
				j=k;
			}
			else
			{
				cs[t].insert(s[j]);
			}
		}


		for(t=0,j=0;j<D;j++)
		{
			for(k=0;k<L;k++)
				if(cs[k].count(language[j][k])!=1)
					break;
			if(k==L)
				t++;
		    
		}

		cout<<"Case #"<<i<<": "<<t<<endl;

		for(j=0;j<L;j++)
			cs[j].clear();
	}
	return 0;
}

