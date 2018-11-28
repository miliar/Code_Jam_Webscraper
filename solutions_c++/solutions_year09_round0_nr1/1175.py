#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

#define SZ(x) (int((x).size()))

static bool matches(const vector<int> &pattern, const string &needle)
{
    for (int i = 0; i < SZ(needle); i++)
    {
        int c = needle[i] - 'a';
        if (!(pattern[i] & (1 << c)))
            return false;
    }
    return true;
}

int main()
{
    int L, D, N;
    vector<string> dict;

    cin >> L >> D >> N;
    dict.resize(D);
    for (int i = 0; i < D; i++)
        cin >> dict[i];

    for (int cas = 1; cas <= N; cas++)
    {
        string pattern_str;
        vector<int> pattern(L, 0);
        bool in_paren = false;
        int pos = 0;

        cin >> pattern_str;
        for (int i = 0; i < SZ(pattern_str); i++)
        {
            if (pattern_str[i] == '(')
                in_paren = true;
            else if (pattern_str[i] == ')')
            {
                in_paren = false;
                pos++;
            }
            else
            {
                pattern[pos] |= 1 << (pattern_str[i] - 'a');
                if (!in_paren) pos++;
            }
        }

        int ans = 0;
        for (int i = 0; i < D; i++)
            if (matches(pattern, dict[i]))
                ans++;
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
