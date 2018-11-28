#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long LL;
vector<int> A,B;
int n;

int cmp(int a,int b){
    return a>b;
}
int main(){
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A.out","w",stdout);
    int cas,ic;
    scanf("%d",&cas);
    for(ic=1;ic<=cas;ic++){
        int i,t;
        scanf("%d",&n);
        A.clear();
        for(i=0;i<n;i++){
            scanf("%d",&t);
            A.push_back(t);
        }
        sort(A.begin(),A.end());
        B.clear();
        for(i=0;i<n;i++){
            scanf("%d",&t);
            B.push_back(t);
        }
        sort(B.begin(),B.end(),cmp);
        LL ans=0;
        for(i=0;i<n;i++) ans+=A[i]*B[i];
        printf("Case #%d: %I64d\n",ic,ans);
    }
    return 0;
}
