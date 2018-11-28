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

bool hasEnoughDigits(string s, int t)
{
    stringstream ss;
    ss << s;
    long long temp;
    ss >> temp;
    ss.str("");
    ss << temp;
    
    return ss.str().size() == t;
}

int main()
{
    int T;
    cin >> T;
    
    for (int i = 0; i < T; ++i)
    {
        string s;
        cin >> s;
        string t = s;
        sort(t.rbegin(), t.rend());
        
        cout << "Case #" << (i + 1) << ": ";
        
        if (t == s)
        {
            sort(t.begin(), t.end());
            if (t[0] == '0')
            {
                int n = 0;
                for (int i = 0; i < t.size(); ++i)
                    if (t[i] != '0')
                    {
                        n = i;
                        break;
                    }
                swap(t[0], t[n]);
            }
            cout << t[0] << 0 << string(t.begin() + 1, t.end()) << endl;
            continue;
        }
        next_permutation(s.begin(), s.end());
        cout << s << endl;
    }
    
    return 0;
}
