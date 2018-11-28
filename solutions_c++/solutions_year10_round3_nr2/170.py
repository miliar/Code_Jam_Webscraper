#include <iostream>
#include <fstream>
#include <string>
#include <stack>
#include <queue>
using namespace std;
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
ifstream fin;
ofstream fout;

_int64 mi(int c,int n)
{
	int i;
	int zs;
	_int64 jg;
	zs=1;
	jg=1;
	for(i=0;i<n;i++)
	{
		zs=zs*2;
	}
	for(i=0;i<zs;i++)
	{
		jg=jg*c;
	}
	return jg;
}



void main()
{
	fin.open("b.in",ios::in);
	fout.open("zz.in",ios::out);
	int cases,con;
	
	int c;
	_int64 cj,l,p;
	int jg;
	int tm;

		
	fin>>cases;
	rep(con,cases)
	{
		
		cout<<con+1<<endl;
		fin>>l>>p>>c;
		cout<<l<<p<<c<<endl;
		jg=0;
		//cout<<mi(c,2);
		cj=l*mi(c,jg);
		while(cj<p)
		{
			jg++;
			cj=l*mi(c,jg);
			//cout<<jg;
		}
		
		fout<<"Case #"<<con+1<<": "<<jg<<endl;		
	}
	
	return;
}