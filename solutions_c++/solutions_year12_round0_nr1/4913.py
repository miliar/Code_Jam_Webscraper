#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <memory.h>
#include <vector>
#include <queue>
#include <deque>
#include <string>
#include <stack>
#include <ctime>
#include <set>
#include <map>
     
using namespace std;

int main() {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//freopen("goat1.in", "r", stdin); freopen("goat1.out", "w", stdout);
	char ex[30] = "yhesocvxduiglbkrztnwjpfmaq";
	string s;
	int n;
	cin >> n;
	getline(cin, s);
	for (int i = 0; i < n; ++i) {
		cout << "Case #" << i + 1 << ": ";
		getline(cin, s);
		for (int j = 0; j < s.length(); ++j) {
			if ('a' <= s[j] && s[j] <= 'z') {
				cout << ex[s[j] - 'a'];
			} else {
				cout << s[j];
			}
		}
		cout << endl;
	}
		
    return 0;
}
