#include <iostream>
#include <string>
#include <sstream>
#include <cctype>
#include <fstream>
#include <queue>
#include <deque>
#include <list>
using namespace std;


int Profit(int R,int K, int N, int groups[]) {
	queue<int> coaster;
	queue<int> waiting;
	int passengers = 0;
	int temp=0;
	int value=0;

	for( int i=0; i<N; i++) { // initialize the waiting line
		waiting.push(groups[i]);
	}
	for (int r=0; r<R; r++) {
		while (!waiting.empty()) { // going on roller coaster
			temp = waiting.front();
			if ((passengers + temp) <= K) {
				waiting.pop();
				coaster.push(temp); 
				passengers = passengers + temp;
				value = value + temp;

			}
			else {break;};
		}
		while(!coaster.empty()) { // coming off roller coaster
			temp = coaster.front();
			coaster.pop();
			waiting.push(temp);
			passengers = passengers - temp;
		}
	}
	return value;
}
			

int main(int argc, char *argv[]) {
	ifstream fp_in(argv[1]);
	ofstream fp_out;
	fp_out.open( "output.txt", ios::out);
	int T;
	int R;
	int K;
	int N;
	string line;
	if (fp_in.is_open()) {
		string state;
		getline(fp_in,line);
		istringstream cases(line);
		cases >> T;
		for (int i=0; i< T; i++) {
			getline(fp_in,line);
			istringstream params(line);	// store the parameters of each test case
			params >> R;
			params >> K;
			params >> N;
			int groups[N];
			getline(fp_in,line);	// store the different groups
			istringstream people(line);
			for(int j=0; j<N; j++) {
				people >> groups[j];
			}
			fp_out << "Case #" << i+1 << ": " << Profit(R,K,N,groups) <<"\n";
		}
		fp_out.close();
		fp_in.close();
	}
	return 0;
}
			
			
