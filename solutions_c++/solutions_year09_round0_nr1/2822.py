#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main () {

	freopen("D:\\A.in", "r", stdin);
	freopen("D:\\A.out", "w", stdout);
	vector<string> known;
	vector<string> st;
	string s, test, tmp;
	int l, d, n, i, j, k, count;
	bool flag, out;
	cin >> l >> d >> n;
	for (i = 0; i < d; ++i) {
		cin >> s;
		known.push_back (s);
	}
	for (i = 0; i < n; ++i) {
		test.clear ();
		tmp.clear ();
		flag = false;
		cin >> test;
		for (j = 0; j != test.size (); ++j) {
			if (test[j] == '(') {
				flag = true;
				continue;
			}
			if (test[j] == ')') {
				st.push_back (tmp);
				tmp.clear ();
				flag = false;
				continue;
			}
			if (flag)
				tmp += test[j];
			else {
				tmp += test[j];
				st.push_back (tmp);
				tmp.clear ();
			}
		}
		out = true;
		count = 0;
		for (j = 0; j < d; ++j) {
			out = true;
			for (k = 0; k < l; ++k) {
				if (st[k].find (known[j][k]) == -1) {
					out = false;
					break;
				}
			}
			if (out) {
				++count;
				out = true;
			}
		}
		cout << "Case #" << i + 1 << ':' << ' ' << count << endl;
		st.clear ();
	}





















	//fclose(stdin);
	//fclose(stdout);
}