#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]) {
	ifstream f;
	f.open(argv[1]);
	int T;
	f >> T;
	for (int i=0; i<T; i++) {
		int N;
		f >> N;
		int* C = new int [N];
		for (int j=0; j<N; j++) f >> C[j];

		bool s = true;
		for (int j=0; j<31; j++) {
			int x = 0;
			int m = (1<<j);
			for (int k=0; k<N; k++) {
				x += ((C[k]&m)>>j);
			}
			if (x%2!=0)  { s = false; break; }
		}
		cout << "Case #" << i+1 << ": ";
		if (s == false) { cout << "NO"; }
		else {
			int min = C[0];
			int sum = C[0];
			for (int j=1; j<N; j++) {
				sum += C[j];
				if (C[j] < min) { min = C[j]; }
			}
			sum -= min;
			cout << sum;
		}
		cout << endl; 
		delete[] C;
	}
	f.close();
}
