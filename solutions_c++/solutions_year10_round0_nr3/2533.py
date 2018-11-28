#include <iostream>
#include <fstream>
using namespace std;
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)

void main()
{
	ifstream fin("b.in");
	ofstream fout("z.in");

	int a[1000][4];
	int g[1000];
	int i,j,c,l;
	int ca,r,k,n;
	int sum;
	int len;
	fin>>ca;
	rep(c,ca)
	{
		memset(a,0,sizeof(a));
		memset(g,0,sizeof(g));
		fin>>r>>k>>n;
		rep(i,n)
			fin>>g[i];
		rep(i,n)
		{
			sum=0;
			j=i;
			sum=sum+g[j];
				j++;
				if(j>=n)
					j=0;
			while(sum+g[j]<=k&&i!=j)
			{
				sum=sum+g[j];
				j++;
				if(j>=n)
					j=0;
			}
			a[i][0]=j;
			a[i][1]=sum;
		}
		
		i=1;
		j=0;
		sum=0;
		while(i<=r)
		{
			if(a[j][2]!=0)
				break;
			a[j][2]=i;
			sum=sum+a[j][1];
			rep(l,n)
				if(a[l][2]!=0)
					a[l][3]=a[l][3]+a[j][1];
			j=a[j][0];
			i++;
		}
		if(i>r)
		{
			fout<<"Case "<<c+1<<": "<<sum<<endl;
			continue;
		}
		len=i-a[j][2];
		while(i+len<=r)
		{
			sum=sum+a[j][3];
			i=i+len;			
		}
		while(i<=r)
		{
			sum=sum+a[j][1];
			j=a[j][0];
			i++;
		}
		fout<<"Case "<<c+1<<": "<<sum<<endl;
	}		
	return;
}