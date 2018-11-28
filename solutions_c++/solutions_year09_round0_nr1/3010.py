#include<iostream>
#include<string>
#include<algorithm>
#include<list>
#include<set>
#include<stack>
using namespace std;

typedef unsigned long ulong;
typedef unsigned int uint;

bool matchwords(string& a, string& b)
{
	for(int i=0; i<a.length(); ++i)
	{
		bool p=false;
		bool pmatch=false;

		for(int j=0; j<b.length();)
		{
			if(b[j]=='('){++j;p=true;continue;}
			if(b[j]==')'){++j;++i;p=false;continue;}

			if(p)
			{
				// try and find a match in parenthesis
				while(j<b.length() && b[j] != ')')
				{
					if(b[j]==a[i])
						{pmatch=true;}
					++j;
				}
				if(!pmatch) return false;
				pmatch=false;
			}
			else
			{
				// just check chars
				if(b[j]!=a[i]) return false;
				++j;
				++i;
			}
		}
	}
	return true;
}

int main()
{
	int L,D,N;
	cin>>L>>D>>N;

	list<string> dict;
	for(int i=0;i<D;++i)
	{
		string w;
		cin>>w;
		dict.push_back(w);
	}

	for(int ca=0;ca<N;++ca)
	{
		string w;
		cin>>w;

		list<string> td=dict;

		for(list<string>::iterator it=td.begin(); it!=td.end();)
		{
			if(!matchwords(*it, w))
				it=td.erase(it);
			else
				++it;
		}

		cout << "Case #" << ca+1 << ": " << td.size() << endl;
	}

	return 1;
}