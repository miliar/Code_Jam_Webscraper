#include <iostream>
#include <fstream>

using namespace std;

int CountFirstOn(int N) {
	if (N > 1) return 2*CountFirstOn(N-1)+1;
	else return 1;
}

int main(int argc, char* argv[])
{
	int T, N, K, L;
	ifstream in("in.txt");
	in >> T;
	for (int i = 0; i < T; i++) {
		in >> N >> K;
		L = CountFirstOn(N);
		cout << N << " " << K << " " << L << endl;
	}
	system("pause>null");
	return 0;
}
//---------------------------------------------------------------------------
