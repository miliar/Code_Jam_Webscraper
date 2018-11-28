#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <map>
#include <iomanip>

using namespace std;

#define MOD 10000

int count(int x, int y, const string& s1, const string& s2, vector<vector<int> >& v) {
    if (y == s2.size()) return 1;
    if (x == s1.size()) return 0;
    if (v[x][y] != -1)  return v[x][y];
    return v[x][y] = ((s1[x] == s2[y] ? count(x+1, y+1, s1, s2, v) : 0) + count(x+1, y, s1, s2, v)) % MOD;
}

int main() {
    int N;
    cin >> N >> ws;
    for (int i = 0; i < N; i++) {
        string s; getline(cin, s);
        vector<vector<int> > v(s.size(), vector<int> (19, -1));
        cout << "Case #" << i+1 << ": " << setfill('0') << setw(4) << count(0, 0, s, "welcome to code jam", v) << endl;
    }
}
