#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char** argv) {
	fstream in;
	fstream out;

    in.open(argv[1], ios::in);
	out.open(argv[2], ios::out);

	int T, N;
	int SO, SB, S, P;
	char LR, R;
	int LO, LB;

    in >> T;
	
	for(int i=1; i<=T; i++) {
		S = SO = SB = 0;
		LO = LB = 1;
		LR = 0;
		
		in >> N;

		for(int j=0; j<N; j++) {
			in >> R >> P;

			if(LR != R) {
				S += SO + SB;
			}

			if(R == 79) {
				SB += max(abs(LO - P) - SO, 0) + 1;
				SO = 0;
				LO = P;
			} else {
				SO += max(abs(LB - P) - SB, 0) + 1;
				SB = 0;
				LB = P;
			}

			LR = R;
		}

		out << "Case #" << i << ": " << S + SB + SO << endl;
	}

    in.close();
	out.close();
}