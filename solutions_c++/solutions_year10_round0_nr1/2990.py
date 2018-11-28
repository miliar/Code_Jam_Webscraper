#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ofstream fout ("A-large.out");
    ifstream fin ("A-large.in");
	int T,N,K;
	int P[31];
	P[0]=1;
	for(int i=1;i<31;i++)
		P[i]=P[i-1]*2;
	fin >> T;
	for(int i=0;i<T;i++)
	{
		fin >> N;
		fin >> K;
		if(K==0) fout<<"Case #"<<i+1<<": OFF"<<endl;
		else
		{
			if(K % P[N]==P[N]-1) 
				fout<<"Case #"<<i+1<<": ON"<<endl;
			else 
				fout<<"Case #"<<i+1<<": OFF"<<endl;
		}
	}
	return 0;
}