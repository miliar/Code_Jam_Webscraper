#include <cstdio>
#include <climits>
#include <cstring>
#include <cassert>
#include <algorithm>
using namespace std;

bool match(char* word, char* pattern)
{
    bool avail[26];
    while (*pattern && *word) {
        memset(avail, false, sizeof(avail));
        if (*pattern == '(') {
            pattern++;
            while (*pattern != ')') {
                avail[*pattern - 'a'] = true;
                pattern++;
            }
        } else
            avail[*pattern - 'a'] = true;

        if (!avail[(int)*word - 'a'])
            return false;

        pattern++;
        word++;
    }
    return *pattern == 0 && *word == 0;
}

int query(int D, char** dic, char* pattern)
{
    int res = 0;
    for (int i = 0; i < D; i++)
        if (match(dic[i], pattern)) res++;
    return res;
}

int main()
{
    int L, D, N;
    char** dic;

    scanf("%d %d %d", &L, &D, &N);
    dic = new char* [D];
    for (int i = 0; i < D; i++) {
        dic[i] = new char[L+1];
        scanf("%s", dic[i]);
    }

    char* pattern = new char[L * 1000];
    for (int i = 0; i < N; i++) {
        scanf("%s", pattern);
        printf("Case #%d: %d\n", i+1, query(D, dic, pattern));
    }
    delete [] pattern;

    for (int i = 0; i < D; i++)
        delete [] dic[i];
    delete [] dic;
    return 0;
}
