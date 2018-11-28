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

#define forn(i, n) for (int i = 0; i < int(n); i++)

int n, k;
vector<int> lines[1000];
int result;

void readData()
{
	cin >> n >> k;
    forn(i, n)
    	lines[i].resize(k);
    forn(i, n)
    	forn(j, k)
        	cin >> lines[i][j];
}

bool before(const vector<int>& a, const vector<int>& b)
{
	forn(i, k)
    	if (a[i] >= b[i])
        	return false;
    return true;
}

bool g[200][200];
int mt[200];
bool used[200];

bool khun(int v)
{
	if (v == -1)
    	return false;
        
	if (used[v])
    	return false;

    used[v] = true;

    forn(i, n)
    	if (g[v][i] && (mt[i] == -1 || khun(mt[i])))
        {
        	mt[i] = v;
            return true;
        }

    return false;
}

void solve()
{
	sort(lines, lines + n);

    memset(g, 0, sizeof(g));

    forn(i, n)
    	forn(j, n)
        	if (i < j && before(lines[i], lines[j]))
            	g[i][j] = true;

    memset(mt, -1, sizeof(mt));

    result = 0;

    forn(i, n)
    {
    	memset(used, 0, sizeof(used));
        result += khun(i);
    }

    result = n - result;
}

int main(int argc, char* argv[])
{
	freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);

	int beginIndex = atoi(argv[1]);
	int endIndex = atoi(argv[2]);

	int testCount;

	string s;
	getline(cin, s);
	sscanf(s.c_str(), "%d", &testCount);
	
	for (int tt = 1; tt <= testCount; tt++)
	{
		readData();

		if (beginIndex <= tt && tt <= endIndex)
		{
			solve();
			printf("Case #%d: %d\n", tt, result);
		}
	}

	fclose(stdin);
    fclose(stdout);
	
    return 0;
}
