#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#include <queue>
#include <ctime>
#include <deque>
#include <stack>

const int INF = 2147483647;
const double EPS = 0.0000001;
const int MOD = 295075153;

using namespace std;
            //"abcdefghijklmnopqrstuvwxyz"

string code = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

	int q;
	cin >> q;
	string s;
	getline(cin, s);
	for(int t = 1; t <= q; ++t) {
        getline(cin, s);
        for(int i = 0; i < s.length(); ++i)
            if(s[i] >= 'a' && s[i] <= 'z')
                s[i] = code[s[i] - 'a'];
        cout << "Case #" << t << ": " << s << endl;
	}

	return 0;
}
