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

typedef _int64 i64;

int f(int k)
{
	int i,m=100;

L:	for(i=2;i<=k;++i)
	{
		if(k%i==0 && m%i==0)
		{
			k/=i,m/=i;
			goto L;
		}
	}

	 return m;
}

string A(i64 n,int d,int g)
{
	if((g==0 && d!=0) || (g==100 && d!=100))
		return "Broken";
	if(d==0)
		return "Possible";

	int k=f(d);
	if(k<=n)
		return "Possible";

	return "Broken";
}

void main()
{
	int i,num,n,d,g;
	string s,ret;
	ifstream fin("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\Google code jam\\A-large\\A-small-attempt0.in");
	ofstream fout("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\Google code jam\\A-large\\A-small.txt");
	
	fin>>s;
	num=atoi(s.c_str());

	for(i=1;i<=num;++i)
	{
		fin>>s;
		n=atoi(s.c_str());
		fin>>s;
		d=atoi(s.c_str());
		fin>>s;
		g=atoi(s.c_str());

		//Case #1: OFF
		char number[100];
		itoa(i,number,10);
		string nn(number);

		ret="Case #"+nn+": "+A(n,d,g);
		fout<<ret<<endl;
	}

	string rr=A(2,100,20);

	cout<<rr<<endl;
}
