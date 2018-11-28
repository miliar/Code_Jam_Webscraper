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

int n;
vector< vector<int> > g;

void readdata()
{
	string s;
	getline(cin, s);
    sscanf(s.c_str(), "%d", &n);g = vector<vector<int> > (n, vector<int>(n, -1));

    for (int i = 0; i < 2 * n - 1; i++)
    {
		getline(cin, s);
        forn(j, s.length())
        {
        	if (s[j] >= '0' && s[j] <= '9')
            {
            	int pos = j / 2;
                //cout << i << " " << j << " | ";
                int row = ((n - 1) - (j - i)) / 2;

                int col = ((i + j) - (n - 1)) / 2;

                g[row][col] = s[j] - '0';
            }
        }
    }
}

bool isGood(vector< vector<int> > v)
{
	int n = v.size();

	forn(i, n)
    {
        forn(j, n)
        {
        	// main
            int ni = j;
            int nj = i;
            if (v[i][j] != v[ni][nj] && v[ni][nj] != -1 && v[i][j] != -1)
            	return false;
            if (v[i][j] == -1)
            	v[i][j] = v[ni][nj];
            if (v[ni][nj] == -1)
            	v[ni][nj] = v[i][j];

            // add
            ni = n - j - 1;
            nj = n - i - 1;
            if (v[i][j] != v[ni][nj] && v[ni][nj] != -1 && v[i][j] != -1)
            	return false;
            if (v[i][j] == -1)
            	v[i][j] = v[ni][nj];
            if (v[ni][nj] == -1)
            	v[ni][nj] = v[i][j];
        }
    }

    return true;
}

bool ok(int m)
{
    	vector<vector<int> > pt = vector<vector<int> > (m, vector<int>(m, -1));

        forn(dx, m - n + 1)
        	forn(dy, m - n + 1)
            {
            	vector<vector<int> > cd(pt);
                bool fail = false;
            	forn(i, n)
                {
                	if (fail)
                    	break;
                	forn(j, n)
                    {
                    	cd[i + dx][j + dy] = g[i][j];
                        // main
                        int ni = j + dy;
                        int nj = i + dx;
                        if (cd[ni][nj] != -1 && cd[ni][nj] != g[i][j])
                        {
                        	fail = true;
                            break;
                        }
                        cd[ni][nj] = g[i][j];

                        // add
                        ni = m - (j + dy) - 1;
                        nj = m - (i + dx) - 1;
                        if (cd[ni][nj] != -1 && cd[ni][nj] != g[i][j])
                        {
                        	fail = true;
                            break;
                        }
                        cd[ni][nj] = g[i][j];
                    }
                }
                if (!fail && isGood(cd))
                {
                	//if (isGood(cd))
                    {
                    	return true;
                    }
                }
            }

            return false;
}

int solve(int inc)
{
	int lf = n;
    int rg = 3.5 * n;

    while (rg - lf > 3)
    {
    	int mid = (((lf + rg) / 2) / 2) * 2 + inc;
        if (mid < n)
        	mid = n;
        if (ok(mid))
        {
        	rg = mid;
        }
        else
        {
        	lf = mid;
        }
    }
    for (int mid = lf; mid <= rg; mid++)
    	if (ok(mid))
        {
        	return mid * mid - n * n;
        }
    return INF;
}

void solve()
{
	cout << min(solve(0), solve(1)) << endl;
}

int main(int argc, char* argv[])
{
	freopen("A-large.in", "rt", stdin);
	//freopen("input.txt", "rt", stdin);

	int testCount;
	cin >> testCount;
    string s;
	getline(cin, s);

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

