#include <iostream>
#include <fstream>
using namespace std;

int n,k;

int main()
{
	int i,j,t,period,flag;

	ifstream fin("input.txt");
	ofstream fout("output.txt");

	fin>>t;

	for(i=1;i<=t;i++)
	{
		fin>>n>>k;
		
		flag=true;
		
		for(j=0;j<n;j++)
			if((k%(1<<(j+1)))<(1<<j))
			{
				flag=false;
				break;
			}

		fout<<"Case #"<<i<<": ";
		
		if(!flag)
			fout<<"OFF\n";
		else
			fout<<"ON\n";

	}
	
	fin.close();
	fout.close();

	return 0;
}