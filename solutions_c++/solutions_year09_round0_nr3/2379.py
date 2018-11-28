#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

#define WELCOME "welcome to code jam"
#define NW 19 /* strlen(WELCOME) */

class TestCase
{
    const char* str;
    int len;

public:
    TestCase(const string& s)
    {
        str = s.c_str();
        len = s.size();
    }

    string result()
    {
        int i = NW - 1, j = len - 1; 

        int cnt = calc(i, j);
        
        char s[5];
        sprintf(s, "%04d", cnt);

        return string(s);
    }
    
    int calc(int i, int j)
    {
        int cnt = 0;
        int s = j;

        //cout << '(' << i << ',' << j << WELCOME[i] << ')';
        while (s >= 0)
        {
            if (str[s--] != WELCOME[i])
                continue; // reverse find for a WELCOME[i]

            //cout << s;
            if (i == 0)
            {
                ++cnt;
                continue;
            }

            if (s < 0)
                break;

            cnt += calc(i - 1, s);
        }

        return cnt % 10000;
    }
};

int main()
{
    int nCases, i;
    cin >> nCases;

    string tc;
    getline(cin, tc);
    for (i = 0; i < nCases; ++i)
    {
        getline(cin, tc);
        //cout << tc << endl;
        cout << "Case #" << i + 1 << ": " << TestCase(tc).result() << endl;
    }

    return 0;
}
