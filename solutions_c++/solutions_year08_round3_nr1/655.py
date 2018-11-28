#include <fstream>
//#include <iostream>
//#include <string>
#include <vector>
#include <algorithm>
//#include <map>
using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");

bool bigger(int a, int b)
{
	return a > b;
}

int main()
{
	int N;
	fin >> N;

	for (int n=1; n<=N; n++)
	{
		int P, K, L;
		fin >> P >> K >> L;

		vector<int> freqs;
		for (int i=0; i<L; i++)
		{
			int frq;
			fin >> frq;
			freqs.push_back(frq);
		}
		sort(freqs.begin(), freqs.end(), bigger);

		int presses = 0;

		for (int i=0; i<freqs.size(); i++)
		{
			presses += freqs[i] * (int)((i / K) + 1);
		}

		fout << "Case #" << n << ": " << presses << endl;

	}

	return 0;
}