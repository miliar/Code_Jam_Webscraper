#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char ** argv) {
	ifstream input(argv[1]);
	ofstream out("output.out");
	int noIn;
	string s;

	input >> noIn;
	getline(input, s);

	for(int i = 1; i <= noIn; i++) {
		out << "Case #" << i << ": ";
		int N, S, p;
		input >> N >> S >> p;

		int guaranteed = 0, contingent = 0;
		int gLimit = (p >= 1 ? 3*p-2 : 0), cLimit = (p >= 2 ? 3*p-4 : 1);

		for(int j = 0; j < N; j++) {
			int t;
			input >> t;
			if(t >= gLimit) guaranteed++;
			else if(t >= cLimit) contingent++;
		}
		int a = guaranteed + (contingent < S ? contingent : S);
		cout << a << endl;
		out << a << endl;
	}

}
