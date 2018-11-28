#include<iostream>
#include<set>
#include<map>
#include<vector>

using namespace std;

int main() {
	
	unsigned cases;
 	unsigned N;
 	long long temp;
	
	cin >> cases;
	
	for (unsigned cn = 0; cn < cases; ++cn) {
//		if (cn) cout << endl;
		cout << "Case #" << cn + 1 << ":" << endl;

		set< long long > sums;
		// maps the sum to the set that created it
		map< long long, vector<long long> > formingSet;
		sums.insert(0);
		formingSet[0] = vector<long long>();
		cin >> N;
		
		bool success = false;
		vector<long long> set1;
		vector<long long> set2;
		
		for (unsigned i = 0; i < N; ++i) {
			cin >> temp;
			
// 			if (temp == 22940096) {
// 				cout << "Well.. it's there!" << endl;
// 			}
// 			cout << "Read " << temp << endl;
			
			if (success) continue;
			
			// iterate through all things in sums.. 
			set<long long> justAdded;
			for (set<long long>::iterator it = sums.begin(); it != sums.end(); it++) {
				// propose putting in:
				long long proposed = temp + *it;
				if (sums.find(proposed) != sums.end()) {
					// success!
					set1 = formingSet[proposed];
					set2 = formingSet[*it];
					set2.push_back(temp);
					
// 					cout << "Found " << proposed << endl;
					success = true;
					break;
				} else {
					// we can just insert it
//					cout << "Adding " << proposed << endl;
					justAdded.insert(proposed);
					formingSet[proposed] = formingSet[*it];
					
// 					if (temp == 22940096) {
// 						cout << ".. it's there!" << endl;
// 					}
// 
					formingSet[proposed].push_back(temp);
					
					
				}
			}
			
			if (!success) {
				// now merge justAdded with sums
				sums.insert(justAdded.begin(), justAdded.end());				
			}
		}
		
// 		cout << "ANSWER___________" << endl;
// 		if (success) {
// 			cout << set1[0];
// 			for (unsigned i = 1; i < set1.size(); ++i) {
// 				cout << " " << set1[1];
// 			}
// 			cout << endl;
// 			cout << set2[0];
// 			for (unsigned i = 1; i < set1.size(); ++i) {
// 				cout << " " << set2[1];
// 			}
// 			cout << endl;
// 		} else {
// 			cout << "Impossible" << endl;
// 		}

// 		cout << "ANSWER___________" << endl;
		if (success) {
			for (unsigned i = 0; i < set1.size(); ++i) {
				if (set1[i] == 0) continue;
				if (i) cout << " ";
				cout << set1[i];
			}
			cout << endl;
			for (unsigned i = 0; i < set2.size(); ++i) {
				if (set2[i] == 0) continue;
				if (i) cout << " ";
				cout << set2[i];
			}
			cout << endl;
		} else {
			cout << "Impossible" << endl;
		}
		
	}
	
	return 0;
	
}
