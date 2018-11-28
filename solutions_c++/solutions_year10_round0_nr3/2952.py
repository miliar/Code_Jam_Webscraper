#include <iostream>
#include <deque>

using namespace std;

int nCases, times, people;
deque<int> deq;

int countIt() {
	int sizeLeft, globalCount = 0;
	deque<int> tmpQueue;
	for(int i = 0; i < times; i++) {
		sizeLeft = people;
		while(deq.size() && sizeLeft >= deq.front()) {
			tmpQueue.push_back(deq.front());
			sizeLeft -= deq.front();
			globalCount += deq.front();
			deq.pop_front();
		}
		while(tmpQueue.size()) {
			deq.push_back(tmpQueue.front());
			tmpQueue.pop_front();
		}
	}
	return globalCount;
}

int main() {
	cin >> nCases;
	for(int i = 0; i < nCases; i++) {
		int nGroups, tmp;
		deq.clear();
		cin >> times >> people >> nGroups;
		while(nGroups--) {
			cin >> tmp;
			deq.push_back(tmp);
		}
		cout << "Case #" << i + 1 << ": " << countIt() << endl;
	}
	return 0;
}
