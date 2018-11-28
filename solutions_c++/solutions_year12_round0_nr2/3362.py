#include <iostream>
using namespace std;

int main() {
	int num_cases;

	cin >> num_cases;

	for( int i = 1; i <= num_cases; i++ ) {
		int numDancers, suprise, bestScore, meet_max, curr_score, max_no_sup;
		cin >> numDancers >> suprise >> bestScore;

		meet_max = max_no_sup = 0;
		// Loop through all the dancers
		for( int j = 0; j < numDancers; j++ ) {
			int diff, avg;
			cin >> curr_score;	

			// Get the min value for all 3 scores
			diff = curr_score % 3;	
			avg = ( curr_score - diff ) / 3;

			if( curr_score == 0 && bestScore != 0 ) {}
			// If the avg is over the min, meet_max true
			else if( avg >= bestScore ) {
				meet_max++;
				max_no_sup++;
			}
			else if( diff == 1 ) {
				// 1 score gets +1
				if( avg + 1 >= bestScore ) {
					meet_max++;
					max_no_sup++;
				}
			}
			else if( diff == 2 ){
				// 2 scores get +1
				if( avg + 1 >= bestScore ) {
					meet_max++;
					max_no_sup++;
				}
				// 1 score gets +2
				else if( avg + 2 >= bestScore && suprise > 0 ) {
					meet_max++;
					suprise--;
				}
			}
			else if( diff == 0 ) {
				// 1 score gets +1, and 1 gets -1
				if( avg + 1 >= bestScore && suprise > 0  && avg > 0 ) {
					meet_max++;
					suprise--;
				}
			}
		}

		// Print result
		cout << "Case #" << i << ": " << meet_max  << endl;
	}
}
