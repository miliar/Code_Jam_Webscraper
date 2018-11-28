#include <iostream>
#include <map>
#include <deque>
#include <algorithm>
using namespace std;
bool combines(map<char, map<char, char> > &combine, char el1, char el2);

int main() {

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {

		int C;
		cin >> C;
		map<char, map<char, char> > combine;
		while (C--) {
			char base1, base2, nonBase;
			cin >> base1;
			cin >> base2;
			cin >> nonBase;
			combine[base1][base2] = nonBase;
			combine[base2][base1] = nonBase;
		}

		int D;
		cin >> D;
		map<char, map<char, bool> > oppose;
		while (D--) {
			char base1, base2;
			cin >> base1;
			cin >> base2;
			oppose[base1][base2] = true;
			oppose[base2][base1] = true;
		}

		int N;
		cin >> N;
		deque<char> queue;
		while (N--) {
			char curBase;
			cin >> curBase;
			if (queue.empty()) {
				queue.push_back(curBase);
				continue;
			}

			char lastElement = queue.back();
			if (combines(combine, curBase, lastElement)) {
				curBase = combine[curBase][lastElement];
				queue.pop_back();
				queue.push_back(curBase);
			} else {
				//maybe it opposes sth
				bool found = false;
				if (oppose.find(curBase) != oppose.end()) {
					map<char,bool> opposingElements = oppose[curBase];
					map<char,bool>::iterator it;
					for (it=opposingElements.begin();it!=opposingElements.end();it++) {
						if (find(queue.begin(),queue.end(),it->first) != queue.end()) {
							queue.clear();
							found = true;
							break;
						}
					}
				}
				if (!found) {
					queue.push_back(curBase);
				}
			}

			/*//combination
			 bool iterate = true;
			 while (iterate) {
			 char lastElement = queue.back();
			 if (combines(combine, curBase, lastElement)) {
			 iterate = true;
			 curBase = combine[curBase][lastElement];
			 queue.pop_back();
			 } else {
			 iterate = false;
			 queue.push_back(curBase);
			 }
			 if (queue.empty()) {
			 queue.push_back(curBase);
			 break;
			 }
			 }*/
		}

		cout << "Case #" << t << ": ";
		cout << "[";
		while (!queue.empty()) {
			cout << queue.front();
			queue.pop_front();
			if (!queue.empty()) {
				cout << ", ";
			}
		}
		cout << "]" << endl;

	}

	return 0;
}

bool combines(map<char, map<char, char> > &combine, char el1, char el2) {
	if (combine.find(el1) != combine.end()) {
		if (combine[el1].find(el2) != combine[el1].end()) {
			return true;
		}
	}
	return false;
}
