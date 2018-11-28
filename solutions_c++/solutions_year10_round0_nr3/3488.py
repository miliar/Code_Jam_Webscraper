#include <string>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char* argv[])
{
	if (argc != 2) {
		cout << "invalid input!" << endl;
		return -1;
	}

	int T;

	ifstream fin(argv[1]);
	ofstream fout("roller.out");
	fin >> T;
	cout << "T=" << T << endl;

	for (int iT = 0; iT < T; iT++) {
		int R, k, N;

		fin >> R;
		fin >> k;
		fin >> N;

		vector<int> g;
		int gi;
		int iN;
		for (iN = 0; iN < N; iN++) {
			fin >> gi;
			g.push_back(gi);
		}

		iN = 0;
		int euro = 0;
		for (int iR = 0; iR < R; iR++) {

			int passenger = 0;
			while ( passenger + g[iN] <= k ) {
				passenger += g[iN];
				iN = (iN+1)%N;
			}
			euro += passenger;
		}

		fout << "Case #";
		fout << iT+1;
		fout << ": ";
		fout << euro;
		fout << endl;
	}

	return 0;
}

