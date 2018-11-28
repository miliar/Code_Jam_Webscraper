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

int am[500][19];

int main()
{
    int N;
    cin >> N;
    cin.ignore();
    const string t = "welcome to code jam";
    for (int cs = 1; cs <= N; ++cs)
    {
        string s;
        getline(cin, s);
        memset(am, 0, sizeof(am));
        for (int i = 0; i < (int) s.length(); ++i)
            if (s[i] == 'w') ++am[i][0];

        for (int i = 0; i < (int) t.length() - 1; ++i)
            for (int j = 0; j < (int) s.length(); ++j)
                for (int k = j + 1; k < (int) s.length(); ++k)
                    if (s[j] == t[i] && s[k] == t[i + 1])
                    {
                        am[k][i + 1] += am[j][i];
                        am[k][i + 1] %= 10000;
                    }

        int sum = 0;
        for (int i = 0; i < (int) s.length(); ++i)
        {
            sum += am[i][18];
            sum %= 10000;
        }

        cout << "Case #" << cs << ": " << setw(4) << setfill('0') << sum << endl;
    }
    return 0;
}