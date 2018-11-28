#include "iostream"
#include "fstream"
#include <vector>
#include <string>
using namespace std;


void main()
{
	ifstream fin;
	ofstream fout;
	int T;	//number of testcases

	fin.open("A-large.in", ios_base::in);
	fout.open("A-large.out", ios_base::out);

	fin>>T;

	for(int i=1; i<=T; i++)
	{
		int N;
		unsigned long K;

		fout<<"Case #"<<i<<": ";

		fin>>N;
		fin>>K;
		
		if(K==0)
		{
			fout<<"OFF";
		}
		else
		{
			unsigned long tmp = 2<<(N-1);

			if((K+1)%tmp == 0)
			{
				fout<<"ON";
			}
			else
				fout<<"OFF";
		}
		

		if(i<T)
			fout<<endl;
	}

	fin.close();
	fout.close();
}