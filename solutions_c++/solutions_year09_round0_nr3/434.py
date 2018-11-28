
#include <string>
#include <vector>
#include <sstream>
#include <iostream>
using namespace std;

string pattern = "welcome to code jam";

int main() {
    string line;
    getline(cin, line);
    stringstream sin(line);
    int tst;
    sin >> tst;
    for (int cas = 0; cas < tst; ++cas) {
        getline(cin, line);
        int len = line.size();
        vector <vector <int> > am(len + 1, vector <int>(pattern.size() + 1, 0));
        am[0][0] = 1;
        for (int at = 0; at < len; ++at)
            for (int pos = 0; pos <= (int)pattern.size(); ++pos) {
                am[at + 1][pos] = (am[at + 1][pos] + am[at][pos]) % 10000;
                if (pos < (int)pattern.size() && pattern[pos] == line[at])
                    am[at + 1][pos + 1] = (am[at + 1][pos + 1] + am[at][pos]) % 10000;
            }
        printf("Case #%d: %04d\n", cas + 1, am[len][pattern.size()]);
    }
    return 0;
}