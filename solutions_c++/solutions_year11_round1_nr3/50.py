#include <iostream>
#include <cstdio>
#include <memory.h>
#include <cstring>
#include <cmath>

#include <vector>
#include <deque>
#include <queue>

#define ABS(a) ((a)<0?-(a):(a))
#define SIGN(a) ((a)<0?-1:((a)>0?1:0))
#define SQR(a) ((a)*(a))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))

#define REP(i, n) for(int i=0; i<(n); ++i)
#define FOR(i, a, b) for(int i=(a); i<(b); ++i)

#define in ({int x;scanf("%d", &x);x;})

#define PI   (3.1415926)
#define INF  (2147483647)
#define INF2 (1073741823)
#define EPS  (0.000001)
#define y1 stupid_cmath

typedef long long LL;

using namespace std;

int N, M, c[99], s[99], t[99], maxres;
bool cards[99];

void rec(int turn, int sum){
    if(turn==0){
        maxres=MAX(maxres, sum);
        return ;
    }
    int i, s1=-1, s0=-1;
    bool f=false;
    for(i=0;i<M;++i){
        f|=cards[i];
        if(cards[i] && t[i]) break;
        if(cards[i])
        if(c[i]==0){
            if(s0<0 || s[s0]<s[i]) s0=i;
        }else{
            if(s1<0 || s[s1]<s[i]) s1=i;
        }
    }
    if(!f){
        maxres=MAX(maxres, sum);
        return ;
    }
    f=false;
    if(i<M){
        cards[i]=false;
        if(c[i]){
            if(N<M){
                cards[N]=true;
                ++N;
                f=true;
            }
        }
        rec(turn-1+t[i], sum+s[i]);
        if(f){
            --N;
            cards[N]=false;
        }
        cards[i]=true;
        return ;
    }

    if(s0<0) s0=s1;
    if(s1>=0 && s[s0]<=s[s1]) s0=s1;

        cards[s0]=false;
        f=false;
        if(N<M && c[s0]){
            cards[N]=true;
            ++N;
            f=true;
        }
        rec(turn-1, sum+s[s0]);
        if(f){
            --N;
            cards[N]=false;
        }
        cards[s0]=true;

    if(s1>=0 && s1!=s0){

        cards[s1]=false;
        f=false;
        if(N<M && c[s1]){
            cards[N]=true;
            ++N;
            f=true;
        }
        rec(turn-1, sum+s[s1]);
        if(f){
            --N;
            cards[N]=false;
        }
        cards[s1]=true;
    }
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    int NN, i, j;
    cin>>NN;
    for(int ii=1;ii<=NN;++ii){

        cin>>N;
        for(i=0;i<N;++i) cin>>c[i]>>s[i]>>t[i];
        cin>>M;
        M+=N;
        for(;i<M;++i) cin>>c[i]>>s[i]>>t[i];

        maxres=0;
        memset(cards, 0, sizeof(cards));
        for(i=0;i<N;++i) cards[i]=true;
        rec(1, 0);

        printf("Case #%d: %d\n", ii, maxres);

    }

	return 0;
}
