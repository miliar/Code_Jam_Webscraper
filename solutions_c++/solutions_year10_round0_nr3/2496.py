#include <iostream>
#include <numeric>
#include <deque>
#include <sstream>
#include <tr1/unordered_map>

using namespace std;
using namespace std::tr1;

typedef struct state {
	string shash;
	unsigned int euros;
	struct state* next;
	state(string h, unsigned int e) { shash = h; euros = e; next = 0; }
	state() { shash = ""; euros = 0; next = 0; }
	string hash() const { return shash; }
} State;

unordered_map<string, state> memoization;

string myhash(const deque<int>& d, int cap) {
	stringstream ss;	
	for (int i = 0; i < d.size(); ++i)
		ss << d[i];
	ss << cap;
	return ss.str();
}

State* GetState(deque<int>& groups, int capacity) {
	
	string hash = myhash(groups, capacity);
	if (memoization.find(hash) == memoization.end()) {
		deque<int> riders;
		while (capacity && !groups.empty() && groups.front() <= capacity) {
			capacity -= groups.front();
			riders.push_back(groups.front());
			groups.pop_front();
		}
		groups.insert(groups.end(), riders.begin(), riders.end());
		State newState(hash, accumulate(riders.begin(), riders.end(), 0));
		memoization[hash] = newState;
	}

	return &memoization[hash];
}

int main(int argc, char* argv[]) {

	istream& in = cin;
	
	int numTestCases = 0;
	in >> numTestCases;
	for (int i = 1; i <= numTestCases; ++i) {

		unsigned int r = 0, k = 0, n = 0;
		unsigned long euros = 0;
		cin >> r; cin >> k; cin >> n;

		deque<int> groups(n);
		for (int j = 0; j < n; ++j) {
			cin >> groups[j];
		}
	
		State* prev_state = 0;
		for (int ride = 0; ride < r; ++ride) {
			State* s = 0;
			if (prev_state && prev_state->next != 0) {
				s = prev_state->next;
			}
			else
				s = GetState(groups, k);

			if (prev_state && prev_state->next == 0) {
				prev_state->next = s;
			}
			prev_state = s;

			euros += s->euros;
		}

		cout << "Case #" << i << ": " << euros << endl;
	}

	return 0;
}
