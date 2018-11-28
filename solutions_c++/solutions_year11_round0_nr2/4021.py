#include <cstdio>
#include <cstring>
#include <list>
#include <map>
#include <set>

using namespace std;

int T, yy, C, ii, D, N, cur;
char ex[26];
int opp[26];
map<pair<int, int>, int> com;
map<pair<int, int>, int>::iterator it3;
char buffer[105];
list<char> li;
list<char>::iterator it;
list<char>::reverse_iterator it1, it2;

int main(void)
{
    scanf("%d\n", &T);
    for (yy = 1; yy <= T; yy++)
    {
        memset(ex, 0, sizeof(ex));
        for (ii = 0; ii < 26; ii++)
            opp[ii] = ii;
        scanf("%d ", &C);
        for (ii = 0; ii < C; ii++)
        {
            scanf("%s ", buffer);
            com[pair<int, int>(buffer[0] - 'A', buffer[1] - 'A')] = buffer[2]
            - 'A';
            com[pair<int, int>(buffer[1] - 'A', buffer[0] - 'A')] = buffer[2]
            - 'A';
        }
        scanf("%d ", &D);
        for (ii = 0; ii < D; ii++)
        {
            scanf("%s ", buffer);
            opp[buffer[0] - 'A'] = buffer[1] - 'A';
            opp[buffer[1] - 'A'] = buffer[0] - 'A';
        }
        scanf("%d ", &N);
        scanf("%s\n", buffer); 
        for (ii = 0; buffer[ii] != 0; ii++)
        {
            cur = buffer[ii] - 'A';
            li.push_back(cur);
            ex[cur]++;
            if (li.size() > 1)
            {
                it1 = li.rbegin();
                it2 = li.rbegin();
                it2++;
                if ((it3 = com.find(pair<int, int>(*it1, *it2))) !=
                    com.end())
                {
                    ex[(int)(*it1)]--;
                    ex[(int)(*it2)]--;
                    ex[(int)(it3->second)]++;
                    li.pop_back();
                    li.pop_back();
                    li.push_back(it3->second);
                }
            }
            if (li.size() >= 1 && opp[li.back()] != li.back() && ex[opp[li.back()]])
            {
                memset(ex, 0, sizeof(ex));
                li.clear();
            }
        }
        printf("Case #%d: [", yy);
        for (it = li.begin(); it != li.end(); it++)
        {
            if (it != li.begin())
                printf(", ");
            printf("%c", *it + 'A');
        }
        printf("]\n");
        com.clear();
        li.clear();
    }
    return 0;
}
