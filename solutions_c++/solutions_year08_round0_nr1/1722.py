#include <iostream>
#include <vector>
#include <string>
using namespace std;


int main() 
{
	int N;
	cin >> N;

	for (int X=1; X<=N; ++X) {
		int S, Q;
		vector<string> engines, queries;
		cin >> S >> ws;
		for (int i=0; i<S; ++i) {
			string s;
			getline(cin, s);
			engines.push_back(s);
		}
		cin >> Q >> ws;
		for (int i=0; i<Q; ++i) {
			string q;
			getline(cin, q);
			queries.push_back(q);
		}
		int switches = 0, pos = 0;
		while (pos < queries.size()) {
			int bestEngine = 0, bestCount = 0;
			for (int i=0; i<engines.size(); ++i) {
				int count = 0;
				for (int j = pos; j < queries.size(); ++j) if (queries[j] != engines[i]) ++count; else break;
				if (count >= bestCount) { bestCount = count; bestEngine = i; }
			}
			pos += bestCount;
			if (pos < queries.size()) ++switches;
		}
		cout << "Case #" << X << ": " << switches << endl;
	}

	return 0;
}
