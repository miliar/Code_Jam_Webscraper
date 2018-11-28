#include <iostream>
#include <sstream>
#include <string>
#include <map>

using namespace std;

string i2s( int n )
{
	ostringstream result;
	result << n;
	return result.str();
}

int s2i( const std::string& s )
{
	int result;
	istringstream ss( s );
	ss >> result;
	return result;
}

int main()
{
	int t,i;
	cin>>t;

	for(i=0; i<t; i++)
	{
		int a,b,j;
		int c = 0;
		cin>>a;
		cin>>b;

		for(j=a;j<b;j++)
		{
			int k;
			string s,s2;
			map<int,bool> e;
			s = i2s(j);
			s2 = s;
			for (k=0; k<(signed)(s.length()-1); k++)
			{
				int h;
				s2 = s2.substr(1)+s2[0];
				h = s2i(s2);
				if(h>j && h<=b && e.find(h) == e.end())
				{
//					cout<<j<<" "<<h<<endl;
					e[h]=true;
					c++;
				}

			}
		}

		cout<<"Case #"<<i+1<<": "<<c<<endl;
	}

	return 0;
}
