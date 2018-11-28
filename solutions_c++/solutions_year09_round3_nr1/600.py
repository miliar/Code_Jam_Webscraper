#include <iostream>
#include <cstring>
#include <cctype>
#include <map>
using namespace std;

long long powEX(int x,int p)
{
	long long res = 1;
	for(int i=0;i<p;++i)
		res *= x;
	return res;
}
long long bf(string& str,int base_int)
{
	long long res = 0;
	for(int i=0;i<str.size();++i)
	{
		res += (str[i] - '0') * powEX(base_int,str.size() - i - 1);
	}
	return res;
}
int main(int argc, char *argv[])
{
	FILE* ifp = freopen("A-large.in","r",stdin);
	//FILE* ifp = freopen("A.in","r",stdin);
	FILE* ofp = freopen("A-large.out","w",stdout);
		
/*
	string sstr = "10213444";
	for(int i=2;i<=30;++i)
	{
		cout<<bf(sstr,i)<< ' '<<i<<endl;
	}*/
	int T;
	string str;
	int cc;
	bool f = false;
	long long res;
	cin>>T;
	for(int i=0;i<T;++i)
	{
		cin>>str;
		map<char,int> mp;
		//if(isalpha(str[0]))
		{
			mp[str[0]] = ('0' + 1);
			str[0] = ('0' + 1);
			f = true;
		}
		cc = 0;
		for(int j=1;j<str.size();++j)
		{
			//if(isalpha(str[j]))
			{
				if(mp.count(str[j]))
					str[j] = mp[str[j]];
				else
				{
					if(cc == 1 && f)
						++cc;
					mp[str[j]] = ('0' + cc);
					str[j] = ('0' + cc);
					++cc;
				}
			}
		}
		cc = str[0];
		for(int j=1;j<str.size();++j)
		if(cc < str[j])cc = str[j];
		cc = (cc - '0' +1);
		res = bf(str,cc);
		//cout<<str<<' '<<cc<<endl;
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}
	return 0;
}
