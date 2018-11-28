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

#define forn(i, n) for (int i = 0; i < int(n); i++)

int main(int argc, char* argv[])
{
	freopen("C-large.in", "rt", stdin);

	int t;
	cin >> t;

    forn(tt, t)
    {
    	li r, k, n;
    	cin >> r >> k >> n;
        vector<li> g(n);
        forn(i, n)
        	cin >> g[i];

        li result = 0;
        li pos = 0;
        vector<li> tx(n, -1);
        vector<li> sum(n, -1);
        vector<li> steps;

        forn(i, r)
        {
        	if (tx[pos] == -1)
            {
            	tx[pos] = i;
                sum[pos] = result;
                steps.push_back(pos);
            }
            else
            {
            	li cycle = i - tx[pos];
                li cycleSum = result - sum[pos];
                li left = r - i;
                li full = left / cycle;
                result += cycleSum * full;
                left = left % cycle;

                forn(x, steps.size())
                	if (steps[x] == pos)
                    {
                    	x++;
                    	forn(f, left)
                        {
                        	li d = sum[steps[x + f]] - sum[steps[x + f - 1]];
                            result += d;
                        }
                    	break;
                    }

                break;
            }


            li size = k;
            forn(off, n)
            {
            	li idx = (pos + off) % n;
            	if (size >= g[idx])
                {
                    result += g[idx];
                    size -= g[idx];
                }
                else
                {
                	pos = idx;
                    break;
                }
            }
        }

        cout << "Case #" << (tt + 1) << ": " << result << endl;
    }

    return 0;
}
