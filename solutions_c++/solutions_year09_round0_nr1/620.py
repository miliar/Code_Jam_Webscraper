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

int main()
{
	freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);

    int l, n, m;

    cin >> l >> n >> m;

    vector<string> w(n);

    forn(i, n)
    	cin >> w[i];


    forn(i, m)
    {
    	string t;
        cin >> t;
        vector<int> mask;

        int idx = 0;
        while (idx < t.length())
        {
        	assert(t[idx] != ')');
        	if (t[idx] != '(')
            {
            	mask.push_back(1 << (t[idx] - 'a'));
            }
            else
            {
            	idx++;
                int mm = 0;
            	while (t[idx] != ')')
                {
                	mm |= (1 << (t[idx] - 'a'));
                	idx++;
                }
                mask.push_back(mm);
            }
            idx++;
        }
        assert(mask.size() == l);

        int result = 0;
        if (mask.size() == l)
        {
            forn(j, n)
            {
                bool fail = false;

                forn(x, l)
                    if ((mask[x] & (1 << (w[j][x] - 'a'))) == 0)
                    {
                        fail = true;
                        break;
                    }

                if (!fail)
                    result++;
            }
        }

        cout << "Case #" << i + 1 << ": " << result << endl;
    }


    fclose(stdin);
    fclose(stdout);
	return 0;
}
