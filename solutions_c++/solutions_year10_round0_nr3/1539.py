#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

const int MAXN  =       1000+10;

int g[MAXN * 2];
long long sum[MAXN * 2];
int next[MAXN];
bool vist[MAXN];
int N,R,k;

void input(){
    scanf("%d%d%d", &R, &k, &N);
    for(int i=1; i<=N; ++i)
        scanf("%d", &g[i]);
}

long long solve(){
    for(int i=1; i<=N; ++i)
        g[N+i] = g[i];

    sum[0] = 0;
    for(int i=1; i<=N+N; ++i)
        sum[i] = sum[i-1] + g[i];

    if(sum[N] <= k)
        return sum[N]*R;

    memset(next, -1, sizeof(next));
    for(int l=1,r=1; l<=N; ++l){
        while(sum[r] - sum[l-1] <= k)
            ++r;
        next[l] = r;
        //cout<<"next["<<l<<"] "<<next[l]<<endl;
    }
    
    long long res = 0;
    for(int i=0,p=1; i<R; ++i){
        res += sum[next[p]-1] - sum[p-1];
        p = next[p] > N? next[p] - N: next[p];
    }
    return res;
    /*
    memset(vist, false, sizeof(vist));
    int rn=0;
    long long rc=0;
    for(int i=1; !vist[i]; i=next[i]>N? next[i]-N: next[i]){
        vist[i] = true;
        ++rn;
        rc += sum[next[i]-1] - sum[i-1];
    }

    cout<<"circle "<<rn<<" "<<rc<<endl;

    long long res = rc * (R / rn);
    R %= rn;

    for(int i=1,j=0; j<R; ++j, i=next[i]>N? next[i]-N: next[i])
        res += sum[next[i]-1] - sum[i-1];

    return res;*/
}

int main(){
    int t;
    scanf("%d", &t);
    for(int i=1; i<=t; ++i){
        input();
        cout<<"Case #"<<i<<": "<<solve()<<endl;
    }
}

