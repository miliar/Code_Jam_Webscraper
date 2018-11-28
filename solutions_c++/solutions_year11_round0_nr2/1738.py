#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

#define Eo(x) { std::cerr << #x " = " << x << std::endl; }

typedef std::pair<char, char> cpair;

inline cpair join(char a, char b) {
    if(a > b) return cpair(b, a);
    else return cpair(a, b);
}

char buf[1 << 17];

std::map<cpair, char> combine;
std::set<cpair> oppose;

std::vector<char> seq;

int main() {
    int t, tc;
    for(scanf("%d", &tc), t = 1; t <= tc; ++t) {
        printf("Case #%d:", t);
        int c, d, n, i;

        seq.clear();
        combine.clear();
        oppose.clear();

        scanf("%d", &c);
        for(i = 0; i < c; i++) {
            scanf(" %s", buf);
            combine[join(buf[0], buf[1])] = buf[2];
        }
        scanf("%d", &d);
        for(i = 0; i < d; i++) {
            scanf(" %s", buf);
            oppose.insert(join(buf[0], buf[1]));
        }
        scanf("%d %s", &n, buf);

        int l = strlen(buf);
        assert(l == n);
        for(i = 0; i < l; i++) {
            seq.push_back(buf[i]);
            int cnt = seq.size();
            if(cnt > 1) {
                if(combine.find(join(seq[cnt-2], seq[cnt-1])) != combine.end()) {
                    char nc = combine[join(seq[cnt-2], seq[cnt-1])];
                    seq.pop_back();
                    seq.pop_back();
                    seq.push_back(nc);
                } else 
                    for(int j = 0; j < cnt-1; j++)
                        if(oppose.find(join(seq[j], seq[cnt-1])) != oppose.end())
                            seq.clear();
            }
        }

        printf(" [");
        for(int i = 0; i < seq.size(); i++)
            printf("%s%c", (i ? ", " : ""), seq[i]);
        printf("]\n");
    }
    return 0;
}
