#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int get() {
    int x;
    scanf("%d",&x);
    return x;
}

void go() {
    int n = get();
    vector<int> m(1 << n);
    generate(m.begin(),m.end(),get);
    vector<int> cost(1 << n);
    int add=(1 << (n-1));
    while(add!=0) {
        generate(cost.begin()+add,cost.begin()+2*add,get);
        add>>=1;
    }
    int total=0;
    for(int i=0;i<cost.size();i++)total+=cost[i];
    vector<vector<int> > who(1<<n);
    for(int i=0;i<(1<<n);i++) {
        int index=1<<n;
        index+=i;
        index>>=1;
        while(index) {
            who[index].push_back(i);
            index>>=1;
        }
    }
    vector<vector<int> > dp(1<<n, vector<int>(12));
    for(int i=(1<<n);--i;) {
        for(int j=0;j<11;j++) {
            if(i<(1<<(n-1))) {
                dp[i][j]=dp[i*2][j]+dp[i*2+1][j];
            } else {
                dp[i][j]=0;
            }
            bool impossible=false;
            bool canPick=true;
            for(int k=0;k<who[i].size();k++) {
                if(m[who[i][k]]<j) {
                    impossible=true;
                }
                if(m[who[i][k]]==j) {
                    canPick=false;
                }
            }
            if(impossible)dp[i][j]=0;
            else {
                if(canPick) {
                    // whee! we can pick this one!
                    if(i<(1<<(n-1))) {
                        dp[i][j]=max(dp[i][j],dp[i*2][j+1]+dp[i*2+1][j+1]+cost[i]);
                    } else {
                        dp[i][j]=max(dp[i][j],cost[i]);
                    }
                }
            }
        }
    }
    printf("%d\n",total-dp[1][0]);
}

int main() {
    int c = get();
    for(int i=0;i<c;i++) {
        printf("Case #%d: ",1+i);
        go();
    }
}
