#pragma comment(linker, "/STACK:40000000") 

#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <string>
#include <vector>
#include <memory>
#include <algorithm>

using namespace std;


int main()
{
    freopen("i.txt", "r", stdin);
    freopen("o.txt", "w", stdout);

    int N;
    scanf("%d ", &N);
    for (int I = 1; I <= N; ++I) {
        int n, m, k;
        char o1[100], o2[100], c1[100], c2[100], c3[100];
        
        scanf("%d ", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%c%c%c ", &c1[i*2], &c2[i*2], &c3[i*2]);
            c1[i*2+1] = c2[i*2];
            c2[i*2+1] = c1[i*2];
            c3[i*2+1] = c3[i*2];
        }
        n *= 2;
        
        scanf("%d ", &m);
        for (int i = 0; i < m; ++i) {
            scanf("%c%c ", &o1[i*2], &o2[i*2]);
            o1[i*2+1] = o2[i*2];
            o2[i*2+1] = o1[i*2];
        }
        m *= 2;

        string res("");
        scanf("%d ", &k);
        for (int i = 0; i < k; ++i) {
            char lit;
            scanf("%c", &lit);
            res.push_back(lit);
            int rlen = (int)res.length();
            if (rlen >= 2) {
                for (int j = 0; j < n; ++j) {
                    if (c1[j] == res[rlen - 1] && c2[j] == res[rlen - 2]) {
                        res.resize(rlen - 2);
                        res.push_back(c3[j]);
                        --rlen;
                        break;
                    }
                }
            }
            if (rlen >= 2) {
                for (int j1 = 0; j1 < rlen - 1; ++j1) {
                    for (int j2 = 0; j2 < m; ++j2) {
                        if (o1[j2] == res[rlen - 1] && o2[j2] == res[j1]) {
                            res.clear();
                            rlen = 0;
                            break;
                        }
                    }
                }
            }
        }

        int rlen = (int)res.length();
        printf("Case #%d: [", I);
        for (int i = 0; i < rlen; ++i) {
            if (i) {
                printf(", ");
            }
            printf("%c", res[i]);
        }
        printf("]\n");
    }

    return 0;
}
