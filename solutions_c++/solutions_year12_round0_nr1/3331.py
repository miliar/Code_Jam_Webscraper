#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <algorithm>

#define forn(i, n) for (int i = 0; i < int(n); i++)

typedef long long li;
typedef long double ld;

using namespace std;

char line[10000];

char code[256];

void apply(char a, char b)
{
    if (code[a] == -1)
        code[a] = b;
    else
        assert(code[a] == b);
}

int main(int argc, char* argv[])
{
    memset(code, -1, sizeof(code));

    FILE* fd = fopen("data.txt", "rt");
    fgets(line, sizeof(line), fd);
    int n;
    sscanf(line, "%d", &n);

    forn(i, n)
    {
        fgets(line, sizeof(line), fd);
        string from = line;
        fgets(line, sizeof(line), fd);
        string to = line;

        forn(j, from.length())
            apply(from[j], to[j]);
    }

    apply('y', 'a');
    apply('e', 'o');
    apply('q', 'z');

    char cc[256] = {0};

    int unassigned = -1;
    for (char a = 'a'; a <= 'z'; a++)
        if (code[a] == -1)
        {
            assert(unassigned == -1);
            unassigned = a;
        }
        else
            cc[code[a]] = 1;

    if (unassigned != -1)
    {
        cerr << "z" << endl;
        int f = -1;
        for (char a = 'a'; a <= 'z'; a++)
            if (cc[a] == 0)
            {
                assert(f == -1);
                f = a;
            }
        cerr << char(unassigned) << " " << char(f) << endl;
        code[unassigned] = f;
    }

    for (int i = 'a'; i <= 'z'; i++)
        if (code[i] != -1)
            cerr << char(i);
    cerr << endl;
    string back;
    for (int i = 'a'; i <= 'z'; i++)
        if (code[i] != -1)
        {
            cerr << char(code[i]);
            back += char(code[i]);
        }
    assert(set<char>(back.begin(), back.end()).size() == 26);
    cerr << endl;

    string s;
    getline(cin, s);
    sscanf(s.c_str(), "%d", &n);

    forn(i, n)
    {
        cout << "Case #" << i + 1 << ": ";
        getline(cin, s);
        forn(j, s.length())
            cout << char(code[s[j]]);
        cout << endl;
    }

    return 0;
}
