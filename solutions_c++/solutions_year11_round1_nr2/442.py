#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define for0(i,n) for(int i = 0; i < (n); i ++)

int n, m;

string dict[105];
string strats[12];
bool isConsistent[105];

char shown[15];


int derp = 100;
int main() {
	
	int kases; cin >> kases;
	
	for0(kase, kases) {
		
		cin >> n >> m;
		
		for0(i, n) cin >> dict[i];
		for0(i, m) cin >> strats[i];
		
		
		cout << "Case #" << (kase+1) << ":";
		
		for0(strat, m) {
			int max = -1;
			string maxMy = "+_+_+_+_+_+";
			for0(j, n) {
				string my = dict[j];
				for0(i, 15) shown[i] = '\0';
				for0(i, 105) isConsistent[i] = true;
				int pen = 0;
				int consistent = 0;
					// cerr << endl;
					// cerr << "my = " << my << endl;
					// cerr << endl;
				for (int i = 0; i < 26; ) {
					char c = strats[strat][i];
					
					// cerr << "MAIN C = " << c << endl;
					// c needs to be in some consistent word
					bool goC = false;
					for0(t,n) {
						if (!isConsistent[t]) continue;
						bool foo = true;
						if (my.size() != dict[t].size()) {
							isConsistent[t] = false;
							continue;
						}
						// cerr << "consistent dict[t] = " << dict[t] << endl;
						for0(k, dict[t].size()) {
					// cerr << "dict[t][k] = " << dict[t][k] << endl;
							if (shown[k] == '\0' && c == dict[t][k]) {
								goC = true;
								break;
							}
						}
						// if (goC) break;
					}
					if (!goC){ i ++; continue;}
					// cerr << "MAIN C = " << c << endl;
					
						// cerr << endl;
					// if (derp-- < 0) return 0;
					if (my.find(c, 0) != string::npos) {
					// cerr << "y" << endl;
						for0(k,my.size()) {
							if (my[k] == c) shown[k] = c;
						}
					// update consistency
						for0(t,n) {
							if (!isConsistent[t]) continue;
							bool foo = true;
							if (my.size() != dict[t].size()) {
								isConsistent[t] = false;
								continue;
							}
							for0(k, dict[t].size()) {
								if ((shown[k] == '\0' &&dict[t][k] == c) || (shown[k] != '\0' && shown[k] != dict[t][k])) {
									isConsistent[t] = false;
									break;
								}
							}
						// cerr << "consistent dict[t] = " << dict[t] << " " << isConsistent[t] << endl;
						}
					} else {
					// cerr << "n" << endl;
					// cerr << "pen c = " << c << endl;
						pen ++;
					// update consistency
						for0(t,n) {
							if (!isConsistent[t]) continue;
							bool foo = true;
							if (my.size() != dict[t].size()) {
								isConsistent[t] = false;
								continue;
							}
							for0(k, dict[t].size()) {
								if (c == dict[t][k]) {
									isConsistent[t] = false;
									break;
								}
							}
						}
					}
					// for0(t,n) {
						// if (!isConsistent[t]) continue;
						// bool foo = true;
						// if (my.size() != dict[t].size()) {
							// isConsistent[t] = false;
							// continue;
						// }
						// for0(k, dict[t].size()) {
							// if (shown[k] == c && c != dict[t][k]) {
								// isConsistent[t] = false;
								// break;
							// }
						// }
					// }
					// update c
					for(int i2 = i+1; i2 < 26; i2 ++) {
								// cerr << "strats = " << strats[strat] << endl;
						char c2 = strats[strat][i2];
								// cerr << "c2 = " << c2 << endl;
								// cerr << "i2 = " << i2 << endl;
								// cerr << "26 = " << 26 << endl;
						bool isValid = false;
						for0(t,n) {
							if (!isConsistent[t]) continue;
									// cerr << "dict[t] = " << dict[t] << endl;
									// cerr << "my.size() = " << my.size() << endl;
									// cerr << "dict[t].size() = " << dict[t].size() << endl;
							for0(k, dict[t].size()) {
										// cerr << "dict[t][k] = " << dict[t][k] << endl;
								if (shown[k] == '\0' && dict[t][k] == c2) {
									// cerr << "new" << endl;
									// cerr << "i2 = " << i2 << endl;
									i = i2;
									isValid = true;
									break;
								}
							}
							if (isValid) break;
						}
						if (isValid) break;
						for (int ib = i+1; ib < i2; ib ++) {
							
						}
					}
						// cerr << "i = " << i << endl;
					
					bool win = true;
					for0(k, my.size()) {
						// cerr << "shown[k] = " << (shown[k] == '\0' ? '_' : shown[k]) << endl;
						if (shown[k] == '\0') win = false;
					}
					if (win) {
						if (pen > max) maxMy = my;
						max = pen > max ? pen : max;
						break;
					}
				}
			}
			cout << " " << maxMy;
			// cout << " " << max;
			// cout << maxMy;
		}
		
		cout << endl;
	}
}