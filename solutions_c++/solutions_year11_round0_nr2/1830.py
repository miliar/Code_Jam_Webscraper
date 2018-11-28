#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

char form[256][256];
bool clear[256][256];
//vector<char> clear[256];
vector<char> list;

void main() {
	
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int n, m, j;
	char str[3], a, b, t;
	
	cin >> n;
	for (int i = 0; i < n; i++) {
		memset(form, 0, sizeof(form));
		memset(clear, 0, sizeof(clear));
		//clear.clear();
		list.clear();

		cin >> m;
		for (j = 0; j < m; j++) {
			cin >> str;
			form[str[0]][str[1]] = str[2];
			form[str[1]][str[0]] = str[2];
		}
		cin >> m;
		for (j = 0; j < m; j++) {
			cin >> str;
			//clear[str[0]].push_back(str[1]);
			//clear[str[1]].pop_back(str[2]);
			clear[str[0]][str[1]] = true;
			clear[str[1]][str[0]] = true;
		}
		cin >> m;
		for (int j = 0; j < m; j++) {
			cin >> a;
transform:
			if (list.size() > 0) { 
				b = list.back();
				t = form[b][a];
			    if (t) { list.pop_back(); a = t; goto transform; }
			}
			list.push_back(a);
			for each (char c in list) 
				if (clear[c][a]) { list.clear(); break; }
		}
		cout << "Case #" << (i + 1) << ": [";
		if (list.size() > 0) cout << list[0];
		for (j = 1; j < list.size(); j++) cout << ", " << list[j];
		cout << ']' << endl;
	}
}