#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#define LL long long
using namespace std;

int A,B;
int v[2000005],stat[5],st;
struct Node {
        int i, j;
};
bool cmp(Node a, Node b) {
        if(a.i==b.i) return a.j<b.j;
        return a.i<b.i;
}
Node node[500];
LL cal()
{
        int i, j, k, exp, len=0;
        LL cnt,ans=0;
        memset(v,0,sizeof v);
        int sst=0;
        j=A;
        exp=1;
        while(j) { j/=10; ++len; exp*=10; }
        exp/=10;
        for(i = A; i <= B; i++){
                if(v[i]) continue;
                j=i;
                cnt=1;
                for(k=1;k<len;k++) {
                        j = (j%10)*exp+j/10;
                        if(j<=i || j>B || v[j]) continue;
                        ++cnt;
                        v[j]=1;
                }
                if(cnt) ans+=cnt*(cnt-1)/2;
        }
        return ans;
}
int main()
{
        int i,t,cas=0;
        freopen("C-large.in","r",stdin);
        freopen("C.out","w",stdout);
        scanf("%d",&t);
        while(t--){
                scanf("%d%d",&A,&B);
                printf("Case #%d: ",++cas);
                printf("%I64d\n", cal());

        }
        return 0;
}

