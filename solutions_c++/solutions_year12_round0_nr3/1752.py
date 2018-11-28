#include <stdio.h>
#include <string.h>
#include <set>

using std::set;

int A, B;
long long int ans;
bool used[2000010];

int check(int now) {
    char sa[10], sb[10];

    int len = 0;
    int x = now;
    while( x > 0 ) {
        sa[len++] = x%10;
        x /= 10;
    }
    //printf("len = %d\nnow = %d\n",len, now);
    int count = 0;
    set<int> S;
    for(int i=1;i<len;++i) {
        for(int j=i;j<len;++j)
            sb[j-i] = sa[j];
        for(int j=0;j<i;++j)
            sb[len-i+j] = sa[j];
        sb[len] = '\0';
        int y = 0;
        for(int j=len-1;j>=0;--j)
            y = y*10+sb[j];
        //printf("%d: %d\n", i, y);
        if(y < A || y > B || y <= now) continue;
        if(S.find(y) != S.end())    continue;
        S.insert(y);
        ++count;
    }
    return count;
}

int main() {
    int t, cases=0;

    scanf("%d",&t);
    while(t--) {
        ans = 0;
        scanf("%d%d",&A,&B);
        for(int i=A;i<=B;++i) {
            ans += check(i);
            //printf("%d\n", ans);
        }
        printf("Case #%d: %I64d\n", ++cases, ans);
    }

    return 0;
}
