#include <iostream>
#include <string.h>
#include <fstream>
using namespace std;

int main()
{
	ifstream fin("A-large.in.");
	ofstream fout("A-large.out");
	int t,n,k,temp,sum;
   fin>>t;
	for (int i=0;i<t;i++)
	{
		fin>>n>>k;
		temp=1;
		sum=0;
		for (int j=0;j<n;j++)
		{
			sum+=temp;
			temp*=2;
		}		
		if (k%(sum+1)<sum)
			fout<<"Case #"<<i+1<<": OFF"<<endl;
		else
			fout<<"Case #"<<i+1<<": ON"<<endl;

	}
}