#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>

using namespace std;

typedef long long ll;
typedef double db;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

const char c[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int T;
string s;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d ", &T);
    forn(t, T) {
        getline(cin, s);
        forn(i, s.length())
            if (s[i] != ' ') s[i] = c[s[i] - 'a'];
        printf("Case #%d: ", t + 1);
        cout << s << '\n';
    }
    return 0;
}
