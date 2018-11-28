#include <iostream>
#include <vector>
#include <set>

using namespace std;

struct Oppose {
	char c1, c2;
	
	Oppose(char c_1, char c_2) {
		c1 = c_1;
		c2 = c_2;
	}
	
	char getPair(char c) {
		if (c == c1) {
			return c2;
		} else if (c == c2) {
			return c1;
		}
		return -1;
	}
};


struct Combine {
	vector<char> c1, c2, res;
	int stored;
	
	Combine() {
		stored = 0;
	}
	
	void addComb(char c_1, char c_2, char r) {
		c1.push_back(c_1);
		c2.push_back(c_2);
		res.push_back(r);
		stored += 1;		
	}
	
	char getComb(char c_1, char c_2) {
		for (int i = 0; i < stored; ++i) {
			if ((c1[i] == c_1 && c2[i] == c_2) || (c2[i] == c_1 && c1[i] == c_2)) {
				return res[i];
			}
		}
		return 0;
	}
};


int main() 
{
	int cases;
	cin >> cases;
	
	for (int i = 0; i < cases; ++i) {

		int combs, opps, length;
		
		cin >> combs;
		Combine cs;
		for (int c = 0; c < combs; ++c) {
			char rule[3]; 
			cin >> rule;
			cs.addComb(rule[0], rule[1], rule[2]);
		}
		
		cin >> opps;
		vector<Oppose> opp;
		for (int c = 0; c < opps; ++c) {
			char rule[2];
			cin >> rule;
			opp.push_back( Oppose(rule[0], rule[1]) );
		}

/*		
		// print out collected info:
		cout << "Oppositions: " << endl;
		for (int c = 0; c < opps; ++c) {
			cout << opp[c].c1 << opp[c].c2 << endl;
		}
		
		cout << "combinations: " << endl;
		for (int c = 0; c < cs.stored; ++c) {
			cout << cs.c1[c] << cs.c2[c] << cs.res[c] << endl;
		}
		cout << endl;
*/
	
		
		cin >> length;
		
		vector<char> sofar;
		char seq[101];
		cin >> seq;
		for (int c = 0; c < length; ++c) {

			bool cleared = false;
			char cur = seq[c];

//			cout << "Looking at character " << c << ": " << cur << endl;

			if (!sofar.empty()) {
				char into = cs.getComb(cur, sofar.back());
				while (into != 0 && !sofar.empty()) {
//					cout << "combines into" << into << endl;
					
					cur = into;
					sofar.pop_back();
					into = cs.getComb(cur, sofar.back());
				}
				
				// now once we did all the combinations, test if there's opposition
				// this can only exist between cur and the rest
				for (int cc = 0; cc < sofar.size(); ++cc) {
					for (int co = 0; co < opps; ++co) {
						
/*						if (opp[co].getPair(cur) == -1) {
							continue;
						}
*/
						if (opp[co].getPair(cur) == sofar[cc]) {
							cleared = true;
							sofar.clear();
//							cout << "cleared" << endl;
							break;
						}

					}
				}
				
			} 
			
			if (!cleared) {
				// just add the new character and done
				sofar.push_back(cur);
//				cout << "added " << cur << endl;
			}
			
		}

		
		cout << "Case #" << i+1 << ": [";
		for (int c = 0; c+1 < sofar.size(); ++c) {
			 cout << sofar[c] << ", ";	
		}
		if (!sofar.empty()) {
			cout << sofar.back();
		}
		cout << "]" << endl;

	}
		
}

