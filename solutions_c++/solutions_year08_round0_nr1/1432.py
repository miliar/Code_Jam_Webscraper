#include <iostream>
#include <string>

using namespace std;

int main() {
	int tn;
	char t[102];
	cin >> tn;
	for(int ti = 0; ti < tn;) {
		int n, qn, fn = 0, res = 0;
		cin >> n;
		cin.ignore();
		string *s = new string[n];
		for(int i = 0; i < n; i++)
			cin.getline(t, 101), s[i] = t;
		cin >> qn;
		cin.ignore();
		bool *flag = new bool[n];
		for(int i = 0; i < n; i++)
			flag[i] = true;
		while(qn--) {
			cin.getline(t, 101);
			int i = 0;
			for(; i < n; i++)
				if(s[i] == t) break;
			if(flag[i]) {
				if(++fn == n) {
					for(res++; fn--; flag[fn] = true);
					fn = 1;
				}
				flag[i] = false;
			}
		}
		cout << "Case #" << ++ti << ": " << res << endl;
	}
	return 0;
}
