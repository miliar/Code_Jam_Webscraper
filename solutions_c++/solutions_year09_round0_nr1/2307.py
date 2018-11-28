/*
  ID: nigo1
  LANG: C++
  TASK:
*/
#include <iostream>
#include <stdio.h>

#define pf printf
#define sf scanf
#define TIME ((double)clock()/CLOCKS_PER_SEC)

using namespace std;

int L, D, N;
char w[5000][15];
bool p[15][26];

int main()
{
    freopen ("A-large.in", "r", stdin);
    freopen ("A-large.out", "w", stdout);
    
    sf("%i %i %i\n", &L, &D, &N);
    char t;
    for (int i = 0; i < D; i++) {
        for (int j = 0; j < L; j++)
              w[i][j] = getchar();
        getchar();
    }
              
    for (int k = 0; k < N; k++) {
        int last_ob = -2, last_cb = -1, l = 0, j = 0, ans = 0;
        memset(p, 0, sizeof(p));
        
        while ((t = getchar()) != '\n') {
              if (t == '(')
                 last_ob = l;
              else if (t == ')')
                 last_cb = l, j++;
              else {
                 p[j][t - 'a'] = 1;
                 if (last_ob < last_cb)
                     j++;
              }
              l++;
        }
        for (int i = 0; i < D; i++) {
            j = 0;
            for (; j < L; j++)
                if (p[j][w[i][j] - 'a'] != 1)
                   break;
                   
            if (j == L) ans++;
        }
        pf("Case #%d: %d\n", k + 1, ans);
    }
        

    sf("%i", &N);
}
