#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

int main()
{
	ifstream fin ("A-large.in");
	ofstream fout ("A-large.out");
	int T;
	int ar[30]={2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824};
	fin >> T;
	for (int tt=0;tt<T;tt++)
	{
		int N,K;
		fin >> N >> K;
		int cycle=pow((double)2,(double)N)-1;
		/*
		int cycle=pow((double)2,(double)N)-1;
		if (N==1) fout << "Case #" << tt+1 << ": " << ((K%2==0) ? "OFF" : "ON") << endl;
		else if (K==0) fout << "Case #" << tt+1 << ": OFF" << endl;
		else if (cycle-K==1) fout << "Case #" << tt+1 << ": OFF" << endl;
		else if ((K-(K/cycle-1))%cycle==0) fout << "Case #" << tt+1 << ": ON" << endl;
		else fout << "Case #" << tt+1 << ": OFF" << endl;
		*/
		int x=0;
		if (K==0) fout << "Case #" << tt+1 << ": OFF" << endl;
		else
		{
			for (int i=1;i<=K;i++)
			{
				if (x==cycle) x=0;
				else x+=1;
			}
			if (x==cycle) fout << "Case #" << tt+1 << ": ON" << endl;
			else fout << "Case #" << tt+1 << ": OFF" << endl;
		}
	}
}
