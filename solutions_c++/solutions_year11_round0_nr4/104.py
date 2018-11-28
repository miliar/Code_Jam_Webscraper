#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main(int argc, char* argv[]) {
	ifstream f;
	f.open(argv[1]);
	int T;
	f >> T;
	for (int i=0; i<T; i++) {
		int N;
		f >> N;
		int x;
		int s = 0;
		for (int j=1; j<=N; j++) {
			f >> x;
			s += (x == j);
		}
		cout << "Case #" << i+1 << ": ";
		cout << setprecision(6) << fixed << static_cast<float>(N-s);
		cout << endl; 
	}
	f.close();
}
