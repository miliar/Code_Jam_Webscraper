#include <string>
#include <sstream>
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

int main()
{
	freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);

    int tt;
    cin >> tt;

    forn(tx, tt)
    {
    	string s;
        cin >> s;
        string was = s;

        next_permutation(s.begin(), s.end());
        if (s > was)
	        cout << "Case #" << tx + 1 << ": " << s << endl;
        else
        {
        	int zeroes = 0;
            string f = "";
            forn(i, s.length())
            	if (s[i] == '0')
                	zeroes++;
                else
                	f += s[i];
            sort(f.begin(), f.end());
            s = f[0] + string(zeroes + 1, '0') + f.substr(1);
	        cout << "Case #" << tx + 1 << ": " << s << endl;
        }
    }

    fclose(stdin);
    fclose(stdout);
	return 0;
}
