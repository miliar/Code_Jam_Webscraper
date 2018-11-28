
#include <cstring>
#include <vector>
#include <iostream>
#include <iomanip>
using namespace std;

const char *msg = "welcome to code jam";

struct PotentialMatch {
	int index;
	int nextletter;

	PotentialMatch(int i = -1, int l = 0) {
		index = i;
		nextletter = l;
	}
};

inline int
entry(char c)
{
	return isspace(c)? 0: c - 'a' + 1;
}

vector<vector<int> >&
mkindex(char *line)
{
	vector<vector<int> >* index = new vector<vector<int> >();
	for (int i = 0; i < 27; i++) {
		index->push_back(vector<int>());
	}
	for (char *p = line; *p; p++) {
		index->at(entry(*p)).push_back(p - line);
	}
	return *index;
}

int
nmatches(char *line)
{
	const vector<vector<int> >& index = mkindex(line);

	vector<PotentialMatch> matchers;
	matchers.push_back(PotentialMatch());

	int nmatches = 0;
	while (!matchers.empty()) {
		PotentialMatch pm = matchers.back(); matchers.pop_back();
		if (msg[pm.nextletter] == 0) {
			nmatches++;
			continue;
		}

		const vector<int>& starts = index[entry(msg[pm.nextletter])];
		for (unsigned i = 0; i < starts.size(); i++) {
			if (starts[i] > pm.index) {
				PotentialMatch npm(starts[i], pm.nextletter + 1);
				matchers.push_back(npm);
			}
		}
	}
	return nmatches;
}

int
main()
{
	const int maxlinelen = 1024;
	char *line = new char[maxlinelen];

	int N;
	cin >> N; cin.getline(line, maxlinelen);

	for (int i = 0; i < N; i++) {
		cin.getline(line, maxlinelen);
		int n = nmatches(line);
		n = n > 9999? 9999: n;
		cout << "Case #" << (i + 1) << ": " << setfill('0') << setw(4) << n << endl;
	}
}
