#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

struct Comb {
	//set<char> base;
	string base;
	char product;

	Comb() : base(""), product() {};
};

struct Opp {
	set<char> opp;

	Opp() : opp() {};
};

string formatResult(const string& str) {
	string result = "[";
	for (string::const_iterator itr = str.begin(); itr != str.end(); ++itr) {
		result += *itr;
		result += ", ";
	}
	result = result.substr(0, result.size() - 2) + "]";
	return result;
}

int main()
{
	ios_base::sync_with_stdio(false);
	int testCases;
	cin >> testCases;

	for (int testCase = 1; testCase <= testCases; ++testCase) {
		vector<Comb> combs;
		vector<Opp> opps;

		int combSize;
		cin >> combSize;

		if (!cin) {
			break;
		}

		//cerr << "combSz: " << combSize << "\n";
		for (int i = 0; i < combSize; ++i) {
			char base1,
				 base2,
				 prod;
			cin >> base1 >> base2 >> prod;

			string base = "";
			base += base1;
			base += base2;
			//cerr << "base: " << base << "\n";
			
			Comb newComb;
			//newComb.base.insert(base1);
			//newComb.base.insert(base2);
			newComb.base = base;
			newComb.product = prod;
			combs.push_back(newComb);
		}

		int oppSize;
		cin >> oppSize;
		//cerr << "oppSz: " << oppSize << "\n";
		for (int i = 0; i < oppSize; ++i) {
			char base1,
				 base2;
			cin >> base1 >> base2;

			Opp newOpp;
			newOpp.opp.insert(base1);
			newOpp.opp.insert(base2);
			opps.push_back(newOpp);
		}

		int seqSize;
		string seq;
		cin >> seqSize;
		cin >> seq;

		//cerr << "starting seq: " << seq << "\n";
		string result = "";
		for (string::iterator itr = seq.begin(); itr != seq.end(); ++itr) {
			char elem = *itr;
			result += elem;
						
			if (result.size() > 1) {
				bool moveOn = false;
				// Combines?
				char penult = *(result.end() - 2);
				for (vector<Comb>::iterator cItr = combs.begin(); cItr != combs.end(); ++cItr) {
					Comb &c  = *cItr;
					string possibleBase1 = "";
					possibleBase1 += penult;
					possibleBase1 += elem;
					string possibleBase2 = "";
					possibleBase2 += elem;
					possibleBase2 += penult;
					
					if (c.base == possibleBase1 || c.base == possibleBase2) {
						//cerr << "combining: " << result << "\n";
						result = result.substr(0, result.size() - 2);
						result += c.product;
						moveOn = true;
						break;
					}
				}

				// If not, does it opposes?
				if (!moveOn) {
					for (vector<Opp>::iterator oItr = opps.begin(); oItr != opps.end(); ++oItr) {
						Opp &o = *oItr;
						if (o.opp.count(elem)) {
							for (set<char>::iterator otherElemItr = o.opp.begin(); otherElemItr != o.opp.end(); ++otherElemItr) {
								if (*otherElemItr == elem) continue;
								
								//cerr << "cancelling: " << result << " - elems: " << elem << "/" << *otherElemItr << "\n";
								
								if (result.substr(0, result.size() - 1).find(*otherElemItr) != string::npos) {
									result = "";
								}
							}
						}
					}
				}

				// If does not combine or oppose, no change then, proceed to next element.
			}
		}

		cout << "Case #" << testCase << ": " << formatResult(result) << "\n"; 
	}
	return 0;
}