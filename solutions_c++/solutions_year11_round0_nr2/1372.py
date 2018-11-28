#define _CRT_SECURE_NO_DEPRECATE

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<fstream>
#include<string>
#include<cmath>
#include<algorithm>
#include<string.h>
#include<memory.h>
using namespace std;

ifstream inf("B-large.in");
ofstream outf("out.txt");
#define cin inf
#define cout outf

int m[255][255];
int o[255][255];
int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		memset(m,0,sizeof(m));
		memset(o,0,sizeof(o));

		int c,d,l;
		string s;
		cin>>c;
		for(int i=0;i<c;i++)
		{
			cin>>s;
			m[s[0]][s[1]] = s[2];
			m[s[1]][s[0]] = s[2];
		}
		cin>>d;
		for(int i=0;i<d;i++)
		{
			cin>>s;
			o[s[0]][s[1]] = 1;
			o[s[1]][s[0]] = 1;
		}
		cin>>l;
		cin>>s;
		string ret;
		for(int i=0;i<l;i++)
		{
			if(ret.size() == 0)
			{
				ret += s[i];
				continue;
			}
			char cc = m[s[i]][ret[ret.size()-1]];
			if(cc)
				ret[ret.size()-1] = cc;
			else
			{
				for(int j=0;j<ret.size();j++)
				{
					if(o[s[i]][ret[j]])
					{
						ret.resize(0);
						break;
					}
				}
				if(ret.size())
					ret += s[i];
			}
		}
		string r = "[";
		for(int i=0;i<ret.size();i++)
		{
			r += ret[i];
			r += ", ";
		}
		if(ret.size())
		{
			r[r.size()-2] = ']';
			r.resize(r.size()-1);
		}
		else
			r += ']';
		cout<<"Case #"<<t<<": "<<r<<endl;
	}
}