#include<string>
#include<fstream>
#include<cstdlib>
using namespace std;

int main()
{
	int map[26]={24,7,4,18,14,2,21,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,16};

	string s;
	int t;
	ifstream in("A.in");
	ofstream out("A.out");

	getline(in,s);
	t=atoi(s.c_str());
	
	for(int i=0;i<t;++i)
	{
		getline(in,s);
		int sz=s.size();
		out<<"Case #"<<i+1<<": ";
		for(int j=0;j<sz;++j)
		{
			if(s[j]!=' ')
			{
				char c='a'+map[s[j]-'a'];
				out<<c;
			}
			else
				out<<' ';
		}
		out<<"\n";
	}
	in.close();
	out.close();
}

		