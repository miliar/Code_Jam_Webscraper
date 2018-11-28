/*
    Qualification Round 2011 -
    Magicka
    by Dave Chang
*/
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std ;

    char comp[256][256];
    bool oppo[256][256];

    int T, C, D, N;
    vector<char> list;
    int inlist[256];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    for(int z=1; z<=T; ++z) {
        memset(comp, 0, sizeof(comp));
        memset(oppo, 0, sizeof(oppo));
        char str[101];
        scanf("%d", &C);
        for(int i=0; i<C; ++i) {
            scanf("%s", str);
            comp[(unsigned)str[0]][(unsigned)str[1]] =
            comp[(unsigned)str[1]][(unsigned)str[0]] = str[2];
        }
        scanf("%d",&D);
        for(int i=0; i<D; ++i) {
            scanf("%s", str);
            oppo[(unsigned)str[0]][(unsigned)str[1]] =
            oppo[(unsigned)str[1]][(unsigned)str[0]] = true;
        }
        scanf("%d %s", &N, str);
        list.clear();
        memset(inlist,0, sizeof(inlist));
        for(int i=0;i<N;++i) {
            list.push_back(str[i]);
            ++inlist[(unsigned)str[i]];
            int s = list.size();
            // test composite
            while(s>1 && comp[(unsigned)list[s-1]][(unsigned)list[s-2]]) {
                char add = comp[(unsigned)list[s-1]][(unsigned)list[s-2]];
                //printf("%d %c\n",i,add);
                --inlist[(unsigned)list[s-1]];
                --inlist[(unsigned)list[s-2]];
                list.pop_back();
                list.pop_back();
                list.push_back(add);
                ++inlist[add];
            }
            // test opposed
            for(unsigned i=0; i<256; ++i) {
                for(unsigned j=i; j<256; ++j) {
                    if(((i==j && inlist[i]>=2) || (i!=j && inlist[i]>=1 && inlist[j]>=1))
                       && oppo[i][j]) {
                        list.clear();
                        memset(inlist, 0, sizeof(inlist));
                    }
                }
            }
        }
        printf("Case #%d: [", z);
        if(list.size()>0)
            printf("%c", list[0]);
        for(unsigned i=1; i<list.size(); ++i)
            printf(", %c", list[i]);
        printf("]\n");
    }
    return 0;
}
