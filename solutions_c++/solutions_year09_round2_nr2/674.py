#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <map>
#include <set>
#include <string>
using namespace std;

int cases, cas = 1;
string num;

int main() {
    for (scanf("%d", &cases); cases--; ) {
        cin >> num; int len = (int) num.size(), pos;
        map<char, int> cnt; cnt[num[len - 1]] = 1;
        for (pos = (int) num.size() - 2; pos >= 0 && num[pos] >= num[pos + 1]; --pos) {
            cnt[num[pos]]++;
        }
        cout << "Case #" << cas++ << ": ";
        if (pos < 0) {
            map<char, int>::iterator it = cnt.begin();
            if (it->first == '0') {
                ++it;
                cout << it->first << "0"; it->second--;
                for (it = cnt.begin(); it != cnt.end(); ++it) for (int k = 0; k < it->second; ++k) {
                    cout << it->first;
                }
                cout << endl;
            } else {
                cout << it->first << "0"; it->second--;
                for (it = cnt.begin(); it != cnt.end(); ++it) for (int k = 0; k < it->second; ++k) {
                    cout << it->first;
                }
                cout << endl;
            }
        } else {
            for (int k = 0; k < pos; ++k) {
                cout << num[k];
            }
            for (map<char, int>::iterator it = cnt.begin(); it != cnt.end(); ++it) if (it->first > num[pos]) {
                cout << it->first; it->second--;
                break;
            }
            cnt[num[pos]]++;
            for (map<char, int>::iterator it = cnt.begin(); it != cnt.end(); ++it) for (int k = 0; k < it->second; ++k) {
                cout << it->first;
            }
            cout << endl;
        }
    }
    return 0;
}
