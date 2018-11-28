#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <set>

using namespace std;

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);
	int z;
	cin >> z;
	for (int q=0;q<z;q++) {
		int c, d, n;

		vector<string> rep;
		cin >> c;
		for (int i=0;i<c;i++) {
			string str;
			cin >> str;
			sort(str.begin(), str.end() - 1);
			rep.push_back(str);
		}

		vector<string> rem;
		cin >> d;
		for (int i=0;i<d;i++) {
			string str;
			cin >> str;
			sort(str.begin(), str.end());
			rem.push_back(str);
		}

		cin >> n;
		string str;
		cin >> str;
		string res = "";
		for (int i=0;i<str.size();i++) {
			if (res.empty()) {
				res += str[i];
				continue;
			}
			char a = str[i];
			char b = res[res.size()-1];
			if (a > b) {
				char temp = b;
				b = a;
				a = temp;
			}

			bool flag = false;
			for (int j=0;j<rep.size();j++) {
				if (rep[j][0] == a && rep[j][1] == b) {
					res[res.size()-1] = rep[j][2];
					flag = true;
					break;
				}
			}
			if (flag) continue;

			for (int j=0;j<res.size();j++) {
				char a = str[i];
				char b = res[j];
				if (a > b) {
					char temp = b;
					b = a;
					a = temp;
				}

				for (int k=0;k<rem.size();k++) {
					if (rem[k][0] == a && rem[k][1] == b) {
						res = "";
						flag = true;
						break;;
					}
				}
				if (flag) break;
			}
			if (flag) continue;

			res += str[i];
		}

		cout << "Case #" << (q+1) << ": [";
		for (int i=0;i<res.size();i++) {
			cout << res[i];
			if (i != res.size()-1) {
				cout << ", ";	
			}
		}
		cout << "]" << endl;
	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}