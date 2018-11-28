#include <iostream>
using namespace std;
int low[1000001];
int main() {
    low[1]=1;
    low[2]=2;
    int upto = 3;
    for (int i=2; i<=1000000; i++) {
        while (upto<low[i]+i && upto<=1000000) {
            low[upto]=i;
            upto++;
        }
    }
    int T; scanf("%d",&T); for (int t=1; t<=T; t++) {
        printf("Case #%d: ",t);
        int A1,A2,B1,B2; scanf("%d %d %d %d",&A1,&A2,&B1,&B2);
        
        long long bad = 0;
        for (int i=A1; i<=A2; i++) {
            long long llow = max(B1,low[i]);
            long long hhigh = min(B2,low[i]+i-1);
            if (hhigh>=llow) bad += hhigh-llow+1;
        }
        long long good = ((long long)(A2-A1+1))*(B2-B1+1);
        printf("%I64d\n",good-bad);
    }
}
