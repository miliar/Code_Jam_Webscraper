#include <iostream>
#include <string>
#include <map>
#include <sstream>
#include <memory.h>
#include <algorithm>
#include <vector>
#include <set>
#include <fstream>
#include <queue>
#include <cmath>

typedef long long int64;
using namespace std;

string s;
int n;

const string wcj = "welcome to code jam";
const int wcjl = 19;

int ways[800][wcjl+1];

int solve(string &s) {
    int l = s.length();
    memset(ways, 0, sizeof ways);
    for (int i=0; i<=s.length(); i++)
        ways[i][0] = 1;
    for (int i=1; i<=s.length(); i++)
        for (int j=1; j<=wcjl; j++) {
            if (s[i-1] == wcj[j-1])
                ways[i][j] = (ways[i][j] + ways[i-1][j-1])%10000;
            ways[i][j] = (ways[i][j]+ways[i-1][j])%10000;
        }
    int ans = ways[s.length()][wcjl];
    return ans;
}

string dig4(int a) {
    char tmp[100];
    itoa(a, tmp, 10);
    string res = tmp;
    while (res.length() < 4)
        res = '0'+res;
    return res;
}

int main() {
    ifstream cin("3.in");
    ofstream cout("3.out");
    cin >> n;
    getline(cin, s);
    for (int i=0; i<n; i++) {
        getline(cin ,s);
        cout << "Case #" << i+1 << ": " << dig4(solve(s)) << endl;
    }
    return 0;
}