#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int MAXN  =   50;

int n;
char map[MAXN][MAXN];
int list[MAXN];

void readin(){
    memset(map, 0, sizeof(map));
    scanf("%d",&n);
    for(int i=0; i<n; ++i){
        scanf("%s", map[i]);
    }
}

void pushdown1(int p, int& res, int t){
    if( p == n - 1 ){
        res = -1;
        return;
    }
    //printf("push %d\n", p);
    
    while(list[p+1] >= list[p] || list[p+1] > t)
        pushdown1(p+1,res, t);
    if(res == -1)
        return;
    swap(list[p], list[p+1]);
    ++res;
    if(list[p+1] > p+1)
        pushdown1(p+1,res, p+1);
}

void pushdown2(int p, int& res, int t){
    if( p == n - 1 ){
        res = -1;
        return;
    }
    //printf("push %d\n", p);
    
    while(list[p+1] >= list[p] || list[p+1] > t)
        pushdown2(p+1,res, t);
    if(res == -1)
        return;
    swap(list[p], list[p+1]);
    ++res;
}

int a1(){
    for(int i=0; i<n; ++i){
        int j;
        for(j=n-1; j>=0; --j)
            if(map[i][j] == '1')
                break;
        list[i] = j;
    }
    int res = 0;
    for(int i=0; i<n; ++i){
        if(list[i] > i){
            pushdown1(i, res, i);
            if(res == -1)
                break;
        }
    }
    return res;
}

int a2(){
    for(int i=0; i<n; ++i){
        int j;
        for(j=n-1; j>=0; --j)
            if(map[i][j] == '1')
                break;
        list[i] = j;
    }
    int res = 0;
    for(int i=n-1; i>=0; --i){
        if(list[i] > i){
            pushdown1(i, res, i);
            if(res == -1)
                break;
        }
    }
    return res;
}

int a3(){
    for(int i=0; i<n; ++i){
        int j;
        for(j=n-1; j>=0; --j)
            if(map[i][j] == '1')
                break;
        list[i] = j;
    }
    int res = 0;
    for(int i=0; i<n; ++i){
        if(list[i] > i){
            pushdown2(i, res, i);
            if(res == -1)
                break;
        }
    }
    return res;
}


typedef int(*F)();
F algo[] = {a1, a2, a3};

bool check(){
    for(int i=0; i<n; ++i)
        if(list[i] > i)
            return false;
    return true;
}

void solve(){
    int res = algo[0]();
    
    for(int i=1; i<sizeof(algo) / sizeof(algo[0]); ++i){
        res = min(res, algo[i]());
        if(!check())
            printf("!!!\n");
    }
    printf("%d\n", res);
}

int main(){
    int t;
    scanf("%d", &t);
    for(int i=1; i<=t; ++i){
        readin();
        printf("Case #%d: ", i);
        solve();
    }
}
