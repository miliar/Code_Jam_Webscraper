#include<vector>
#include<string>
#include<iostream>
#include<sstream>
#include<algorithm>
#include<math.h>
#include<complex>
#include <fstream>

using namespace std;

void main()
{
	ifstream ff("datos.txt");
	ofstream re("res.txt");
	int n,i,x,y,nn,m,t,j,d[10],cu,k,mi,cc,mm;
	bool c,imp,todos;
	ff>>cc;
	int sab[100][100];
	int gustos[100];
	vector<complex<int> > v;
	for(nn=0;nn<cc;nn++)
	{
		for(i=0;i<100;i++)for(j=0;j<100;j++)sab[i][j]=-1;
		for(i=0;i<100;i++) gustos[i]=0;
		ff>>n;
		ff>>m;
		for(i=0;i<m;i++)
		{
			ff>>t;
			gustos[i]=t;
			for(j=0;j<t;j++)
			{
				ff>>x>>y;
				sab[i][x-1]=y;
			}
		}
		mm=1000;mi=-1;
		for(i=0;i<=(int)(pow(2,n));i++)
		{
			x=i;j=0;cu=0;
			for(k=0;k<10;k++)d[k]=0;
			while(x!=0){if(x%2==1)cu++;d[j]=x%2;j++;x=x/2;}
			todos=true;
			for(j=0;j<m;j++)
			{
				c=false;
				for(k=0;k<n;k++) 
					if(sab[j][k]==d[k])c=true;
				if(!c)todos=false;
			}
			if(todos && cu<mm) {mm=cu;mi=i;}
		}
		if(mi==-1) re <<"Case #"<<nn+1<<": "<< "IMPOSSIBLE"<<endl;
		else
		{
			re <<"Case #"<<nn+1<<": ";
			x=mi;j=0;cu=0;
			for(k=0;k<10;k++)d[k]=0;
			while(x!=0){if(x%2==1)cu++;d[j]=x%2;j++;x=x/2;}
			for(k=0;k<n;k++) re<<d[k]<<" ";
			re<<endl;
		}
	}
}


/*void main()
{
	ifstream ff("datos.txt");
	ofstream re("res.txt");
	int n,i,x,y,c,nn,m,t,j,p,q,a,b,c,d;
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
}*/