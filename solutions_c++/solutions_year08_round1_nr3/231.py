#include<vector>
#include<string>
#include<iostream>
#include<sstream>
#include<algorithm>
#include<math.h>
#include<complex>
#include <fstream>

using namespace std;

/*void main()
{
	ifstream ff("datos.txt");
	ofstream re("res.txt");
	int n,i,x,y,c,nn,m,t,j;
	ff>>c;
	vector< vector<complex<int> > > con;
	vector<complex<int> > v;
	for(nn=0;nn<c;nn++)
	{
		con.clear();
		ff>>n;
		ff>>m;
		for(i=0;i<m;i++)
		{
			v.clear();
			ff>>t;
			for(j=0;j<t;j++)
			{
				ff>>x>>y;
				v.push_back(complex<int> (x,y));
			}
			con.push_back(v);
		}
		
		re <<"Case #"<<nn+1<<": "<< x<<endl;
	}
}*/


void main()
{
	ifstream ff("datos.txt");
	ofstream re("res.txt");
	int n,i,x,y,c,nn,m,t,j,p,q;
	ff>>c;
	vector< vector<complex<int> > > con;
	vector<complex<int> > v;
	for(nn=0;nn<c;nn++)
	{
		ff>>n;
		p=x=1;q=y=0;
		for(i=0;i<n;i++)
		{
			x=(3*p+5*q)%1000;
			y=(p+3*q)%1000;
			p=x;q=y;
		}
		m=(2*x+999)%1000;
		re <<"Case #"<<nn+1<<": ";
		if(m<10) re <<"00";
		if(m>=10 &&m<100) re <<"0";
		re <<m<<endl;
	}
}