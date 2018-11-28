#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <set>
#include <ios>
#include <map>
#include <algorithm>
#include <iomanip>
#include <limits>

using namespace std;

const string p = "welcome to code jam";
const int psz = p.size();
map<int, int> d;

int solve(string& s, int pi, int si)
{
    if (pi == psz) return 1;
    if (si == s.size()) return 0;

    int di = pi * 1000 + si;
    if (d.find(di) != d.end()) return d[di];

    int result = 0;
    char l = p[pi];
    bool found = false;
    for (int i = si; i < s.size(); ++i)
    if (l == s[i]) result = (result + solve(s, pi + 1, i + 1)) % 10000;
    d[di] = result;

    return result;
}

int main(int argc, char* argv[])
{
	int N;

	cin >> N;
    cin.ignore(numeric_limits<int>::max(), '\n');

    for (int i = 1; i <= N; ++i) {
        string s;
        getline(cin, s);

        d.clear();

        cout << "Case #" << i << ": " << setw(4) << setfill('0') << solve(s, 0, 0) << endl;
    }

	return 0;
}
