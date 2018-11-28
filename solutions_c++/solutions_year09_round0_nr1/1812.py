#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define sz size()
#define PB push_back
#define clr(x) memset(x, 0, sizeof(x))
#define forn(i,n) for(__typeof(n) i = 0; i < (n); i++)
#define ford(i,n) for(int i = (n) - 1; i >= 0; i--)
#define forv(i,v) forn(i, v.sz)
#define For(i, st, en) for(__typeof(en) i = (st); i < (en); i++)

using namespace std;
typedef long long ll;

int main()
{
	int lower = 0, words = 0, cases = 0;
	cin >> lower >> words >> cases;
    vector <string> alien;
    forn(i, words)
    {
        string input;
        cin >> input;
        alien.PB(input);
    }
    forn(i, cases)
    {
        string pattern;
        cin >> pattern;
        vector <string> pat;
        bool open = true;
        string tmp_str = "";
        forv(j, pattern)
        {
            if(open && pattern[j] != '(' && pattern[j] != ')')
            {
                stringstream ss;
                string s;
                ss << pattern[j];
                ss >> s;
                pat.PB(s);
                continue;
            }
            if(pattern[j] == '(')
            {
                open = false;
                tmp_str = "";
                continue;
            }
            else if(pattern[j] == ')')
            {
                pat.PB(tmp_str);
                open = true;
                continue;
            }
            if(!open)
                tmp_str += pattern[j];
        }
        int ret = 0;
        forv(a, alien)
        {
            forv(j, alien[a])
            {
                char c = alien[a][j];
                bool found = false;
                forv(k, pat[j])
                {
                    if(c == pat[j][k])
                    {
                        found = true;
                        break;
                    }
                }
                if(!found)
                    break;
                if(j == alien[i].size()-1)
                    ret++;
            }
        }
        printf("Case #%d: %d\n", i+1, ret);
    }

	return 0;
}
