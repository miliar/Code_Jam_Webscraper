#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;

struct Combiner
{
	Combiner(char c1, char c2, char replace) : C1(c1), C2(c2), Replace(replace) {}
	char C1;
	char C2;
	char Replace;

	bool match(char u1, char u2)
	{
		return (u1 == C1 && u2 == C2) || (u1 == C2 && u2 == C1);
	}
};

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t != T; ++t) {
		vector<Combiner> combiners;
		int C;
		cin >> C;
		for (int c = 0; c != C; ++c) {
			string s;
			cin >> s;
			combiners.push_back(Combiner(s[0], s[1], s[2]));
		}
		int D;
		cin >> D;
		map<char, vector<char> > opposers;
		for (int d = 0; d != D; ++d) {
			string s;
			cin >> s;
			opposers[s[0]].push_back(s[1]);
			opposers[s[1]].push_back(s[0]);
		}
		int N;
		cin >> N;
		string S;
		cin >> S;

		vector<char> Vec;
		set<char> Set;
		for (int n = 0; n < N; ++n) {
			char next = S[n];
			Vec.push_back(next);
			Set.insert(next);

			// combiner check
			if (Vec.size() >= 2) {
				bool combined = false;
				for (int com = 0; com != combiners.size(); ++com) {
					if (combiners[com].match(Vec[Vec.size() - 2], Vec[Vec.size() - 1])) {
						Vec.pop_back();
						Vec.pop_back();
						Vec.push_back(combiners[com].Replace);
						combined = true;
						break;
					}
				}
				if (combined) {
					Set.clear();
					Set.insert(Vec.begin(), Vec.end());
					continue;
				}
			}

			// opposer check
			vector<char>& opp = opposers[next];
			for (size_t oppI = 0; oppI != opp.size(); ++oppI) {
				if (Set.find(opp[oppI]) != Set.end()) {
					Vec.clear();
					Set.clear();
				}
			}
		}
		cout << "Case #" << t + 1 << ": [";
		for (int i = 0; i != Vec.size(); ++i) {
			cout << Vec[i];
			if (i + 1 != Vec.size()) {
				cout << ", ";
			}
		}
		cout << "]\n";
	}
	return 0;
}
