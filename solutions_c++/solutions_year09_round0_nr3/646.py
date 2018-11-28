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

int z[1000][1000];

int M = 10000;

int main()
{
	freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);

    int tc;
    cin >> tc;
    string s;
    getline(cin, s);
    string t = "welcome to code jam";

    forn(tt, tc)
    {
    	getline(cin, s);

        int n = s.length();
        int m = t.length();

        forn(i, n + 1)
        	forn(j, m + 1)
            	z[i][j] = 0;

        forn(i, n + 1)
        	z[i][0] = 1;

        for (int i = 1; i <= n; i++)
        	for (int j = 1; j <= m; j++)
            {
            	if (s[i - 1] != t[j - 1])
                {
                	z[i][j] = z[i - 1][j] % M;
                }
                else
                {
                	z[i][j] = (z[i - 1][j - 1] + z[i - 1][j]) % M;
                }
            }

        printf("Case #%d: %04d\n", tt + 1, z[n][m]);
    }

    fclose(stdin);
    fclose(stdout);
	return 0;
}
