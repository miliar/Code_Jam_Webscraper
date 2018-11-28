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
        vector <char> seen;
        int base = 0;
        forv(i, input)
        {
            bool has_seen = false;
            forv(j, seen)
                if(input[i] == seen[j])
                {
                    has_seen = true;
                    break;
                }
            if(!has_seen)
            {
                seen.PB(input[i]);
                base++;
            }
        }
        vector <int> assignment;
        forv(i, seen)
        {
            if(i==0)
                assignment.PB(1);
            else if(i==1)
                assignment.PB(0);
            else
                assignment.PB(i);
        }
        long long ret = 0;
        if(base == 1)
            base++;
        for(int i=input.size()-1; i>=0; i--)
        {
            int seen_index = 0;
            forv(j, seen)
                if(seen[j] == input[i])
                {
                    seen_index = j;
                    break;
                }
            int actual_num = assignment[seen_index];
            int place = input.size()-1-i;
            ret += actual_num * pow(base, double(place));
        }
        printf("Case #%d: %lld\n", n+1, ret);
    }
	return 0;
}
