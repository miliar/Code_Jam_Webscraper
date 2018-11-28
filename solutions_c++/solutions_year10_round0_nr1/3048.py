// ==============================================
// ==Author: zerosumi@gmail.com
// ==School: Beijing Institute of Technology
// ==============================================

#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream filein("C:\\Users\\zerosumi\\Project\\tmp\\Debug\\in.txt");
	ofstream fileout("C:\\Users\\zerosumi\\Project\\tmp\\Debug\\out.txt");
	int T, N, K;
	filein >> T;
	static int times[31] = {0,1};
	for (int i = 2; i <= 30; i++) {
		times[i] = times[i - 1] * 2 + 1;
	}
	for (int i = 1; i <= T; i++) {
		filein >> N;
		filein >> K;
		if (K != 0 && (K+1) % (times[N]+1) == 0)
			fileout << "Case #" << i << ": " << "ON" << endl;
		else
			fileout << "Case #" << i << ": " << "OFF" << endl;
	}
	return 0;
} 
