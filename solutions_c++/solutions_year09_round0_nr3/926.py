#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

using namespace std;

vector<string> inputs;
const string p = "welcome to code jam";
bool debug = false;
int N;

// table with 500 raws and p.length colomns
// that contains cached data for the current calculation
vector<int> cache(p.length() * 500);

/* i - index in the p
 * j - index in the s
 * s - test string
 */
int calc(string &s, int i, int j)
{
    int res = 0;
    if(debug) cout << "calc(s," << i << "," << j << ")?" << endl;
    // impossible variants;
    if ( i >= p.length() 
      || j >= s.length()
      // too many symbols left in pattern
      || (p.length() - i > s.length() - j))
    {
        if(debug) cout << "calc(s," << i << "," << j << "): " << res << " (out)" << endl;
        return res;
    }
    // get cached result
    if(cache[p.length()*j + i] != -1)
    {
        res = cache[p.length()*j + i];
        if(debug) cout << "calc(s," << i << "," << j << "): " << res << " (cached)" << endl;
        return res;
    }
    // letters equals
    if (p[i] == s[j])
    {
        // last letter in pattern
        if (i == p.length()-1)
            res = 1;
        // not last letter in pattern, try next one
        else
            res = calc(s, i+1, j+1);
    }
    res += calc(s, i, j+1);
    res %= 10000;
    //save the result
    cache[p.length()*j + i] = res;
    if(debug) cout << "calc(s," << i << "," << j << "): " << res << endl;
    return res;
}

int main(void)
{
    cin >> N; string tmp; getline(cin, tmp);
    inputs.resize(N);
    for (int i = 0; i < N; i++)
        getline(cin, inputs[i]);

    for (int i = 0; i < N; i++)
    {
        cout << "Case #" << i+1 << ": ";
        cout << setw(4) << setfill('0');
        // reinit cache
        cache.assign(inputs[i].length() * p.length(), -1);
        cout << calc(inputs[i], 0, 0) << endl;
    }
    return 0;
}
