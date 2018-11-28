#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
using std::vector;

int main()
{
    int T, tIdx;
    scanf("%d", &T);
    int N, nIdx;
    vector<char> eList;
    char ch, c1, c2;
    char o[26][26];
    char c[26][26];
    int C, cIdx, D, dIdx;
    int flag[26], idx;
    for (tIdx = 0; tIdx < T; ++tIdx)
    {
        for (cIdx = 0; cIdx < 26; ++cIdx)
        {
            memset(o[cIdx], 0, sizeof(char) * 26);
            memset(c[cIdx], 0, sizeof(char) * 26);
        }
        memset(flag, 0, sizeof(int) * 26);
        scanf("%d", &C);
        for (cIdx = 0; cIdx < C; ++cIdx)
        {
            scanf(" %c%c%c", &c1, &c2, &ch);
            c[c1 - 'A'][c2 - 'A'] = ch;
            c[c2 - 'A'][c1 - 'A'] = ch;
        }
        scanf("%d", &D);
        for (dIdx = 0; dIdx < D; ++dIdx)
        {
            scanf(" %c%c", &c1, &c2);
            o[c1 - 'A'][c2 - 'A'] = 1;
            o[c2 - 'A'][c1 - 'A'] = 1;
        }
        scanf("%d", &N);
        scanf("%c", &ch);
        for (nIdx = 0; nIdx < N; ++nIdx)
        {
            scanf("%c", &ch);
            if (eList.empty())
            {
                idx = ch - 'A';
                ++flag[idx];
                eList.push_back(ch);
                continue;
            }
            c1 = eList.back();
            while (c[c1 - 'A'][ch - 'A'] != 0)
            {
                ch = c[c1 - 'A'][ch - 'A'];
                eList.pop_back();
                --flag[c1 - 'A'];
                if (eList.empty())
                    break;
                c1 = eList.back();
            }
            idx = ch - 'A';
            ++flag[idx];
            eList.push_back(ch);
            for (cIdx = 0; cIdx < 26; ++cIdx)
            {
                if (o[ch - 'A'][cIdx] == 1 && flag[cIdx] != 0)
                {
                    memset(flag, 0, sizeof(int) * 26);
                    eList.clear();
                    break;
                }
            }
        }
        printf("Case #%d: [", tIdx + 1);
        for (cIdx = 0; cIdx < eList.size(); ++cIdx)
        {
            if (cIdx != 0)
                printf(", ");
            printf("%c", eList[cIdx]);
        }
        printf("]\n");
        eList.clear();
    }
    return 0;
}
