#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <sstream>
using namespace std;

int main() {
	fstream fin("C-small-attempt0.in");
	//ifstream fin("test.in");
	ofstream fout("output2.txt");
	int T, N, C[1000];
	fin >> T;
	for(int i = 0; i < T; i++) {
		fin >> N;
		for(int j = 0; j < N; j++)
			fin >> C[j];
		bool solved = false;
		sort(C, C + N);
		/*for(int j = 0; j < N; j++)
			fout << C[j] << " ";
		fout << endl;
		*/int mx = 0, mxpt = 0;
		for(int k = 0; k < 1 << N; k++) {
			int sean = 0, patrick = 0, sum = 0, pat = 0;
			for(int p = 0; p < N; p++)
				if(k & (1 << p)) {
					//fout << k << endl;
					sean ^= C[N - p - 1];
					sum += C[N - p - 1];
				}
				else {
					patrick ^= C[N - p - 1];
					pat += C[N - p - 1];
				}
			//fout << sean << " " << patrick << endl;
			//fout << sum << " " << pat << " " << sean << " " << patrick << endl;
			if(sean == patrick && sum > mx && pat > 0 && sum > 0) {
				mx = sum;
				mxpt = pat;
				solved = true;
				//break;
			}
		}
		if(!solved)
			fout << "Case #" << i + 1 << ": NO" << endl;
		else
			fout << "Case #" << i + 1 << ": " << mx << endl;
	}
	fin.close();
	fout.close();
	return 0;
}