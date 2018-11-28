#include <fstream>
#include <iostream>
#include <cstdlib>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("a.out");

int main()
{
	int T;
	int N, K;
	int two[31];
	two[0] = 1;
	for (int i=1; i<31; i++) two[i] = two[i-1] * 2;
	fin >> T;
	int cases = 0;
	while (T--)
	{
		fin >> N >> K;
		bool ison = false;
		if ((K+1)%two[N] == 0) ison =  true;
		fout << "Case #" << ++cases << ": " << (ison?"ON":"OFF") << endl;
	}
	return 0;
}