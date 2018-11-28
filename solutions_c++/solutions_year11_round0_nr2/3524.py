#include <iostream>
#include <cstring>

using namespace std;


int t, c, d, n;
string c_tab[36];
string d_tab[28];
string n_tab;

bool
combine(string &tmp, char ch) {

	int last = tmp.size() - 1;

	for (int i=0; i<c; ++i) {

		if (c_tab[i][0] == ch && c_tab[i][1] == tmp[last] ||
		    c_tab[i][1] == ch && c_tab[i][0] == tmp[last] ) {

			tmp[last] = c_tab[i][2];

			return true;
		}
	}

	tmp += ch;


	return false;
}

string
opposed(string tmp, char ch) {

	int last = tmp.size();
	bool is_in = false;

	for (int i=0; i<d; ++i) {

		for (int j=0; j<last; ++j) {

			if (d_tab[i][0] == ch && d_tab[i][1] == tmp[j] ||
			    d_tab[i][1] == ch && d_tab[i][0] == tmp[j] ) {

				tmp = "";

				is_in = true;
				break;
			}
		}

		if (is_in) break;
	}


	return tmp;
}

int
main()
{
	cin >> t;

	for (int i=0; i<t; ++i) {

		cin >> c;
		for (int j=0; j<c; ++j) {

			cin >> c_tab[j];
		}

		cin >> d;
		for (int j=0; j<d; ++j) {

			cin >> d_tab[j];
		}

		cin >> n;
		cin >> n_tab;

		string tmp = "";
		tmp += n_tab[0];
		for (int j=1; j<n; ++j) {

			if (!combine(tmp, n_tab[j])) {

				tmp = opposed(tmp, n_tab[j]);
			}
		}

		cout << "Case #" << i + 1 <<": [";
		if (tmp.size()) cout << tmp[0];
		for (int j=1; j<tmp.size(); ++j) {

			cout << ", " << tmp[j];
		}
		cout << "]" << endl;
	}


	return 0;
}
