//17:46 2010-05-23 begin lsy
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

const int MAXL=1000;

int c;
int ans[11][MAXL+10][MAXL+10];

int calc(int l,int p) {
    if (ans[c][l][p]>=0) return ans[c][l][p];
    if (l*c>=p) {
        ans[c][l][p]=0;
        return 0;
    }
    if (l*c*c>=p) {
        ans[c][l][p]=1;
        return 1;
    }
    int i;
    ans[c][l][p]=1000;
    for (i=l+1;i<p;i++) {
        ans[c][l][p]=min(ans[c][l][p],max(calc(l,i),calc(i,p))+1);
    }
    return ans[c][l][p];
}

int main() {
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int T;
    scanf("%d",&T);
    int l,p;
    int i;
    memset(ans,-1,sizeof(ans));
    for (i=1;i<=T;i++) {
        scanf("%d%d%d",&l,&p,&c);
        printf("Case #%d: %d\n",i,calc(l,p));
    }
    return 0;
}

        
