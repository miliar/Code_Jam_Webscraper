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
#define MAXN 1010
typedef long long int Lint;

int N;
int n[MAXN];
int t[MAXN][MAXN];
int maxcount[MAXN];
int chose[MAXN];

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
    int cas, c=0;
    freopen("cs.in", "r", stdin);
    freopen("cs.out", "w", stdout);
    scanf("%d", &cas);
    while(cas--)
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
            //cout<<chose[i]<<endl;
        }

        for(int i = N; i >= 1; i--){
            if(isin(i) && !isFirst)continue;
            isFirst = false;
            small++;
            pack(i);
            //cout<<i<<endl;
        }

        isFirst = true;
        memset(n, 0, sizeof(n));
        for(int i = 1; i <= N; i++){
            //if(used[i])continue;
            if(isin(i) && !isFirst)continue;
            isFirst = false;
            big++;
            pack(i);
            //cout<<" "<< i<<endl;
        }

        //cout<<small<<" "<<big<<endl;

        printf("Case #%d: %d\n", ++c, big - small);

    }
    return 0;
}

