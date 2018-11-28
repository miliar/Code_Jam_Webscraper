#include <fstream>
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

int main()
{
	int n;
	fin>>n;
	int N, K;
	for(int i=0;i<n;++i)
	{
		fin >> N;
		fin >> K;
		int L = (1 << N);
		fout << "Case #" << i+1 <<": " << ((K % L == L - 1) ? "ON" : "OFF")<<endl;
	}
	return 0;
}
