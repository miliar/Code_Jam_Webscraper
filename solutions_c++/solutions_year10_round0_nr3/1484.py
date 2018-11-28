#include <iostream>
#include <queue>
#include <set>
#include <string>
#include <sstream>

using namespace std;

string tostring(queue<int> groups) {
	stringstream out;
	while (!groups.empty()) {
		out << groups.front() << "|";
		groups.pop();
	}
	return out.str();
}


void solve(int c) {
	queue<int> groups;

	int r, k, n; cin >> r >> k >> n;
	for (int g = 0; g < n; g++) {
		int s; cin >> s;
		groups.push(s);
	}

	set<string> found;
	long long ammount = 0;
	int remaining = r;
	string repeat;
	for (int i = 0; i < r ; i++) {
		string state = tostring(groups);
		if (found.find(state) != found.end()) {
			repeat = state;
			break;
		}
		found.insert(state);
		int p = 0;
		queue<int> riding;
		while (!groups.empty() && p + groups.front() <= k) {
			p+= groups.front();
			riding.push(groups.front());
			ammount += groups.front();
			groups.pop();
		}
		while (!riding.empty()) {
			groups.push(riding.front());
			riding.pop();
		}
		remaining--;
	}	

	long long ammount_r = 0;
	int repeat_size = 0;
	for (int i = 0; i < r ; i++) {
		int p = 0;
		queue<int> riding;
		while (!groups.empty() && p + groups.front() <= k) {
			p+= groups.front();
			riding.push(groups.front());
			ammount_r += groups.front();
			groups.pop();
		}
		while (!riding.empty()) {
			groups.push(riding.front());
			riding.pop();
		}
		string state = tostring(groups);
		repeat_size++;
		if (state == repeat) break;
	}

	ammount += ammount_r * (remaining / repeat_size);
	remaining -= repeat_size * (remaining / repeat_size);

	while (remaining > 0) {
		int p = 0;
		queue<int> riding;
		while (!groups.empty() && p + groups.front() <= k) {
			p+= groups.front();
			riding.push(groups.front());
			ammount += groups.front();
			groups.pop();
		}
		while (!riding.empty()) {
			groups.push(riding.front());
			riding.pop();
		}
		remaining--;
	}

	cout << "Case #" << c << ": " << ammount << endl;
}

int main () {
	int nt; cin >> nt; int c = 1;
	while (nt-- != 0) solve(c++);

	return 0;
}
