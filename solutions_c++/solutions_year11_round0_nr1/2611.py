#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
using namespace std;
#define forn(i,n) for(int i=0; i<int(n); i++)
#define forsn(i,s,n) for(int i=(s); i<int(n); i++)
#define dforn(i,n) for(int i = int(n) - 1; i >= 0; i--)
#define forall(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define dforall(i,c) for(__typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)
#define all(c) (c).begin(), (c).end()
#define esta(v,c) ((c).find(v) != (c).end())
#define zMem(c) memset((c), 0, sizeof(c))
#define pb push_back
#define x first
#define y second
const int INF = 1000000000;
typedef long long tint;
typedef long double tdbl;
typedef pair<int,int> pint;

int main()
{
	#ifdef ACMTUYO
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int TT; cin >> TT;
    string basura; getline(cin, basura);
    forn(tt, TT) {
        string s;
        getline(cin, s);
        istringstream in(s); int bas; in >> bas;
        int p[2] = {1, 1}, t[2] = {0, 0}, T = 0;
        char r; int k;
        while(in >> r >> k) {
            int w = 0;
            if(r=='B') w = 1;
            t[w] += abs(p[w] - k);
            t[w] = T = max(t[w], T) + 1;
            p[w] = k;
        }
        cout << "Case #" << tt + 1 << ": " << T << endl;
    }
	return 0;
}
