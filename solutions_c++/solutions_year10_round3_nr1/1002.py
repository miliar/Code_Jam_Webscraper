#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <cassert>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[])
{
	ifstream InputFile("A-large.in");
	ofstream OutputFile("A.out");

	int T;
	InputFile >> T;

	for (int i=0; i<T; ++i)
	{
		int N;
		InputFile >> N;

		vector< pair<int, int> > wires;

		for (int n=0; n<N; ++n)
		{
			int A, B;
			InputFile >> A >> B;
			wires.push_back(pair<int, int>(A, B));
		}

		int y=0;

		for (int n=0; n<N; ++n)
		{
			for (int m=n+1; m<N; ++m)
			{
				if ((wires[n].first > wires[m].first && wires[n].second < wires[m].second)
					|| (wires[n].first < wires[m].first && wires[n].second > wires[m].second))
				{
					++y;
				}
			}
		}

		OutputFile << "Case #" << i+1 << ": " << y << endl;
		cout << "Case #" << i+1 << ": " << y << endl;
	}

	return 0;
}

