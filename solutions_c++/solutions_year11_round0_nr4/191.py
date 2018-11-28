#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char * argv[]){

	if (argc < 2){
		cout <<"Enter input";
		return 0;
	}

	ifstream input(argv[1]);
	int problem_count;
	input >> problem_count;

	for (int p = 1; p <= problem_count; p++){
		int count = 0;
		int n;
		input >> n;
		for(int i = 1; i <= n; i++) {
			int t;
			input >> t;
			if ( t != i )
				count++;
		}


		cout << "Case #" << p <<": "<< count <<".000000\n";
	}

	input.close();
	return 0;
}


