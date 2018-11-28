#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int N, K, T;
	ifstream fin("a.in");
	ofstream fout("a.out");
	fin>>T;
	for(int t=0;t<T;t++)
	{
		fin>>N>>K;
		bool res = true;
		for(int j=N-1;j>=0;j--)
		{
			res = res && ((K>>j) % 2 == 1);
		}
		fout<<"Case #"<<(t+1)<<": "<<( res ? "ON" : "OFF")<<"\n";
	}
	return 0;
}
