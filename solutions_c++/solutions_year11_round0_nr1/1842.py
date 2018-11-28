#include <iostream>
#include <string>
#include <queue>
#include <algorithm>
#include <sstream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	int nT; cin >> nT;
	// read
	for (int t = 0; t < nT; t++) {
		int num; cin >> num;
		char ch; int val;
		vector<pair<char,int> > data;
		for (int i = 0; i < num; i++) {
			cin >> ch >> val;
			data.push_back(make_pair(ch,val));
		}
		int minTime = 0;
		// simulate
		int bluePos = 1;
		int orgPos = 1;
		for (int i = 0; i < data.size(); i++) {
			if (data[i].first == 'O') {
				// move org to pos
				int need = abs(data[i].second - orgPos) + 1; // incl push
				// move up to need positions in the right one for next blue if required
				int nextBluePos = -1;
				for (int j = i+1; j < data.size(); j++) {
					if (data[j].first == 'B') {
						nextBluePos = data[j].second;
						break;
					}
				}
				if (nextBluePos != -1) {
					// try moving
					if (nextBluePos < bluePos) {
						// back
						bluePos = max(nextBluePos, bluePos - need);
					} else {
						// forward
						bluePos = min(nextBluePos, bluePos + need);
					}
				}
				orgPos = data[i].second;
				minTime += need;
			} else {
				int need = abs(data[i].second - bluePos) + 1;
				// move up to need positions in the right one for next orange if required
				int nextOrgPos = -1;
				for (int j = i+1; j < data.size(); j++) {
					if (data[j].first == 'O') {
						nextOrgPos = data[j].second;
						break;
					}
				}
				if (nextOrgPos != -1) {
					// try moving
					if (nextOrgPos < orgPos) {
						// back
						orgPos = max(nextOrgPos, orgPos - need);
					} else {
						// forward
						orgPos = min(nextOrgPos, orgPos + need);
					}
				}
				bluePos = data[i].second;
				minTime += need;
			}
		}
		cout << "Case #" << (t+1) << ": " << minTime << "\n";
	}
	return 0;
}