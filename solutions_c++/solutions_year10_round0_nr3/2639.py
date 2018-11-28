#include<fstream>
#include<iostream>
#include<string>
using namespace std;
int main()
{
int i,r,k,n,a[100],j,s=0,t=0,b[100],c=0,m=0,g;
ifstream fin("C-small-attempt0.in");
ofstream fout("output.in");
fin>>g;
while(g>0)
{
	g--;	
	m++;
	c=0;
	fin>>r>>k>>n;
	for(i=0;i<n;i++)
		fin>>a[i];
	for(i=0;i<r;i++)
	{
		t=0;
		s=0;
		while(s<k && t<n)
		{
			s=s+a[t];
			b[t]=a[t];
			t++;
			if(s+a[t]>k)
				break;
		}
		if(t!=n)
		{
			for(j=0;j<n-t;j++)
				a[j]=a[j+t];
			for(j=0;j<t;j++)
				a[j+n-t]=b[j];
		}
		c=s+c;
	}
	fout<<"Case #"<<m<<": "<<c<<"\n";
}
return 0;
}
