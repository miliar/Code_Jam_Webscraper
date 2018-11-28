#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cmath>
#include <set>
using namespace std;

int a[20], len;

void change(int x){
    int i = 1, j;

    len = 1;
    while(x / i >= 10){
        i = i * 10;
        len++;
    }

    int aa;
    aa = 10;
    for(j = 0; j < len; ++j){
        a[j] = a[j + len] = x / i;
        x = x % i;
        i = i / 10;
    }

    printf("");
}

int ans;

set<pair<int, int> > S;

int IsOK(int A, int B, int n){
    int i, j, t;
    int flag = 0;
    for(i = 1; i < len; ++i){
        t = 0;
        if(a[i] == 0){
            continue;
        }
        for(j = 0; j < len; ++j){
            t = t * 10 + a[i + j];
        }
        if(n < t && t <= B){
            S.insert(make_pair(n, t));
        }
    }
    return 0;
}

int main()
{
    int T;
    freopen("C-large.in", "r", stdin);
    //freopen("3.txt", "w", stdout);
    scanf("%d", &T);
    int cas = 1;
    while(T--){
        int A, B;
        scanf("%d %d", &A, &B);
        int i;
        ans = 0;
        S.clear();
        for(i = A; i <= B; ++i){
            change(i);
            if(IsOK(A, B, i)){
                ;
            }
        }
        printf("Case #%d: ", cas++);
        printf("%d\n", S.size());
    }
    return 0;
}