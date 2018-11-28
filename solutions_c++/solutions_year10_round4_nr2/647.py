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

const int INF = 1000000000;
const ld EPS = 1E-9;

#define forn(i, n) for (int i = 0; i < int(n); i++)

int p;
int n;
vector<int> m;
int z[1300][1300];

void readdata()
{
	cin >> p;
    n = 1 << p;
    m.resize(n);
    forn(i, n)
    	cin >> m[i];

    forn(i, p)
    {
    	int size = n >> (i + 1);
        forn(j, size)
        	scanf("%d", &z[i][j]);
    }
}

void solve()
{
	long long sum = 0;
	forn(i, n)
    {
        int pos = i / 2;
        forn(j, p)
        {
        	if (j >= m[i])
            {
            	sum += z[j][pos];
            	z[j][pos] = 0;
            }
            pos /= 2;
        }
    }
    cout << sum << endl;
}

int main(int argc, char* argv[])
{
	freopen("B-small-attempt0.in", "rt", stdin);

	int testCount;
	cin >> testCount;

    int minTest = 1;
    int maxTest = testCount;

    if (argc == 3)
    {
    	minTest = atoi(argv[1]);
    	maxTest = atoi(argv[2]);
    }

    for (int tt = 1; tt <= testCount; tt++)
    {
    	readdata();

        if (minTest <= tt && tt <= maxTest)
        {
	        cout << "Case #" << tt << ": ";
            int now = clock();
            solve();
            int duration = clock() - now;
            cerr << "[INFO]: Test#" << tt << " takes " << duration << "ms" << endl;
        }
    }

    return 0;
}
