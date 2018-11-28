#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

int main()
{
	long long int t,n,k,c,s,m=0;
	ifstream fin("A-large.in");
	ofstream fout("outputlong.in");
	fin>>t;
	while(t--)
	{
		m++;
		fin>>n>>k;
		c=pow(2,n)-1;
		if(k<c)
		{
			fout<<"Case #"<<m<<": "<<"OFF\n";
			continue;
		}
		else
		{
			s=c;
			while(s<k)
			{
				s+=(c+1);
			}
			//cout<<s<<" "<<k;
			if(s==k)
				fout<<"Case #"<<m<<": "<<"ON\n";
			else
				fout<<"Case #"<<m<<": "<<"OFF\n";
			
		}
	}
	return 0;
}
