#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;
int main(int argc, char ** argv){
	ifstream fin(argv[1]);
	int T;
	fin >> T;
	
	for (int t=0; t!= T; t++){
		int N;
		fin >> N;
		unsigned long long	sum=0,
							xum = 0, 
							minC=1E7;
		for (int n=0; n!=N; n++) {
			unsigned long long C;
			fin >> C;
			sum += C;
			xum ^= C;
			minC = min(minC,C);
		}
		if (xum != 0 ) {
			cout << "Case #" << t+1 << ": NO" << endl;
		} else {
			cout << "Case #" << t+1 << ": " << sum - minC << endl;
		}

	}
}