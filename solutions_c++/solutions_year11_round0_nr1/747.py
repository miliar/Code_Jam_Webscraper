#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>

using namespace std;

int solve( vector<int>& order, vector<int>* sequences) 
{
	int second = 0;
	int pos[2] = {1,1};
	int it[2] = {0,0};
	for (int i = 0; i < order.size(); ++i) {
		int go = order[i];
		int wait = 1- order[i];
		int actiontime = abs(sequences[go][it[go]] - pos[go]) + 1;
		bool needWait = it[wait] < sequences[wait].size();
		int waittime = needWait ? sequences[wait][it[wait]] - pos[wait] : 0;
		if (abs(waittime) <= actiontime) {
			if (needWait) {
				pos[wait] = sequences[wait][it[wait]];
			}
		} else {
			pos[wait] += waittime > 0 ? actiontime : -actiontime;
		}
		pos[go] = sequences[go][it[go]++];
		second += actiontime;
	}
	return second;
}

int main(int argc, char* argv[]) {
	int numOfCases;
	int curCase = 1;
	cin >> numOfCases;
	for (;curCase <= numOfCases; ++curCase) {
		int numOfSeq;
		cin >>numOfSeq;
		vector<int> order;
		vector<int> sequences[2];
		for (int i = 0; i < numOfSeq; ++i) {
			char name;
			int pos;
			cin >> name >> pos;
			if (name == 'O') {
				order.push_back(0);
				sequences[0].push_back(pos);
			} else {
				order.push_back(1);
				sequences[1].push_back(pos);
			}
		} // for (int i = 0; i < numOfSeq; ++i)
		int result = solve(order, sequences);
		cout << "Case #" <<curCase << ": " << result <<endl;
	}
}