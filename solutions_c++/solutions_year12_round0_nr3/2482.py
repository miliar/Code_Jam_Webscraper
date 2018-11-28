#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <map>
#include <math.h>

using namespace std;

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int main (int argc, char * argv[]) {
    ifstream is(&argv[1][0]);
    string line;
    int cases;
/*
//1111-2222
11xy	1xy1	xy11	y11x
1x1y	x1y1	1y1x	y1x1
12xy	2xy1	xy12	y12x
1x2y	x2y1	2y1x	y1x2
22xy	2xy2	xy22	y22x
2x2y	x2y2	2y2x	y2x2
*/
    multimap<int, int> pairs;//int32 for 2 000 000 limit 

    if (is.is_open()) {
	    if (is.good()) { 
		    getline(is, line);
		    cases = atoi(line.c_str());
	    }
		int * slot;
		bool * goodSlot;
		pair<multimap<int,int>::iterator,multimap<int,int>::iterator> ret;
		multimap<int,int>::iterator it,it2;
	    for (int caseCounter = 0; caseCounter < cases; caseCounter++) {
		    getline(is, line, ' ');
		    int A = atoi(line.c_str());
		    getline(is, line);
		    int B = atoi(line.c_str());
			int a = A;
			int digits = 0;
			while (a > 0) {
				a /= 10;
				digits++;
			}
			if (digits == 1) {
					cout << "Case #" << caseCounter+1 << ": " << 0 << endl;
					continue;
			} 
			for (int i = A; i <= B; i++) {
				slot = new int[digits];
				goodSlot = new bool[digits];
				slot[0] = i;
				goodSlot[0] = true;
				for (int j = 1; j < digits; j++) {
					int power = pow(10,digits-j);
					slot[j] = (i % power)*(pow(10,j)) + (i/power);	
					goodSlot[j] = (slot[j] >= A && slot[j] <= B) ? true : false;
				}
				for (int j = 0; j < digits-1; j++) {
					for (int k = j+1; k < digits; k++) {
						if (goodSlot[j] && goodSlot[k] && slot[j] != slot[k]) {
							if (pairs.count(slot[j]) == 0) {
								pairs.insert(pair<int,int>(slot[j], slot[k]));
								pairs.insert(pair<int,int>(slot[k], slot[j]));
							} else {
								bool bInsert = true;
								ret = pairs.equal_range(slot[j]);
								it = ret.first;
								for(; it != ret.second; ++it) {
									if (it->second == slot[k]) {
										bInsert = false;
										break;
									}
								}
								if (bInsert) {
									pairs.insert(it, pair<int,int>(slot[j], slot[k]));
									//pairs.insert(pair<int,int>(slot[j], slot[k]));
									pairs.insert(pair<int,int>(slot[k], slot[j]));
								}
							}
							
						}
					}
				}
			}
/*
			it = pairs.begin();
			for(; it != pairs.end(); ++it) {
					cout << it->first << " " << it->second << "\n";
			}
*/
		    cout << "Case #" << caseCounter+1 << ": " << pairs.size()/2 << endl;
		    pairs.clear();
			delete [] slot;
			delete [] goodSlot;
	    }
	    is.close();
	    return 0;
    }

    return -1;    
}
