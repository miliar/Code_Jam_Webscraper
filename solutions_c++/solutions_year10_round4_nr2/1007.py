#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
	int t;
	ofstream fout("D:\\out");
	ifstream fin("D:\\in");
	fin >> t;
	int two[] = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048};
	for (int testcase = 0; testcase < t; ++testcase) {
		int p;
		fin >> p;
		int minmatch[1050];
		for (int i = 0; i < two[p]; ++i) {
			fin >> minmatch[i];
			minmatch[i] = p - minmatch[i];
		}

		for (int i = 0; i < p; ++i) {
			for (int j = 0; j < two[p - 1 - i]; ++j) {
				int temp;
				fin >> temp;
			}
		}

		int result = 0, step = two[p];
		while (step > 1) {
			int ptr = 0;
			for (int i = 0; i < two[p] / step; ++i) {
				bool watch = false;
				for (int j = i * step; j < (i + 1) * step; ++j) {
					if (minmatch[j] > 0) {
						watch = true;
						break;
					}
				}

				if (watch) {
					++result;
					for (int j = i * step; j < (i + 1) * step; ++j) {
						if (minmatch[j] > 0) {
							--minmatch[j];
						}
					}
				}
			}
			step /= 2;
		}
		fout << "Case #" << testcase + 1 << ": " << result << endl;
	}

	return 0;
}

