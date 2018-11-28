#include <iostream>
#include <set>
#include <string>

using namespace std;

int main() {
	int t, caso = 1;
	int n, m;
	
	cin >> t;
	while (t--) {
		cin >> n >> m;
		
		set <string> table;
		string s;
		int ans = 0, from;
		
		table.insert("/");
		
		while (n--) {
			cin >> s;
			from = 1;
			do {
				from = s.find('/',from);
				if (from < 0) {
					break;
				}
				table.insert(s.substr(0,from));
				from++;
			} while (true);
			table.insert(s);
		}
		
		while (m--) {
			cin >> s;
			from = 1;
			do {
				from = s.find('/',from);
				if (from < 0) {
					break;
				}
				if (table.find(s.substr(0,from)) == table.end()) {
					table.insert(s.substr(0,from));
					ans++;
				}
				from++;
			} while (true);
			if (table.find(s) == table.end()) {
				table.insert(s);
				ans++;
			}
		}
		
		cout << "Case #" << caso++ << ": " << ans << endl;
	}
	
	return 0;
}
