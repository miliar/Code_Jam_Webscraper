#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<numeric>
#include<cmath>

#include<fstream>

using namespace std;

int A(vector<int> o,vector<int> b,vector<char> s)
{
	int i;
	int ret=0,lo=0,lb=0,difo=0,difb=0;

	if(o.size())
		difo=o[0]-1;
	if(b.size())
		difb=b[0]-1;

	for(i=0;i<s.size();++i)
	{
		if(s[i]=='O')
		{
			ret+=difo+1,++lo;
			if(difb>=difo+1)
				difb-=(difo+1);
			else
				difb=0;
			if(lo<o.size())
				difo=abs(o[lo]-o[lo-1]);
		}
		else
		{
			ret+=difb+1,++lb;
			if(difo>=difb+1)
				difo-=(difb+1);
			else
				difo=0;
			if(lb<b.size())
				difb=abs(b[lb]-b[lb-1]);
		}
	}

	return ret;
}

void main()
{
	int i,j,num,n,k;
	char c;
	string s,ret;
	vector<int> o,b;
	vector<char> vs;
	ifstream fin("D:\\gcj\\A-small\\A-large.in");
	ofstream fout("D:\\gcj\\A-small\\A-large.txt");
	
	fin>>s;
	num=atoi(s.c_str());

	for(i=1;i<=num;++i)
	{
		o.clear(),b.clear(),vs.clear();
		fin>>s;
		n=atoi(s.c_str());

		for(j=1;j<=n;++j)
		{
			fin>>s;
			c=s[0];
			vs.push_back(c);

			fin>>s;
			k=atoi(s.c_str());
			if(c=='O')
				o.push_back(k);
			else
				b.push_back(k);
		}

		//Case #1: OFF
		char number[100];
		itoa(i,number,10);
		string nn(number);

		ret="Case #"+nn+": ";
		int kk=A(o,b,vs);
		fout<<ret<<A(o,b,vs)<<endl;
	}

/*	int ao[]={5,8};
	int ab[]={100};
	char cs[]={'O','O','B'};

	vector<int> o(ao,ao+2);
	vector<int> b(ab,ab+1);
	vector<char> s(cs,cs+3);

	int ret=A(o,b,s);

	cout<<ret<<endl;*/
}
