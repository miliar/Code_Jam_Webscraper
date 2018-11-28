#include <ctime>
#include <cstdio>
#include <queue>
#include <cassert>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <cassert>
#include <utility>

using namespace std;

typedef long long li;
typedef long double ld;

#define forn(i, n) for (int i = 0; i < int(n); i++)

vector<string> split(string s)
{
	vector<string> result;
	s += "/";
    string item;
	forn(i, s.length())
    	if (s[i] == '/')
        {
        	result.push_back(item);
            item = "";
        }
        else
        {
        	item += s[i];
        }
    return result;
}

struct folder
{
	map<string, int> inner;
};

int n, m;

folder f[10000];
int p;
int z;

void put(const vector<string>& d, int idx, int tree)
{
	if (idx >= d.size())
    	return;

    if (f[tree].inner.count(d[idx]) == 0)
    {
	    z++;
    	f[tree].inner[d[idx]] = p++;
    }

    put(d, idx + 1, f[tree].inner[d[idx]]);
}

int main(int argc, char* argv[])
{
	freopen("A-large.in", "rt", stdin);

	int testCount;
	cin >> testCount;

    forn(tt, testCount)
    {
    	cin >> n >> m;
        p = 1;
        forn(i, 10000)
        	f[i].inner.clear();

        z = 0;
        forn(i, n)
        {
        	string s;
        	cin >> s;
            vector<string> v = split(s);
            put(v, 1, 0);
        }

        z = 0;
        forn(i, m)
        {
        	string s;
        	cin >> s;
            vector<string> v = split(s);
            put(v, 1, 0);
        }

        cout << "Case #" << (tt + 1) << ": " << z << endl;
    }

    return 0;
}
