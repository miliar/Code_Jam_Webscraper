#include<iostream>
#include<vector>
#include<string>
#include <fstream>
using namespace std;
vector<string> v;
string str;
int l,d,n,p,c,j,k,i;
bool d1;
char ch;
int main()
{
	ofstream fout ("out.txt");
    ifstream fin ("in.txt");
	fin>>l>>d>>n;
	for (i=0;i<d;i++)
	{
		fin>>str;
		v.push_back(str);
	}
	for (i=1;i<=n;i++)
	{
		bool m[29][18]={0};
		d1=0;
		fin>>str;
		p=0;
		for (j=0;j<str.length();j++)
		{
			ch=str[j];
			if (ch=='(')
			{
				d1=1;
			}
			else if (ch==')')
			{
				d1=0;
				p++;
			}
			else if (d1)
			{
				m[ch-'a'][p]=1;
			}
			else m[ch-'a'][p++]=1;
		}
		if (p!=l)
		{
			fout<<"Case #"<<i<<": 0"<<endl;
			continue;
		}
		c=0;
		for (j=0;j<d;j++)
		{
			for (k=0;k<l;k++)
			{
				if (!m[v[j][k]-'a'][k]) break;
			}
			if (k==l) c++;
		}
		fout<<"Case #"<<i<<": "<<c<<endl;
	}
	v.clear();
	return 0;
}