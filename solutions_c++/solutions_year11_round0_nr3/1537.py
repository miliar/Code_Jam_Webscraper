#include <iostream>
#include <fstream>
using namespace std;

int main (int argc, char * const argv[]) {
    //ifstream in("..//..//sample.in.txt");
	//ifstream in("..//..//C-small-attempt0.in.txt");
	ifstream in("..//..//C-large.in.txt");
	
	if (!in) {
		cout << "Input file cannot be opened";
		return 1;
	}
	
	ofstream out("output.txt");
	if (!out) {
		cout << "Output file cannot be opened";
		in.close();
		return 1;
	}
	
	int T;
	in >> T;
	
	for (int t = 0; t < T; t++) {
		int N;
		in >> N;
		int C[N];
		for (int n = 0; n < N; n++) {
			in >> C[n];
		}
		
		// 2 piles is possible only if exclusive or all values = 0
		int result = 0;
		int sum = 0;
		int smallestValue = 1000001;
		for (int n = 0; n < N; n++) {
			result = result ^ C[n];
			
			if (smallestValue > C[n])
				smallestValue = C[n];
			sum += C[n];
		}
		
		out << "Case #" << (t + 1) << ": ";
		if (result == 0) {
			out << sum - smallestValue;
		}
		else {
			out << "NO";
		}
		out << endl;
	}
	
	in.close();
	out.close();
	
    return 0;
}
