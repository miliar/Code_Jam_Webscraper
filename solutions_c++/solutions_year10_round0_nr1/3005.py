#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream fin;
	fin.open("C:\\data\\A.in");
	ofstream fout;
	fout.open("C:\\data\\A.out");

	int n;
	fin>>n;
	for(int i=1;i<=n;++i)
	{
		fout<<"Case #"<<i<<": ";
		int N,K;
		fin>>N>>K;
		if(K==0)
		{
			fout<<"OFF"<<endl;
			continue;
		}
		int K1=K%(1<<N);
		K1++;
		N=1<<N;
		if(K1!=N)
			fout<<"OFF";
		else
			fout<<"ON";
		fout<<endl;
	}
	return 0;
}