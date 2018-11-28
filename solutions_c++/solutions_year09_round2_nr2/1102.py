#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
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
	int cases = 0;
    scanf("%d\n", &cases);
    forn(n, cases)
    {
        string input;
        getline(cin, input);
        vector <int> seen;
        vector <int> ret;
        int stop_index = -1;
        for(int i=input.size()-1; i>0; i--)
        {
            if(input[i] > input[i-1])
            {
                stop_index = i-1;
                seen.PB(input[i]-'0');
                break;
            }
            seen.PB(input[i]-'0');
        }
        if(stop_index == -1)
        {
            if(input[input.size()-1]-'0' != 0)
            {
                ret.PB(input[input.size()-1]-'0');
                ret.PB(0);
                for(int i=input.size()-2; i>=0; i--)
                    ret.PB(input[i]-'0');
            }
            else
            {
                vector <int> nonZero;
                int numZero = 1;
                forv(i, input)
                {
                    if(input[i]-'0' != 0)
                        nonZero.PB(input[i]-'0');
                    else
                        numZero++;
                }
                sort(nonZero.begin(), nonZero.end());
                ret.PB(nonZero[0]);
                forn(i, numZero)
                    ret.PB(0);
                for(int i=1; i<nonZero.size(); i++)
                    ret.PB(nonZero[i]);
            }
        }
        else
        {
            forn(i, stop_index)
                ret.PB(input[i]-'0');
            sort(seen.begin(), seen.end());
            int stop = input[stop_index]-'0';
            forv(i, seen)
            {
                if(seen[i] > stop)
                {
                    ret.PB(seen[i]);
                    seen.erase(seen.begin()+i);
                    seen.PB(stop);
                    break;
                }
            }
            sort(seen.begin(), seen.end());
            forv(i, seen)
                ret.PB(seen[i]);
        }
        string answer = "";
        forv(i, ret)
        {
            string s;
            stringstream ss;
            ss << ret[i];
            ss >> s;
            answer = answer + s;
        }
        printf("Case #%d: %s\n", n+1, answer.c_str());
    }
	return 0;
}
