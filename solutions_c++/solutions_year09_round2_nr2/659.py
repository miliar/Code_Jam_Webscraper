#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
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
#include <cctype> 
#include <string> 
#include <cstring> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <ctime> 
#include <limits>

using namespace std;

typedef long long ll;

int main()
{
    int n;
    string s;
    cin >> n;
    for (int t = 1; t <= n; ++t)
    {
        cin >> s;
        if (!next_permutation(s.begin(), s.end()))
        {
            sort(s.begin(), s.end());
            for (int j = 0; j < s.length(); ++j)
                if (s[j] > '0')
                {
                    s = s.substr(j, 1) + "0" + s.substr(0, j) + s.substr(j + 1);
                    break;
                }
        }
        cout << "Case #" << t << ": " << s << endl;
    }
    return 0;
}