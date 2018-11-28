#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include "stdlib.h"
using namespace std;

int main() {
	//Number of test cases
	int t;
	cin >> t;

	for (int i = 1; i <= t; i++) {
		//Initialization
		map<pair<char, char>, char> comboMap;
		set<pair<char, char> > opposedSet;

		int c;	//number of combinatinos
		cin >> c;

		string combo;
		for (int j = 0; j < c; j++) {
			cin >> combo;

			if (combo.length() < 3) {
				cerr << "Parse error!" << endl;
				cerr << "Combo: " << combo << endl;
				exit(1);
			}

			char c1 = combo[0];
			char c2 = combo[1];
			char c3 = combo[2];

			//Combinations are mutal.
			comboMap.insert(make_pair(make_pair(c1, c2), c3));
			comboMap.insert(make_pair(make_pair(c2, c1), c3));
		}

		int d;	//number of opposed pairs
		cin >> d;

		string opposition;
		for (int j = 0; j < d; j++) {
			cin >> opposition;

			if (opposition.length() < 2) {
				cerr << "Parse error!" << endl;
				cerr << "Opposed: " << opposition << endl;
				exit(1);
			}

			char c1 = opposition[0];
			char c2 = opposition[1];

			//Oppositions are mutual
			opposedSet.insert(make_pair(c1, c2));
			opposedSet.insert(make_pair(c2, c1));
		}

		int n;	//number of elements
		cin >> n;

		string elements;
		cin >> elements;

		//Figure out what happens
		string elementList = "";
		for (int j = 0; j < elements.length(); j++) {
			char curr = elements[j];
			int length = elementList.length();
			if (length == 0) {
				//If no elements
				elementList += curr;
			}
			else {
				//Check for combinations
				char prev = elementList[length - 1];
				map<pair<char, char>, char>::iterator it = comboMap.find(make_pair(prev, curr));
				if (it != comboMap.end()) {
					//it forms a combination
					//Add current, then replace prev + current with transformed
					elementList[length-1] = it->second;
				}
				else {
					//Check for oppositions
					bool anyOpposed = false;
					for (int k = 0; k < length; k++) {
						set<pair<char, char> >::iterator it = opposedSet.find(make_pair(elementList[k], curr));

						if (it != opposedSet.end()) {
							//it forms an opposition
							//clear the element list

							anyOpposed = true;
							elementList.clear();

							break;
						}
					}

					if (!anyOpposed) {
						//Normal case
						elementList += curr;
					}
				}
			}
		}

		//Display the output
		cout << "Case #" << i << ": [";

		for (int j = 0; j < elementList.length(); j++) {
			if (j > 0) {
				cout << ", ";
			}
			cout << elementList[j];
		}
		cout << "]" << endl;
	}
}
