#pragma warning(disable:4786)
#include<iostream>
#include<string>
#include<sstream>
#include<set>
#include<fstream>
using namespace std;
int main()
{
	string use,imp;
	set<string> engines,replace;
	set<string>::iterator it;
	ifstream cin("1.txt");
	ofstream cout("A-large.txt");
	int N,S,Q,result=0;
	getline(cin,use);
	stringstream ss;
	ss<<use;
	ss>>N;
	int i=0;
	while(i<N)
	{
		i++;
		getline(cin,use);
		stringstream qq;
		qq<<use;
		qq>>S;
		int count=0;
		while(count++<S)
		{
			getline(cin,use);
			engines.insert(use);
		}
		replace=engines;
		getline(cin,use);
		stringstream ww;
		ww<<use;
		ww>>Q;
		count=0;
		while(count<Q)
		{
			getline(cin,use);
			
			if(engines.size()==0)
			{
				result++;
				engines=replace;
				engines.erase(imp);
			}
		    if(engines.count(use))
			{
				engines.erase(use);
				imp=use;
			}
			count++;
		}

		if(engines.size()==0)
			result++;
		cout<<"Case #"<<i<<": "<<result<<endl;
	engines.clear();
	replace.clear();
		result=0;
	}
	return 0;
}






