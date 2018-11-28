#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char** argv) {
	fstream in;
	fstream out;

    in.open(argv[1], ios::in);
	out.open(argv[2], ios::out);

	int T, N;
	int X, XOR, ADD, S;

    in >> T;
	
	for(int i=1; i<=T; i++) {
		in >> N;

		XOR = 0;
		ADD = 0;
		S = 10000000;

		for(int j=0; j<N; j++) {
			in >> X;
			XOR ^= X;
			ADD += X;
			if(X < S) S = X;
		}

		out << "Case #" << i << ": ";
		if(XOR == 0) out << ADD-S << endl; else out << "NO" << endl;
	}

    in.close();
	out.close();
}