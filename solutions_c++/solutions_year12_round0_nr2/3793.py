#include <fstream>
#include <algorithm>
using namespace std;

int sum(int n[3]){
	return (n[0] + n[1] + n[2]);
}

int compare(const void* a, const void* b){
	return ((*(int*)b) - (*(int*)a));
}

struct trip{
	int s[3];
};

int main(int argc, char ** argv){
	ifstream inFile;
	inFile.open(argv[1]);

	ofstream outFile;
	outFile.open(argv[2]);


	int numCases;
	inFile >> numCases;
	
	int N, S, p; //numGooglers, numSpecial, Goal score
	for(int i = 1; i <= numCases; i++){
		int totalSatisfied = 0;
		inFile >> N >> S >> p;
		trip* trips = new trip[N];
		for (int n = 0; n < N; n++){
			//for each googler
			
			for (int k = 0; k < 3; k++){
				trips[n].s[k] = 10; //initialise all scores to 10
			}	

			int totalScore = 0;
			inFile >> totalScore;
			while (sum(trips[n].s) > totalScore){ //maximise the scores
				static int k = 0;
				trips[n].s[k]--; 
				k++;
				if (k == 3) k = 0;
			}
			qsort(trips[n].s, 3, sizeof(int), compare);
			if (S > 0){
				if (trips[n].s[0] == (p - 1)){
					//if the score is less than the goal and we have some specials left.
					if (-2 < (trips[n].s[0]+1) - (trips[n].s[1]-1) < 2){
						if (trips[n].s[0] < 10 && trips[n].s[1] > 0) {
							trips[n].s[0]++;
							trips[n].s[1]--;
							S--;
						}
					}
				}
			}
				
			if (trips[n].s[0] >= p){
				totalSatisfied++;
			}			
			//all 3 should be within 1 point of each other here
		}

		outFile << "Case #" << i << ": " << totalSatisfied << endl;
		

		delete[] trips;

	}
	inFile.close();
	outFile.close();
}
