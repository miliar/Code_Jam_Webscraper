#include <iostream> // AUFGABE A
#include <fstream>

using namespace std;

const problem = 1;

int main(int argc, char** argv) {
	fstream in;
	fstream out;

	switch(problem) {
		case 0:
			in.open("D:\\A-test.in", ios::in);
			out.open("D:\\A-test.out", ios::out);
			break;
		case 1:
			in.open("D:\\A-small.in", ios::in);
			out.open("D:\\A-small.out", ios::out);
			break;
		case 2:
			in.open("D:\\A-large.in", ios::in);
			out.open("D:\\A-large.out", ios::out);
			break;
	}

	int T, N, D, G, X;

    in >> T;
	
	for(int i=1; i<=T; i++) {
		in >> N >> D >> G;
		X = 1;

		if((G == 100 && D != 100) || (G == 0 && D != 0)) {
            out << "Case #" << i << ": Broken" << endl;
		} else {
			if((D % 2) == 0) {
				D = D/2;
				X = X*2;
			}
			if((D % 2) == 0) {
				D = D/2;
				X = X*2;
			}
			if((D % 5) == 0) {
				D = D/5;
				X = X*5;
			}
			if((D % 5) == 0) {
				D = D/5;
				X = X*5;
			}

			if(N >= 100/X)
				out << "Case #" << i << ": Possible" << endl;
			else
				out << "Case #" << i << ": Broken" << endl;
		}

		
	}

    in.close();
	out.close();
}