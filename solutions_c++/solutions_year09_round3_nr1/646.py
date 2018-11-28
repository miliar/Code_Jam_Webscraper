/*
  ID: nigo1
  LANG: C++
  TASK:
*/
#include <iostream>
#include <stdio.h>

#define pf printf
#define sf scanf
#define TIME pf("%f\n", (double)clock()/CLOCKS_PER_SEC);

using namespace std;

int N, n;
char c[64];
int used[256];
long long unsigned minn;

int main()
{
    freopen ("A-large.in", "r", stdin);
    freopen ("A-large.out", "w", stdout);
    
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> c;
        
        memset(used, -1, sizeof(used));
        int cnt = 0;
        n = strlen(c);
        used[c[0]] = 1;
        for (int j = 1; j < n; j++)
            if (used[c[j]] == -1)  
               if (cnt == 1) used[c[j]] = ++cnt, cnt++;
               else used[c[j]] = cnt++;
        if (cnt <= 1) cnt = 2;
        
        long long unsigned b = 1, res = 0;
        for (int j = n - 1; j >= 0; j--)
            res += b*used[c[j]], b*=cnt;
            
        pf ("Case #%i: %llu\n", i + 1, res);
    }
    

    sf("%i", &N);
}
