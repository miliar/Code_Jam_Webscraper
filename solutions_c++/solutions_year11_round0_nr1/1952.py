#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

struct Robot {
	char c;
	int pos;
	int goal;
	bool pressed;
	bool done;
};

int main() {
	int nCases;
	cin >> nCases;
	for (int thisCase = 1; thisCase <= nCases; thisCase++) {
		int nSteps;
		cin >> nSteps;
		
		char c;
		int i;
		
		char curr = 0x00;
		int total = 0;
		int time = 0;
		int pO = 1, pB = 1;
		int *p;
		
		vector< pair<char,int> > seq;
		
		for (int thisStep = 0; thisStep < nSteps; thisStep++) {
			cin >> c >> i;
			seq.push_back(pair<char,int>(c,i));
			
		}

		vector< pair<char,int> >::iterator iO = seq.begin(), iB = seq.begin(), it = seq.begin();

		Robot o = {'O', 1, 1, false, false};
		while (iO != seq.end() && iO->first != o.c) iO++;
		if (iO != seq.end()) o.goal = iO->second;
		else o.done = true;
	
		Robot b = {'B', 1, 1, false, false};
		while (iB != seq.end() && iB->first != b.c) iB++;
		if (iB != seq.end()) b.goal = iB->second;
		else b.done = true;
		
		bool pressed;
		int count = 0;
		
		// cout << "Orange: " << o.pos << endl;
		// cout << "Blue:   " << b.pos << endl << endl;
		
		while (!(o.done && b.done)) {
			pressed = false;
			
			if (!o.done) {

				if (o.pos == o.goal) {
					if (!pressed && it->first == o.c) {

						do { iO++; } while (iO != seq.end() && iO->first != o.c);
						if (iO != seq.end()) o.goal = iO->second;
						else o.done = true;
						it++;
						pressed = true;
						
					} else {

					}
				} else {
					o.pos += o.goal < o.pos ? -1 : 1;

				}
			}
			
			if (!b.done) {
				if (b.pos == b.goal) {
					if (!pressed && it->first == b.c) {
					
						do { iB++; } while (iB != seq.end() && iB->first != b.c);
						if (iB != seq.end()) b.goal = iB->second;
						else b.done = true;
						it++;
						pressed = true;
						
					}
				} else {
					b.pos += b.goal < b.pos ? -1 : 1;
				}
			}
			count++;
			
			// cout << "Orange: " << o.pos << endl;
			// cout << "Blue:   " << b.pos << endl << endl;

		}
		
		cout << "Case #" << thisCase << ": " << count << endl;
		// cout << endl;
	}
}
