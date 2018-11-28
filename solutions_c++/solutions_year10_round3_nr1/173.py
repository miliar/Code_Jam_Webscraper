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


void main()
{
	fin.open("b.in",ios::in);
	fout.open("z.in",ios::out);
	int cases,con;
	int i,j;
	int sum;
	int n;
	int a[1005];
	int b[1005];

	
	fin>>cases;
	rep(con,cases)
	{
		fin>>n;
		rep(i,n)
		{
			fin>>a[i];
			fin>>b[i];
		}
		sum=0;
		rep(i,n)
		{
			rep(j,n)
			{
				if(i==j)
					continue;
				if((((a[i]-a[j])>0)&&((b[i]-b[j])<0))||(((a[i]-a[j])<0)&&((b[i]-b[j])>0)))
					sum++;
			}
		}
		sum=sum/2;
		
		fout<<"Case #"<<con+1<<": "<<sum<<endl;
	}
	return;
}