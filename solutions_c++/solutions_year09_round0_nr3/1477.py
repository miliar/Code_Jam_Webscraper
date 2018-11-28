#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <list>
#include <vector>
#include <cmath>
#include <algorithm>
#include <sstream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FOD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, a) for (int i = 0; i < (a); i++)
#define mp make_pair
#define cl clear()
#define sz(a) ((int)a.size())
#define X first
#define Y second
#define pb push_back
#define sqr(a) ((a) * (a))

const string t = "welcome to code jam";

int n;
int a[20];

int main()
{
	scanf("%d\n", &n);
	string s;
    REP(i, n)
    {
        getline(cin, s);
        memset(a, 0, sizeof(a));
        a[19] = 1;
        FOD(k, sz(s) - 1, 0)
            FOD(j, 18, 0)
                if (s[k] == t[j])
                {
                    a[j] += a[j + 1];
                    a[j] %= 10000;
                }
        stringstream ss;
        ss << a[0];
        s = ss.str();
        while (sz(s) < 4)
            s = '0' + s;
        printf("Case #%d: %s\n", i + 1, s.c_str());
    }
	return 0;
}
