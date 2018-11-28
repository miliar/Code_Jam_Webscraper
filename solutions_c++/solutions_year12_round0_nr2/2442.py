#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <map>

using namespace std;

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int main (int argc, char * argv[]) {
    ifstream is(&argv[1][0]);
    string line;
    int cases;
    multimap<int,pair<int*,bool> > scoreCombinations;	//2 combinations per each TOTAL, only total 0 and 1 has a single combination
    multimap<int,pair<int*,bool> >::iterator it;
    for (int i = 0; i <= 10; i++) {
		for (int j = i; j <= i+2; j++) {
			for (int k = j; k <= i+2; k++) {
				int * comb = new int[3];
				comb[0] = i;
				comb[1] = j; 
				comb[2] = k; 
				int total = i+j+k;
				qsort(comb, 3, sizeof(int), compare);
				bool bSurprising = (comb[2] - comb[0] == 2);
				pair<int*,bool> p(&comb[0], bSurprising);
				scoreCombinations.insert(pair<int,pair<int*,bool> >(total, p));
			}
		}
    }
/*
    for (int i = 0; i <= 30; i++) {
	    cout << "total " << i << endl;
	    for (it = scoreCombinations.equal_range(i).first; it != scoreCombinations.equal_range(i).second; ++it) {
		    cout << it->second.first[0] << ", " << it->second.first[1] << ", " << it->second.first[2] << " " << it->second.second << endl; 
	    }
    }
*/    
       if (is.is_open()) {
        if (is.good()) { 
            getline(is, line);
            cases = atoi(line.c_str());
        }
        for (int caseCounter = 0; caseCounter < cases; caseCounter++) {
            getline(is, line, ' ');
			int N = atoi(line.c_str());
            getline(is, line, ' ');
			int S = atoi(line.c_str());
            getline(is, line, ' ');
			int p = atoi(line.c_str());
			pair<int,bool> * scoreFlags = new pair<int,bool>[N]; //flags:  0 == no good, 1 == best, 2 = best surprised, 4 = best not surprised
			int surpr = 0;
			int nosur = 0;
			int match = 0;
			for (int i = 0; i < N; i++) {
					if (i == N-1)
							getline(is, line);
					else
							getline(is, line, ' ');
					int score = atoi(line.c_str());
					scoreFlags[i].first = 0;
					for (it = scoreCombinations.equal_range(score).first; it != scoreCombinations.equal_range(score).second; ++it) {				
						if (it->second.first[2] >= p) {
							scoreFlags[i].first |= 1;
							if (it->second.second)
									scoreFlags[i].first |= 2;
							else
									scoreFlags[i].first |= 4;
						}
					}
					scoreFlags[i].second = false;
					if (scoreFlags[i].first & 1) {
						if(scoreFlags[i].first & 2) {
							if(scoreFlags[i].first & 4) {
								if (surpr == S || nosur == (N-S)) {
									match++;	
									scoreFlags[i].second = true;
									if (surpr == S)
										nosur++;
									else
										surpr++;
								}
							} else if (surpr < S) {
									match++;	
									scoreFlags[i].second = true;
									surpr++;
							}
						} else if(scoreFlags[i].first & 4) {
							if (nosur < N-S) {
									match++;	
									scoreFlags[i].second = true;
									nosur++;
							}
						}
					}
			}
			for (int i = 0; i < N; i++) {
				if (!scoreFlags[i].second && (scoreFlags[i].first & 2) && (scoreFlags[i].first & 4))
					match++;				
			}
            cout << "Case #" << caseCounter+1 << ": " << match << endl;
			delete [] scoreFlags;
        }
		scoreCombinations.clear();
        is.close();
        return 0;
    }


    return -1;    
}
