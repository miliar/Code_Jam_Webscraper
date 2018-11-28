#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>

using namespace std;



int main() {
	int cases;
	cin >> cases;
	for (int caseno = 1; caseno <= cases; caseno++) {
		cout << "Case #" << caseno << ": ";
		int c;
		cin >> c;
		string s;
		map <char, map <char,char> > combine;
		for (char i = 'A'; i <= 'Z'; i++) {
			for (char j = 'A'; j <= 'Z'; j++) {
				combine[i][j] = 0;
			}
		}
		
		for (int i = 0; i < c; i++) {
			cin >> s;
			combine[s[0]][s[1]] = s[2];
			combine[s[1]][s[0]] = s[2];
// 			cout << combine[s[0]][s[1]] << endl;
// 			cout << combine[s[1]][s[0]] << endl;
		}
		cin >> c;
		set < pair<char,char> > oppose;
		for (int i = 0; i < c; i++) {
			cin >> s;
			oppose.insert(make_pair(s[0],s[1]));
			oppose.insert(make_pair(s[1],s[0]));
			
		}
		cin >> c >> s;
		vector <char> ans;
		for (int i = 0; i < c; i++) {
			ans.push_back(s[i]);
			if (ans.size() > 1) {
				char temp = combine[ans[ans.size()-2]][ans[ans.size()-1]];
// 				cout << "check combine " << ans[i-1] << ' ' << ans[i] << ' ' << temp << endl;
				if (temp != 0) { //combine
					ans.resize(ans.size()-2);
					ans.push_back(temp);
				} else {
					//look for oppose
					pair <char,char> p;
					p.second = s[i];
					for (int j = 0; j < ans.size()-1; j++) {
						p.first = ans[j];
						if (oppose.count(p) == 1) { //oppose
// 							cout << "oppose " << p.first << ' ' << p.second << endl;
							ans.resize(0);
							break;
						}
					}
				}
			}
// 			if (ans.size() > 0) {
// 				cout << ans[0];
// 				if (ans.size() > 1) {
// 					for (int i = 1; i < ans.size(); i++) {
// 						cout << ", " << ans[i];
// 					}
// 				}
// 			}
// 			cout << endl;
		}
		//print it
		cout << '[';
		if (ans.size() > 0) {
			cout << ans[0];
			if (ans.size() > 1) {
				for (int i = 1; i < ans.size(); i++) {
					cout << ", " << ans[i];
				}
			}
		}
		cout << ']' << endl;
	}
}