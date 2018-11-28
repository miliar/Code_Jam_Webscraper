#include <iostream>
#include <fstream>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;

ifstream fin("C-large.in");
ofstream fout("C-large.out");
typedef long long int ll;

int x[5005];
int y[5005][2];

int main() {
	int T;
	fin >> T;
	for(int i=0; i < T; i++) {
		cout << i << "\n";
		int R, N, K;
		fin >> R >> K >> N;
		for(int j=0; j < N; j++)
			fin >> x[j];
		for(int j=N; j < N+N; j++)
			x[j] = x[j-N];
		for(int j=0; j < N; j++) {
			int s = 0;
			int r = K;
			int k;
			for(k = 0; k < N; k++) {
				r -= x[j+k];
				if(r < 0) break;
				else s += x[j+k];
			}
			y[j][0] = k;
			y[j][1] = s;
		}
		ll s = 0;
		int ind = 0;
		for(int j=0; j < R; j++) {
			s += y[ind][1];
			ind = (ind + y[ind][0]) % N;
		}
		fout << "Case #" << (i + 1) << ": " << s << "\n";
	}
	return 0;
}
