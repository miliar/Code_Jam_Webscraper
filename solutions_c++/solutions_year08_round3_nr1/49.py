#include<cstdio>
#include<algorithm>
using namespace std;

const int MAXL  =   1000+10;

int P,K,L;
int fre[MAXL];

void init(){
    scanf("%d%d%d", &P, &K, &L);
    for(int i=0; i<L; ++i)scanf("%d", &fre[i]);
}

bool cmp(int a,int b){
    return a>b;
}

void solve(){
    sort(fre, fre+L, cmp);
    long long res=0;
    for(int i=0,times=1,j=0; i<L; i+=j){
        for(j=0; i+j<L && j<K; ++j)res += fre[i+j] * times;
        ++times;
    }
    printf("%I64d\n", res);
}

int main(){
    int N;
    scanf("%d", &N);
    for(int i=1; i<=N; ++i){
        init();
        printf("Case #%d: ", i);
        solve();
    }
}
