#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

#define TRACE(x...) x
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << '\n')

#define forz(p)     for(int i = 0; i < p; ++i)
#define foriz(i, p) for(int i = 0; i < p; ++i)
#define tr(x)       for(typeof(x.begin())it=x.begin();it!=x.end();++it)
#define read(n)     (scanf("%d", &(n)) == 1)

const int INF = 0x3f3f3f3f;
const double EPS = 1e-9;

inline int cmpD(double x, double y, double tol = EPS)
{
    return (x <= y + tol) ? (x + tol < y) ?  -1 : 0 : 1;
}

char combine[256][256];
char annihilate[256][256];
char blah[128];
char bc = 0;

void read_combine()
{
    string s;
    cin >> s;
    char a, b, c;
    a = s[0]; b = s[1]; c = s[2];
    combine[a][b] = c;
    combine[b][a] = c;
}

void read_anil()
{
    string s;
    cin >> s;
    char a, b;
    a = s[0]; b = s[1];
    annihilate[a][b] = 1;
    annihilate[b][a] = 1;
}

void push(char c)
{
    blah[bc++] = c;
}

void mashup()
{
    char c;
    while(bc > 1 and (c = combine[blah[bc-1]][blah[bc-2]]))
    {
        --bc;
        blah[bc-1] = c;
    }
}

void cleanup()
{
    const int last = bc-1;
    forz(last)
    {
        if (annihilate[blah[last]][blah[i]])
        {
            bc = 0;
            return;
        }
    }
}

string go()
{
    memset(combine, 0, sizeof(combine));
    memset(annihilate, 0, sizeof(annihilate));
    bc = 0;

    int C, D, N;
    cin >> C;
    forz(C) read_combine();

    cin >> D;
    forz(D) read_anil();

    cin >> N;
    string s;
    cin >> s;

    tr(s)
    {
        push(*it);
        mashup();
        cleanup();
    }

    ostringstream ss;
    ss << '[';
    forz(bc)
    {
        if (i) ss << ", ";
        ss << blah[i];
    }

    ss << ']';
    return ss.str();
}

int main()
{
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    forz(T)
        cout << "Case #" << i+1 << ": " << go() << '\n';
    return 0;
}
