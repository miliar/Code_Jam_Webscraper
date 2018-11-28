#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	
	const char* filename="A-large.in";
	const char* outputname="A-large.out";
	
	/*
	const char* filename="test.txt";
	const char* outputname="testout.txt";
	*/

	ifstream fin(filename);
	ofstream fout(outputname,ios_base::out);

	int num;
	fin>>num;
	for (int i=0; i<num; i++)
	{
		int n,k;
		fin>>n>>k;
		long r=(1<<n)-1;
		if (k%(r+1)==r)
		{
			fout<<"Case #"<<i+1<<": ON"<<endl;
		}
		else
		{
			fout<<"Case #"<<i+1<<": OFF"<<endl;
		}
	}

	fin.close();
	fout.close();

	return 0;
}