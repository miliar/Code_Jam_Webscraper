#include <iostream>
#include <stdlib.h>
#include <stdint.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

class tuple {
	char a;
	char b;
public:
	tuple(char x, char y)
	: a(x), b(y) {}
	
	uint16_t cast() {
//		cout << "Key " << (uint16_t) ( (a<<8) + b) << endl;
		return (uint16_t) ( (a<<8) + b);
	}
};

void print_line(vector<char> &line) {

	cout << "[";
	for (vector<char>::iterator j = line.begin(); j != line.end(); j++) {
		if (j == line.begin()) {
			cout << *j;
		} else {
			cout << ", " << *j;
		}
	}
	cout << "]" << endl;

}

int main() {
	
	int num_case;
	cin >> num_case;
		
	for (int i = 0; i < num_case; i++) {
	
		map<uint16_t, char> combine;
		set<char> conflict[26];
		
		int temp;
		cin >> temp;
		for (int j = 0; j < temp; j++) {
			char a, b, c;
			cin >> a >> b >> c;
			combine[tuple(a,b).cast()] = c;
			combine[tuple(b,a).cast()] = c;
		}
		cin >> temp;
		for (int j = 0; j < temp; j++) {
			char a, b;
			cin >> a >> b;
			conflict[a-'A'].insert(b);
			conflict[b-'A'].insert(a);
		}
		
		cin >> temp;		
		multiset<char> cur;
		vector<char> line;
		
		for (int j = 0; j < temp; j++) {
			char next;
			cin >> next;
			if (!line.empty()) {
				/* check combine first */
				if (combine.find(tuple(next, line.back()).cast()) != combine.end()) {
//					cout << "Combine " << next << " " << line.back() << endl;
					cur.erase(cur.find(line.back()));
					line.back() = combine[tuple(next, line.back()).cast()];
				} else if (combine.find(tuple(line.back(), next).cast()) != combine.end()) {
//					cout << "Combine " << line.back() << " " << next << endl;
					cur.erase(cur.find(line.back()));
					line.back() = combine[tuple(line.back(), next).cast()];
				} else {
					/* no combine, check conflict */
					vector<char> inter_temp(cur.size());
					vector<char>::iterator it;
					it = set_intersection(cur.begin(), cur.end(), conflict[next-'A'].begin(), conflict[next-'A'].end(), inter_temp.begin());
					if ( it != inter_temp.begin()) {
						/* if conflict, clear */
//						cout << "Conflict on " << next << endl;
						cur.clear();
						line.clear();
					} else {
						/* if no conflict, push_back and set */
						cur.insert(next);
						line.push_back(next);
					}
				}
			} else {
				line.push_back(next);
				cur.insert(next);
			}
//			print_line(line);
		}
		
		cout << "Case #" << i+1 << ": ";
		print_line(line);
	}

	return 0;
}
