#include <iostream>
#include <string>
using namespace std;

string str;
string pat = "welcome to code jam";
int mas[30][600];
int n;


int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	cin >> n;
	getline(cin, str);
	for (int i = 0; i < n; ++i) {
		getline(cin, str);
		for (int j = 0; j < 30; ++j) memset(mas[j], 0, sizeof(mas[j]));

		for (int j = 0; j < str.size(); ++j) {
			if (str[j] == pat[0])
				mas[1][j] = 1;
		}

		for (int k = 1; k < pat.size(); ++k) {
			int sum = 0;
			for (int j = 0; j < str.size(); ++j) {
				if (str[j] == pat[k])
					mas[k + 1][j] = sum % 10000;
				sum += mas[k][j];
			}
		}

		int res = 0;
		for (int k = 0; k < str.size(); ++k)
			res += mas[pat.size()][k];
		res = res % 10000;

		cout << "Case #" << i + 1 << ": "; 
		if (res < 10)
			cout << "000" << res;
		else if (res < 100)
			cout << "00" << res;
		else if (res < 1000)
			cout << "0" << res;
		else 
			cout << res;
		cout << endl;
	}

	return 0;
}