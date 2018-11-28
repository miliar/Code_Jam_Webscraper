#include<fstream>
#include<iostream>
#include<cmath>
using namespace std;
int main()
{
long long int n,k,g=0,s=0,b=0,m=0,w;
ifstream fin("A-large.in");
ofstream fout("output.in");
fin>>w;
while(w>0)
{
	w--;	
	m++;
	s=0;
	b=0;
	fin>>n>>k;
	g=pow(2,n-1);
	while(s<k)
	{
		s=s+g+(g-1);
		if(s==k)
		{
			b++;
			break;
		}
		s++;
		if(s>k)
			break;
	}
	if(b>0)
		fout<<"Case #"<<m<<": ON\n";
	else
		fout<<"Case #"<<m<<": OFF\n";
}
return 0;
}
