#include <functional>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <bitset>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <ctime>
#include <stack>
#include <deque>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;

long long pow(long long a, long long b)
{
    long long n = 1;
    for (int i = 0; i < b; ++i)
        n *= a;
    return n;
}

int main()
{
    int T;
    cin >> T;
    
    for (int i = 0; i < T; ++i)
    {
        string s;
        cin >> s;
        
        int base;
        long long seconds = 0;
        set <char> t(s.begin(), s.end());
        base = (t.size() > 1 ? t.size() : 2);
        
        map <char, int> characterMap;
        characterMap[s[0]] = 1;
        int n = 0;
        seconds += characterMap[s[0]]
                 * pow((long long)base, (long long)s.size() - 1);
        for (int j = 1; j < s.size(); ++j)
        {
            if (!characterMap.count(s[j]))
            {
                characterMap[s[j]] = n;
                n += (n == 0 ? 2 : 1);
            }
            seconds += characterMap[s[j]]
                     * pow((long long)base, (long long)s.size() - j - 1);
        }
        
        cout << "Case #" << (i + 1) << ": " << seconds << endl;
    }
    
    return 0;
}
                
                
