#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

char combine[26][26];
unsigned int oppose[26];

void setbit(int index, int pos)
{
    oppose[index] |= ((unsigned int)1 << pos);
}
int main()
{
    int T;
    scanf("%d",&T);
    for (int test=1; test<=T; ++test) {
        memset(combine, 0, sizeof(combine));
        memset(oppose, 0, sizeof(oppose));
        int C;
        scanf("%d", &C);
        for (int c=0; c<C; ++c) {
            char buf[10];
            scanf("%s",buf);
            combine[buf[0]-'A'][buf[1]-'A'] = buf[2];
            combine[buf[1]-'A'][buf[0]-'A'] = buf[2];
        }

        int D;
        scanf("%d",&D);
        for (int d=0; d<D; ++d) {
            char buf[10];
            scanf("%s",buf);
            setbit(buf[0]-'A', buf[1]-'A');
            setbit(buf[1]-'A', buf[0]-'A');
        }

        int N;
        scanf("%d", &N);
        char invokelist[1000];
        scanf("%s",invokelist);

        string answer;
        unsigned int curlist = 0;
        int count[26] = {0};
        memset(count, 0, sizeof(count));
        
        for (int n=0; n<N; ++n) {
            if (answer.empty()) {
                answer.push_back(invokelist[n]);
                unsigned int curpos = (invokelist[n] - 'A');
                count[curpos]++;
                curlist |= ((unsigned int)1 << curpos);
            }
            else {
                char combchar = combine[answer[answer.length()-1]-'A'][invokelist[n]-'A'];
                if (combchar) {
                    unsigned int curpos = (answer[answer.length()-1] - 'A');
                    if (count[curpos]) count[curpos]--;
                    if (!count[curpos]) {
                        curlist &= ~((unsigned int)1 << curpos);
                    }
                    answer[answer.length()-1] = combchar;
                }
                else {
                    if (curlist & oppose[invokelist[n] - 'A']) {
                        curlist = 0;
                        answer.clear();
                        memset(count, 0, sizeof(count));
                    }
                    else {
                        unsigned int curpos = (invokelist[n] - 'A');
                        count[curpos]++;
                        curlist |= ((unsigned int)1 << (curpos));
                        answer.push_back(invokelist[n]);
                    }
                }
            }
        }

        printf("Case #%d: [", test);
        for (int ans=0; ans<answer.length(); ++ans) {
            printf("%c", answer[ans]);
            if (ans < answer.length() - 1) {
                printf(", ");
            }
        }
        printf("]\n");
    }
    return 0;
}