#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;


char well[26][26];
bool foe[26][26];


int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int ts;
	cin >> ts;
	for (int tt=0; tt<ts; ++tt) {
		printf ("Case #%d: [", tt+1);

		int c1, c2, n;
		memset (well, 0, sizeof well);
		memset (foe, 0, sizeof foe);
		cin >> c1;
		for (int i=0; i<c1; ++i) {
			char a, b, c;
			cin >> a >> b >> c;
			well[a-'A'][b-'A'] = well[b-'A'][a-'A'] = c;
		}
		cin >> c2;
		for (int i=0; i<c2; ++i) {
			char a, b;
			cin >> a >> b;
			foe[a-'A'][b-'A'] = foe[b-'A'][a-'A'] = true;
		}
		string s;
		cin >> n >> s;

		vector<char> st;
		for (int i=0; i<n; ++i) {
			st.push_back (s[i]);
			while (st.size()>=2 && well[st.back()-'A'][st[st.size()-2]-'A']) {
				char to = well[st.back()-'A'][st[st.size()-2]-'A'];
				st.pop_back();
				st.back() = to;
			}

			bool f = false;
			for (size_t i=0; i<st.size()-1; ++i)
				f |= foe[st[i]-'A'][st.back()-'A'];
			if (f)
				st.clear();
		}

		if (st.size()) {
			printf ("%c", st[0]);
			for (size_t i=1; i<st.size(); ++i)
				printf (", %c", st[i]);
		}
		printf ("]\n");
	}

}