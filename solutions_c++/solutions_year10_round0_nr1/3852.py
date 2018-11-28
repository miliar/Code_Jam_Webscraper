#include<iostream>
#include<fstream>
#include<cmath>

using namespace std;
int main() 
{
	ifstream fin("D:\\io\\A-large.in",ios::in);
	ofstream fout("D:\\io\\A-large.out");


	__int64 C;
	long double N = 0;
	__int64 K = 0;
        __int64 power;
	fin>>C;
	fin.get();

	for(__int64 i=0;i < C;++i )
	{
	fin>>N>>K;
	power = pow(2,N);
	fout<<"Case #";
        fout<<i+1<<": ";  
	if(!((K+1) % power))
	    fout<<"ON";
	else
            fout<<"OFF";
	fout<<"\n";
	}
	fout.close();
	fin.close();
	return 0;
} 