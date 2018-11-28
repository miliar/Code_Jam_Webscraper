#include <cstdio>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    char cs[1000];
    string s;

    for (int casenum = 1; casenum <= t; ++casenum)
    {
        scanf("%s", cs);
        s = cs;
        if (!next_permutation(s.begin(), s.end()))
        {
            s = "0" + s;
            string::size_type iter = s.rfind('0');
            s[0] = s[iter + 1];
            s[iter + 1] = '0';
        }
        printf("Case #%d: %s\n", casenum, s.c_str());
    }
    return 0;
}
