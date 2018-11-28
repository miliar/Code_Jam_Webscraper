#include <algorithm>
#include <cstdio>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

typedef queue<int> QI;
typedef vector<int> VI; 
typedef unsigned long long ULL;
typedef vector<ULL> VULL;

#define D 1

void doit(int kase) {
    int R,k,N;
    scanf("%d %d %d", &R, &k, &N);
    VI v;
    QI q;
    for(int i=0;i<N;i++) {
        int in;
        scanf("%d",&in);
        v.push_back(in);
        q.push(in);
    }
    VULL w;
    ULL earn = 0, kap=0;
    int pos=0,round=0;
    do{
        ULL to_add =(ULL) q.front();
        VI push;
        while(kap + to_add <= (ULL) k ) {
if(D)       fprintf(stderr,"kap: %llu, to_add: %llu\n",kap,to_add);
            q.pop();
            push.push_back(to_add);
            kap+=to_add;
            pos++;
            if(q.size()==0) break;
            to_add = q.front();
        }
        for(int i=0;i<(int)push.size();i++) q.push(push[i]);
        earn+=kap;
        w.push_back(earn);
        round++;
        kap = 0;
    }while((round < R) && ((pos%N)!=0));
if(D)fprintf(stderr, "round: %d, pos: %d\n",round,pos);
if(D)for(int i=0;i<round;i++) fprintf(stderr, "w[%d] = %llu\n",i,w[i]);
    ULL sum = (R/round) * w[round-1] + w[R%round] * ((R%round)>0);
    printf("Case #%d: %llu\n",kase,sum);
}

void doit2(int kase) {
    printf("Case #%d: ",kase);
    int gi[1024];
    int R,k,N;
    scanf("%d %d %d", &R, &k, &N);
    for(int i=0;i<N;i++) scanf("%d", &gi[i]);
    int pointer = 0;
    int K=0;
    ULL earn=0;
    for(int rnd = 0; rnd < R; rnd++){
        for(int i=0;i<N;i++) {
            int p = gi[pointer % N];
            if(K+p>k) break;
            pointer++;
            K+=p;
        }
        earn+=(ULL)K;
        K = 0;
    }
    printf("%llu\n",earn);
}

int main(){
    int N;
    cin >> N;
    for(int i=1;i<=N;i++) doit2(i);
}
