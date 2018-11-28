#include<iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;
string str[10000];
int c;
bool is_equla(string s)
{
	for (int i=0;i<c;++i)
	{
		if (str[i]==s)
		{
			return true;
		}
	}
	return false;
}
int main()
{
	ifstream in("A-large.in");
	ofstream out("out.txt");
	int cases;
	in>>cases;
	int count=1;
	while (cases--)
	{
		c=0;
		out<<"Case #"<<count++<<": ";
		int n,m;
		in>>n>>m;
		string s;
		int i,j;
		for (i=0;i<n;++i)
		{
			in>>s;
			//cout<<s<<endl;
			str[c++]=s;
			//getchar();
		}
		int tot=0;
		for (i=0;i<m;++i)
		{
			in>>s;
			string temp="";
			int slen=s.length();
			for (int j=0;j<slen;++j)
			{
				temp+=s[j];
				if (s[j+1]=='/'&&j!=0)
				{
					if (!is_equla(temp))
					{
						tot++;
						str[c++]=temp;
					}
				}
			}
			if (!is_equla(temp))
			{
				tot++;
				str[c++]=temp;
			}
		}
		out<<tot<<endl;
	}
}