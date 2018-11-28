#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

#define FOR(A, I, B) for(int A = (int)I; A < (int)B; A++)

int l, d, n;

char dic[5010][20];
int possible[5010];

void marcaimp(int pos, char c)
{
    FOR(i, 0, d){
        if(dic[i][pos] != c) possible[i] = -1;
    }
}

int main()
{
    scanf("%d %d %d", &l, &d, &n);
    FOR(i, 0, d)
        scanf("%s", dic[i]);

    FOR(i, 0, n){
        char pat[1000];

        memset(possible, 0, sizeof(possible));
        scanf("%s", pat);
        
        int pos = 0;
        FOR(j, 0, l){
            if(pat[pos] == '('){
                int ini = pos;
                while(pat[pos] != ')') pos++;
                FOR(k, 0, d){
                    if(possible[k] == 0){
                        bool ok = false;
                        FOR(m, ini + 1, pos){
                            if(dic[k][j] == pat[m]){
                                ok = true;
                                break;
                            }
                        }
                        if(!ok) possible[k] = -1;
                    }
                }
                pos++;
            } else {
                marcaimp(j, pat[pos]);
                pos++;
            }
        }
        int resp = 0;
        FOR(ii, 0, d) if(possible[ii] == 0) resp++;
        printf("Case #%d: %d\n", i + 1, resp);
    }
    return 0;
}

