#include<algorithm>
#include<cstdio>
const int L=105;
const int NO_ANS=-1;
using namespace std;

int N,S,P;
int p[L];
int dp[L][L];

int no_surprising(int k) {
    return k/3+(k%3!=0);
}

int surprising(int k) {
    if(k==0 || k==1) return -1;
    return 1+(1+k)/3;
}

int go(int n,int s) {
    if(s<0) return NO_ANS;
    if(n<0) { 
        if(s==0) return 0;
        return NO_ANS;
    }

    if(dp[n][s]!=-1)
        return dp[n][s];

    int v1 = no_surprising(p[n]);
    int v2 = surprising(p[n]);
    int res = NO_ANS;
    if(v1!=-1) {
        int r = go(n-1,s);
        if(r!=NO_ANS)
            res = max(res, r+(v1>=P));
    }

    if(v2!=-1) {
        int r = go(n-1,s-1);
        if(r!=NO_ANS)
            res = max(res, r+(v2>=P));
    }

    return dp[n][s] = res;
}

int main () {
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++) {

        scanf("%d%d%d",&N,&S,&P);
        for(int i=0;i<N;i++)
            scanf("%d",&p[i]);

        memset(dp,-1,sizeof(dp));
        printf("Case #%d: %d\n",t,max(0,go(N-1,S)));
    }
}
