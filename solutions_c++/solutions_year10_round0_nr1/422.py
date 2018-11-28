#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int cases=1;
	ifstream fin("input.txt");
	int n;
	fin >> n;
	long long a[35]={0};
	a[0]=1;
	for(int i=1;i<=30;i++)
	{
		a[i]=a[i-1]*2;
	}
	ofstream fout("output.txt");
	for(cases=1;cases<=n;cases++)
	{
		int nr;
		long long k;
		fin >> nr >> k;
		k=k%a[nr];
		if (k==a[nr]-1)
			fout << "Case #" << cases << ": ON" <<endl;
			else
			fout << "Case #" << cases << ": OFF" <<endl;
	}
	return 0;	
}