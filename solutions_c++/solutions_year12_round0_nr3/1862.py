#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <cstdio>
#include <queue>

using namespace std;

__int64 ans, A, B;

string int_to_string (int x) {
    string res = "";
    while (x) {
        char c = '0' + x % 10;
        res = c + res;
        x /= 10;
    }
    return res;
}

int string_to_int (const string& s) {
    if (s[0] == '0' && s.size() > 1) {
        return -1000000;
    }
    int res = 0;
    for (int i = 0; i < s.size(); ++i) {
        res = res * 10 + (s[i] - '0');
    }
    return res;
}

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
        cerr << "test = " << test << endl;
		ans = 0;
		cin >> A >> B;

        for (int x = A; x <= B; ++x) {
            if (x % 100000 == 0)
                cerr << x << endl;
            string cur = int_to_string(x);
            set <int> now;
            for (int i = 0; i < cur.size(); ++i) {
                rotate(cur.begin(), cur.begin() + 1, cur.end());
                now.insert(string_to_int(cur));
            }
            for (set <int>::iterator it = now.upper_bound(x); it != now.end(); ++it) {
                if (x < *it && *it <= B) {
                    ++ans;
                }
                if (*it > B) {
                    break;
                }
            }

        }
		
		cout << "Case #" << test << ": " << ans << endl;
	}
	return 0;
}