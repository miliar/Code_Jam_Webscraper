#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ifstream in("C-large.in");
	ofstream out("result.out");

	int T;
	in >> T;
	for(int i = 1; i <= T; i++){
		int N;
		in >> N;
		int small = 10000000;
		int total = 0;
		int sum = 0;
		for(int j = 0; j < N; j++){
			int v;
			in >> v;
			total = total ^ v;
			sum += v;
			if(v < small){
				small = v;
			}
		}
		if(total == 0){
			out << "Case #" << i << ": " << (sum-small) << endl;
		}else{
			out << "Case #" << i << ": NO" << endl;
		}
		
	
	}

	return 0;
}
