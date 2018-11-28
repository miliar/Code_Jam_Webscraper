#include <iostream>
#include <fstream>
#include <string>
using namespace std;
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)


ifstream fin;
ofstream fout;



void main()
{
	fin.open("c.in",ios::in);
	fout.open("z.in",ios::out);
	int cases,con;
	int i,j;

	int n,k,b,t;
	int x[50];
	int v[50];
	int a[50];
	int sum;
	int swap;
	int l;
	
	fin>>cases;
	rep(con,cases)
	{
		fin>>n>>k>>b>>t;
		memset(a,0,sizeof(a));
		rep(i,n)
			fin>>x[i];
		rep(i,n)
			fin>>v[i];
		
		rep(i,n)
		{
			if(x[i]+v[i]*t>=b)
				a[i]=1;
		}

		//rep(i,n)
		//{
		//	cout<<a[i];
		//}
		sum=0;
		swap=0;
		rep(i,n)
		{
			sum=sum+a[i];
		}
		if(sum<k)
		{
			fout<<"Case #"<<con+1<<": IMPOSSIBLE"<<endl;
			continue;
		}
		sum=0;
		l=n-1;
		j=n-1;
		while(sum<k)
		{
				while(a[j]==0)
				{
					j--;
				}
				if(l==j)
				{l--;j--;sum++;continue;}

					a[l]=1;
					a[j]=0;
					swap=swap+l-j;
					l--;
					j--;
				sum++;
		}

		fout<<"Case #"<<con+1<<": "<<swap<<endl;	

	}
	return;
}