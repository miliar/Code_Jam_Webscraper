#include <mymacro.h>
using namespace std;

char T[] = "yhesocvxduiglbkrztnwjpfmaq";
class Solver {
public:
	string solve() {
		string s;
		getline(cin, s);
		rep(i, sz(s))
			s[i] = isalpha(s[i]) ? T[(int)s[i] - 'a'] : s[i];
		return s;
	}
};

int main() {
	int T; scanf("%d\n", &T);
	for(int t=1; t<=T; t++) {
		Solver sol;
		cout << "Case #" << t << ": " << sol.solve() << endl;
	}
	return 0;
}

