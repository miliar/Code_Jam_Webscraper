#include <iostream>
#include <fstream>
#include <sstream>
#include <functional>
#include <algorithm>
#include <vector>
#include <list>

using namespace std;

int mintrains(vector<int> arr, vector<int> dep) {
	int i=0, j=0, di, dj, start=0, ctime=-1, tcnt=0;
	while (i<arr.size() && j<dep.size()) {
		if (arr[i] < dep[j]) {
			// Process train arrival;
			tcnt++;
			i++;
			continue;
		}
		if (arr[i] == dep[j]) {
			// Process simultaneous arrival/departure
			i++;
			j++;
			continue;
		}
		if (dep[j] < arr[i]) {
			// Process train departure
			if (tcnt==0) {	
				tcnt++; 
				start++;
			}
			tcnt--;
			j++;
			continue;
		}
	}
	if (i==arr.size()) {
		tcnt-=dep.size()-j;	// All trains depart;
		if (tcnt < 0) {
			start-=tcnt;
		}
	}
	return start;
}

int ttime (istream &i) {
	string tmp;
	i >> tmp;
	istringstream hs(string(tmp.begin(), tmp.begin() + tmp.find(":")));
	int h;
	hs >> h;
	istringstream ms(string(tmp.begin() + tmp.find(":") + 1, tmp.end()));
	int m;
	ms >> m;
	return h*60 + m;
}

void process_case() {
	int T;
	cin >> T;
	int NA, NB;
	cin >> NA >> NB;
	vector<int> arriveA, arriveB, departA, departB;
	for (int i=0; i<NA; i++){
		departA.push_back(ttime(cin));
		arriveB.push_back(ttime(cin)+T);
	}
	for (int i=0; i<NB; i++){
		departB.push_back(ttime(cin));
		arriveA.push_back(ttime(cin)+T);
	}
	
	sort(arriveA.begin(), arriveA.end());
	sort(arriveB.begin(), arriveB.end());
	sort(departA.begin(), departA.end());
	sort(departB.begin(), departB.end());
	
	cout << mintrains(arriveA, departA) << " " << mintrains(arriveB, departB) << endl;
}

int main() {
	int n;
	cin >> n;
	for (int i=0; i<n; i++){
		cout << "Case #" << i+1 << ": ";
		process_case();
	}
	return 0;
}
