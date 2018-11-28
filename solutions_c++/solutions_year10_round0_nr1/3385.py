#include<fstream>
#include<math.h>
#include<iostream>

using namespace std;
int main()
{
	int n,i;
	unsigned long k,f;
	ifstream fin("jammu1.in");
	ofstream fout("output.out");
	fin>>i;
	int j=0;
    while(i--)
    {
       	fin>>n>>k;
		fout<<"Case #"<<(++j)<<": ";
		f=(unsigned long)pow(2,n);
		if((k+1)%f==0)
			fout<<"ON\n";
		else
			fout<<"OFF\n";
	}
	fin.close();
	fout.close();
	return 0;
}
