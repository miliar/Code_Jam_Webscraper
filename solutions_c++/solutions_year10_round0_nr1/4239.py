#include <string.h>
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
	ofstream fout("out.txt");
	fin >> T;
//	cout << "T=" << T << endl;

	for (int i = 0; i < T; i++) {
		int N, K;
		int ison = 0;
		unsigned long power = 1;
		unsigned long onoff = 0;

		fin >> N;
		fin >> K;
//		cout << "Test #" << i+1 << ": N=" << N << ", K=" << K << endl;

		int j = 0;
		while (j < K) {
			onoff = power^onoff;
			power = (onoff+1)^onoff;
			j++;
		}
//		cout << "onoff=" << onoff << endl;
//		cout << "power=" << power << endl;

		ison = ((power) >> N) & 1;
//		cout << "ison=" << ison << endl;

		fout << "Case #";
		fout << i+1;
		fout << ": ";
		fout << (ison ? "ON" : "OFF");
		fout << endl;
	}

	return 0;
}
