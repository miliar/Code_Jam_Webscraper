#include <cstdio>

#include <vector>
#include <map>
#include <string>
#include <set>
using namespace std;


int main() {
	// freopen("input.txt", "r", stdin);
	// freopen("B-small-attempt0.in", "r", stdin);
	// freopen("B-small-attempt0.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int iTest = 0; iTest < t; ++iTest) {
		typedef map<string, char> TMap;
		TMap nonBase;

		int c;
		scanf("%d", &c);
		for (int ic = 0; ic < c; ++ic) {
			char s[100];
			scanf("%s", s);
			char ch = s[2];
			s[2] = 0;
			nonBase[s] = ch;
		}

		typedef set<string> TSet;
		TSet opposite;

		int d;
		scanf("%d", &d);
		for (int id = 0; id < d; ++id) {
			char s[100];
			scanf("%s", s);
			opposite.insert(s);
		}

		int n;
		scanf("%d", &n);
		char elems[1000];
		scanf("%s", elems);

		typedef vector<char> TCharVector;
		TCharVector state;

		for (int i = 0; i < n; ++i) {
			char ch = elems[i];
			bool combined = false;
			if (!state.empty()) {
				{
					string s;
					s += state.back();
					s += ch;
					if (nonBase.find(s) != nonBase.end()) {
						state.pop_back();
						state.push_back(nonBase[s]);
						combined = true;
					}
				}
				if (!combined) {
					string s;
					s += ch;
					s += state.back();
					if (nonBase.find(s) != nonBase.end()) {
						state.pop_back();
						state.push_back(nonBase[s]);
						combined = true;
					}
				}
			}
			bool cleared = false;
			if (!combined) {
				for (int j = 0; j < state.size(); ++j) {
					{
						string s;
						s += state[j];
						s += ch;
						if (opposite.find(s) != opposite.end()) {
							state.clear();
							cleared = true;
						}
					}
					if (!cleared) {
						string s;
						s += ch;
						s += state[j];
						if (opposite.find(s) != opposite.end()) {
							state.clear();
							cleared = true;
						}
					}
				}
			}
			if (!combined && !cleared)
				state.push_back(ch);
		}

		printf("Case #%d: [", iTest + 1);
		for (size_t i = 0; i < state.size(); ++i) {
			if (i)
				printf(", ");
			printf("%c", state[i]);
		}
		printf("]\n");
	}

	return 0;
}