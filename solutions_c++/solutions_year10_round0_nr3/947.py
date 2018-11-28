#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <sstream>
#include <queue>

using namespace std;

int main(int argc, char *argv[]){
	if (argc != 2){
		cerr << "Error: " << argv[0] << " file" << endl;
		exit(-1);
	}
	ifstream file(argv[1]);
	if (!file.is_open()){
		cerr << "Error: file " << argv[0] << " could not be opened" << endl;
	}
	int T;
	file >> T;
	for (int i = 0; i < T; i++){
		long long R, K, N;
		file >> R >> K >> N;
		queue<long> groups;
		for (int j = 0; j < N; j++){
			long g;
			file >> g;
			groups.push(g);
		}
		int currentR = 0;
		long totalGroupsTravelled = 0;
		long totalOccupants = 0;
		while(currentR < R){
			currentR++;
			int currentOccupants = 0;
			int currentGroups = 0;
			while((currentOccupants + groups.front() <= K) && (currentGroups < N)){
				currentGroups++;
				currentOccupants += groups.front();
				groups.push(groups.front());
				groups.pop();
				totalGroupsTravelled++;	
			}
			totalOccupants += currentOccupants;
			if (totalGroupsTravelled % N == 0){
				totalOccupants *= (R / currentR);
				currentR *= (R / currentR);
			} 
		}
		cout << "Case #" << (i+1) << ": " << totalOccupants << endl;
	}

	file.close();
}
