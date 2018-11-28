#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <cstring>
#include <map>
#include <algorithm>
#include <memory.h>

using namespace std;
#define MAXL 1010
typedef long long int Lint;

int N;
int n[MAXL];
int t[MAXL][MAXL];
int maxcount[MAXL];
int chose[MAXL];

void pack2(int c){
    int origin = c;
    if(c == 1){
        return;
    }
    for(int i = 2; i <= c; i++){
        int cnt = 0;
        while((c % i) == 0 && c >= i){
            c = c / i;
            cnt++;
        }
        if(cnt > t[c][i])
            t[c][i] = cnt;
        if(cnt > maxcount[i]){
            maxcount[i] = cnt;
            chose[i] = origin;
        }
        if(c == 1)return;
         }
}

void pack(int c){
    if(c == 1){
        return;
    }
    for(int i = 2; i <= c; i++){
        int cnt = 0;
        while((c % i) == 0 && c >= i){
            c = c / i;
            cnt++;
        }
        if(cnt > n[i])
            n[i] = cnt;
        if(c == 1)return;
    }
}

bool isin(int c){
    if(c == 1){
        return true;
    }
    for(int i = 2; i <= c; i++){
        int cnt = 0;
        while((c % i) == 0 && c >= i){
            c = c / i;
            cnt++;
        }
        if(cnt > n[i])
            return false;
        if(c == 1)return true;
    }
    return true;
}

int main()
{
    int cases;
    int Case = 0;
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.txt", "w", stdout);
    scanf("%d", &cases);
    while(cases--)
    {
        scanf("%d", &N);
        memset(t, 0, sizeof(t));
        memset(maxcount, 0, sizeof(maxcount));
        memset(chose, 0, sizeof(chose));
        for(int i = 1; i <= N; i++){
            pack2(i);
        }

        int big = 0;
        int small = 0;
        bool isFirst = true;
        memset(n, 0, sizeof(n));
        
        for(int i = 1; i <= N; i++){
            if(maxcount[i] == 0)continue;
            if(isin(chose[i]) && !isFirst)continue;
            isFirst = false;

            small++;
            pack(chose[i]);
        }

        for(int i = N; i >= 1; i--){
            if(isin(i) && !isFirst)continue;
            isFirst = false;
            small++;
            pack(i);
        }

        isFirst = true;
        memset(n, 0, sizeof(n));
        for(int i = 1; i <= N; i++){
            if(isin(i) && !isFirst)continue;
            isFirst = false;
            big++;
            pack(i);
        }


        printf("Case #%d: %d\n", ++Case, big - small);

    }
    return 0;
}
