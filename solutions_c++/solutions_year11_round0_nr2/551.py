#include <fstream>
#include <string>
#include <vector>
#include <set>

using namespace std;

#define sz(v)		((int) v.size())
#define fv(v, i)	for (int i = 0; i < sz(v); ++i)
#define fn(n, i)	for (int i = 0; i < n; ++i)

#define FILENAME	"B-large-0"

const int M = 26;
int combination[M][M];
set<int> opposed[M];
int counter[M];

int main() {
	ifstream in(FILENAME ".in");
	ofstream out(FILENAME ".out");

	int T;
	in >> T;
	for (int test = 1; test <= T; ++test) {
		vector<int> ans;
		int C, D, N;
		memset(combination, 0xff, sizeof(combination));
		memset(counter, 0, sizeof(counter));
		fn(M, i)
			opposed[i].clear();
		string str;

		in >> C;
		fn(C, i) {
			in >> str;
			combination[str[0] - 'A'][str[1] - 'A'] = str[2] - 'A';
			combination[str[1] - 'A'][str[0] - 'A'] = str[2] - 'A';
		}
		in >> D;
		fn(D, i) {
			in >> str;
			opposed[str[0] - 'A'].insert(str[1] - 'A');
			opposed[str[1] - 'A'].insert(str[0] - 'A');
		}
		in >> N >> str;
		fv(str, i) {
			int next = str[i] - 'A';
			if (sz(ans) > 0 && combination[ans.back()][next] != -1) {
				int back = ans.back();
				int c = combination[back][next];
				ans.pop_back();
				ans.push_back(c);
				--counter[back];
				++counter[c];
			} else {
				bool clear = false;
				for (set<int>::iterator it = opposed[next].begin(); it != opposed[next].end(); ++it)
					if (counter[*it] > 0) {
						ans.clear();
						memset(counter, 0, sizeof(counter));
						clear = true;
						break;
					}
				if (!clear) {
					ans.push_back(next);
					++counter[next];
				}
			}
		}

		out << "Case #" << test << ": [";
		fv(ans, i)
			out << (i == 0 ? "" : ", ") << (char) (ans[i] + 'A');
		out << "]" << endl;
	}

	return 0;
}