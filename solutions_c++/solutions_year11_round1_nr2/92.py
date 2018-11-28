// vim:set ts=8 sw=4 et smarttab:
// Round 1A 2011

#include <cstdio>
#include <cstring>
#include <cassert>
#include <map>
#include <algorithm>
#include <utility>

int n;
char word[10000][12];
char list[30];
int length[10000];
int table[10000][26];
int set[10000];
int set_value[10000];
bool set_split[10000];
int set_point[10000];
int nset;
typedef std::pair<int, int> pi;
std::map<pi, int> next_set;

void print_set(char c)
{
    /*
    printf("\nprint_set %c\n", c);
    for (int i = 0; i < n; ++i)
        printf("%s set: %d set_point: %d\n", word[i], set[i], set_point[set[i]]);
        */
}

int solve()
{
    nset = 1;
    for (int i = 0; i < n; ++i)
        set[i] = 0;
    for (int i = 0; i < nset; ++i)
        set_point[i] = 0;
    next_set.clear();
    for (int i = 0; i < nset; ++i)
        set_value[i] = -1;
    for (int i = 0; i < n; ++i)
    {
        int sv = length[i];
        if (set_value[set[i]] == -1)
            set_value[set[i]] = sv;
        else if (set_value[set[i]] != sv)
        {
            std::map<pi, int>::iterator it = next_set.find(pi(set[i], sv));
            if (it == next_set.end())
            {
                next_set[pi(set[i], sv)] = nset;
                set[i] = nset;
                set_point[nset] = 0;
                ++nset;
            }
            else
                set[i] = it->second;
        }
    }
    print_set(' ');
    for (int j = 0; j < 26; ++j)
    {
        char c = list[j];
        next_set.clear();
        for (int i = 0; i < nset; ++i)
        {
            set_value[i] = -1;
            set_split[i] = false;
        }
        for (int i = 0; i < n; ++i)
        {
            int sv = table[i][c - 'a'];
            if (set_value[set[i]] == -1)
                set_value[set[i]] = sv;
            else if (set_value[set[i]] != sv)
            {
                std::map<pi, int>::iterator it = next_set.find(pi(set[i], sv));
                if (it == next_set.end())
                {
                    if (!set_split[set[i]])
                    {
                        set_split[set[i]] = true;
                        if (set_value[set[i]] == 0)
                            ++set_point[set[i]];
                    }
                    next_set[pi(set[i], sv)] = nset;
                    set_point[nset] = set_point[set[i]];
                    if (set_value[set[i]] != 0 && sv == 0)
                        ++set_point[nset];
                    else if (set_value[set[i]] == 0 && sv != 0)
                        --set_point[nset];
                    set_value[nset] = sv;
                    set[i] = nset;
                    ++nset;
                }
                else
                    set[i] = it->second;
            }
        }
        print_set(c);
    }
    int max = -1;
    for (int i = 0; i < nset; ++i)
        max = std::max(max, set_point[i]);
    for (int i = 0; i < n; ++i)
        if (set_point[set[i]] == max)
            return i;
    assert(0);
    return -1;
}

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        printf("Case #%d:", tc);
        int m;
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i)
        {
            scanf("%s", word[i]);
            int len = strlen(word[i]);
            length[i] = len;
            for (char c = 'a'; c <= 'z'; ++c)
            {
                int temp = 0;
                for (int j = 0; j < len; ++j)
                    if (word[i][j] == c)
                        temp |= (1 << j);
                table[i][c - 'a'] = temp;
            }
        }
        for (int i = 0; i < m; ++i)
        {
            scanf("%s", list);
            int answer = solve();
            printf(" %s", word[answer]);
        }
        printf("\n");
    }
}
