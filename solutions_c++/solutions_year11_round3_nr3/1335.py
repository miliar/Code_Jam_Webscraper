#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");

	int T;
	fin >> T;

	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		int N, L, H;
		fin >> N >> L >> H;

		vector<int> freqs(N);
		for (int i = 0; i < N; i++)
			fin >> freqs[i];

		int note;
		for (note = L; note <= H; note++)
		{
			int i;
			for (i = 0; i < N; i++)
				if ( (note >= freqs[i] && note % freqs[i] != 0) || (note < freqs[i] && freqs[i] % note != 0) )
					break;
			if (i == N)
				break;
		}

		fout << "Case #" << nTestCase << ": ";
		if (note <= H)
			fout << note;
		else
			fout << "NO";
		fout << endl;
	}
}
