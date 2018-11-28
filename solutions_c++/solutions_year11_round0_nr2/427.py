// vim:set ts=8 sw=4 et smarttab:
// Qualification Round 2011

#include <cstdio>
#include <cstring>
#include <cctype>
#include <cassert>
#include <deque>
#include <algorithm>

int combine[26][26];
bool opposite[26][26];

void init()
{
    std::fill(combine[0], combine[26], -1);
    std::fill(opposite[0], opposite[26], false);
}

void input_combine()
{
    int c;
    scanf("%d", &c);
    for (int i = 0; i < c; ++i)
    {
        char temp[10];
        int a, b, c;
        scanf("%s", temp);
        assert(strlen(temp) == 3);
        for (int j = 0; j < 3; ++j)
            assert(isupper(temp[j]));
        a = temp[0] - 'A';
        b = temp[1] - 'A';
        c = temp[2] - 'A';
        combine[a][b] = c;
        combine[b][a] = c;
    }
}

void input_opposite()
{
    int d;
    scanf("%d", &d);
    for (int i = 0; i < d; ++i)
    {
        char temp[10];
        int a, b;
        scanf("%s", temp);
        assert(strlen(temp) == 2);
        for (int j = 0; j < 2; ++j)
            assert(isupper(temp[j]));
        a = temp[0] - 'A';
        b = temp[1] - 'A';
        opposite[a][b] = true;
        opposite[b][a] = true;
    }
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        init();
        input_combine();
        input_opposite();
        int n;
        scanf("%d", &n);
        assert(n >= 1 && n <= 100);
        char str[102];
        scanf("%s", str);
        assert((int)strlen(str) == n);
        std::deque<int> element_list;
        for (int i = 0; i < n; ++i)
        {
            assert(isupper(str[i]));
            int a = str[i] - 'A';
            int temp;
            if (!element_list.empty() && (temp = combine[element_list.back()][a]) != -1)
            {
                element_list.pop_back();
                element_list.push_back(temp);
            }
            else
            {
                bool flag = true;
                for (std::deque<int>::const_iterator it = element_list.begin(); it != element_list.end(); ++it)
                    if (opposite[*it][a])
                    {
                        element_list.clear();
                        flag = false;
                        break;
                    }
                if (flag)
                    element_list.push_back(a);
            }
        }
        printf("Case #%d: [", tc);
        for (std::deque<int>::const_iterator it = element_list.begin(); it != element_list.end(); ++it)
        {
            if (it != element_list.begin())
                printf(", ");
            printf("%c", 'A' + *it);
        }
        printf("]\n");
    }
}
