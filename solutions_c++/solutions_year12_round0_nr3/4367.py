#include <iostream>

int n, m, tc, res;

void input(){
    scanf("%d %d", &n, &m);
}

void process(){
    int i, j, k, l;
    
    for(k = 1; k <= n; k *= 10);
    k /= 10;
    
    res = 0;
    for(i = n; i < m; i++){
        for(j = i + 1; j <= m; j++){
            for(l = k * (i % 10) + (i / 10); l != i; l = k * (l % 10) + (l / 10)){
                if(l == j){
                    res++;
                }
            }
        }
    }
}

void output(){
    printf("Case #%d: %d\n", tc, res);
}

int main(){
    int t;
    freopen("/Users/protos37/Documents/input.txt", "r", stdin);
    freopen("/Users/protos37/Documents/output.txt", "w", stdout);
    scanf("%d", &t);
    for(tc = 1; tc <= t; tc++){
        input();
        process();
        output();
    }
    return 0;
}