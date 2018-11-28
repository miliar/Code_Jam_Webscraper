/*#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<string> A;
int main() {
	freopen("INPUT.txt", "r", stdin);
	freopen("OUTPUT.txt", "w", stdout);

	string a;
	getline(cin, a);
	int i = 1;
	while (getline(cin, a)) {

		a += ' ';
		string buf = "";
		for (int j = 0; j < a.length(); j++) {
			if (a[j] == ' ') {
				if (buf != "") {
					A.push_back(buf);
					buf = "";
				}
			} else {
				buf += a[j];
			}
		}
		cout << "Case #" << i << ":";
		for ( int j = A.size() - 1; j >= 0; j--) {
			cout << ' ' << A[j];
		}
		cout << endl;
		A.clear();
		i++;
	}
	return 0;
}*/

/*#include <iostream>
#include <vector>
using namespace std;
int main() {
	freopen("INPUT.txt", "r", stdin);
	freopen("OUTPUT.txt", "w", stdout);
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		int c, m;
		cin >> c >> m;
		vector<int> I(m);
		for (int j = 0; j < m; j++) {
			cin >> I[j];
		}
		cout << "Case #" << i + 1 << ": ";
		for (int j = 0; j < m - 1; j++) {
			for (int k = j + 1; k < m; k++) {
				if (I[j] + I[k] == c) {
					cout << j + 1 << ' ' << k + 1 << endl;
					j = m;
					break;
				}
			}
		}
	}

	return 0;
}*/

/*#include <iostream>
#include <string>
using namespace std;
string A[] = {"2", "22", "222", "3", "33", "333", "4", "44", "444", "5", "55", "555", "6", "66", "666", "7", "77", "777", "7777", "8", "88", "888",
	"9", "99", "999", "9999"};
int main() {
	freopen("INPUT.txt", "r", stdin);
	freopen("OUTPUT.txt", "w", stdout);
	string a;
	getline(cin, a);
	int i = 1;
	while(getline(cin, a)) {
		cout << "Case #" << i << ": ";
		int last = -1;
		for (int i = 0; i < a.length(); i++) {
			if (a[i] == ' ') {
				if (last == 0) cout << ' ';
				last = 0;
				cout << '0';
			} else {
				if (last == A[a[i] - 'a'][0] - '0') cout << ' ';
				last = A[a[i] - 'a'][0] - '0';
				cout << A[a[i] - 'a'];
			}
		}
		cout << endl;
		i++;
	}
	return 0;
}*/

/*#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
	freopen("INPUT.txt", "r", stdin);
	freopen("OUTPUT.txt", "w", stdout);
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int m;
		cin >> m;
		vector<long long> A(m), B(m);
		for (int j = 0; j < m; j++) {
			cin >> A[j];
		}
		for (int j = 0; j < m; j++) {
			cin >> B[j];
		}
		sort(A.begin(), A.end());
		sort(B.begin(), B.end());
		long long ans = 0;
		for (int j = 0; j < m; j++) {
			ans += A[j] * B[m - j - 1];
		}
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}*/

#include <iostream>
#include <string>
using namespace std;
int main() {
	freopen("INPUT.txt", "r", stdin);
	freopen("OUTPUT.txt", "w", stdout);
	string A = "yhesocvxduiglbkrztnwjpfmaq";
	string a;
	getline(cin, a);
	int j = 1;
	while (getline(cin, a)) {
		cout << "Case #" << j << ": ";
		for (int i = 0; i < a.length(); i++) {
			if (a[i] == ' ') {
				cout << ' ';
			} else {
				cout << A[a[i] - 'a'];
			}
		}
		cout << endl;
		j++;
	}
	return 0;
}