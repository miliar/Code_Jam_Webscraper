#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin("large1.txt");
	ofstream fout("out.txt");
	int t,i;
	fin>>t;
	for(i=1;i<t;++i)
	{
		int n,k;
		fin>>n>>k;
		if((k&((1<<(n))-1))==((1<<(n))-1))fout<<"Case #"<<i<<": ON"<<endl;
		else fout<<"Case #"<<i<<": OFF"<<endl;
	}
	int a,b;
	fin>>a>>b;
	if((b&((1<<(a))-1))==((1<<(a))-1))fout<<"Case #"<<i<<": ON";
	else fout<<"Case #"<<i<<": OFF";
	return 0;
}

