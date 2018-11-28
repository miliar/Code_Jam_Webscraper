#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int N;
	fin>>N;
	for(int i = 1;i<=N;++i)
	{
		int a;
		fin>>a;
		_int64 b;
		fin>>b;
		_int64 c = 1<<a;
		fout<<"Case #";
		fout<<i;
		fout<<": ";
		if((b+1)%c == 0)
		{
			fout<<"ON"<<endl;;
		}
		else
		{
			fout<<"OFF"<<endl;
		}
	}
	return 0;
}