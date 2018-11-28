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

vector<string> f;
int n;
int result;

bool can(int row, const string& s)
{
	forn(i, n)
    	if (s[i] == '1' && i > row)
        	return false;
    return true;
}

void readData()
{
	f.clear();
	cin >> n;
    forn(i, n)
    {
    	string line;
        cin >> line;
        f.push_back(line);
    }
}

void solve()
{
	result = 0;

    forn(i, n)
    {
    	if (!can(i, f[i]))
        {
        	int pos = -1;
        	for (int j = i + 1; j < n; j++)
            	if (can(i, f[j]))
                {
                	pos = j;
                    break;
                }
            assert(pos >= 0);
            for (int j = pos; j > i; j--)
            	swap(f[j], f[j - 1]), result++;
        }
    }
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
