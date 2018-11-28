#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

#define REP(i,n) for(int i=0;i<n;++i)
#define VAR(v, n) typeof(n) v = (n)
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)

using namespace std;

int count(vector<int> &v,int P) {
    int c[1000];
    int out=0;
    memset(c,0,sizeof(c));
    FOREACH(it,v) {
        c[*it]=1;
        for(int i=*it-1;i>0&&c[i]==0;--i) out++;
        for(int i=*it+1;i<=P&&c[i]==0;++i) out++;
    }
    return out;
}

int main() {
    int T;
    scanf("%d",&T);
    REP(test,T) {
        vector<int> v;
        int P,Q;
        int p;
        int coins=-1;
        scanf("%d%d",&P,&Q);
        v.clear();
        REP(i,Q) {
            scanf("%d",&p);
            v.push_back(p);
        }
        sort(v.begin(),v.end());
        do {
            p=count(v,P);
            if(coins==-1||p<coins) {
                coins=p;
            }
        } while(next_permutation(v.begin(),v.end()));
        printf("Case #%d: %d\n",test+1,coins);
    }

    return 0;
}
