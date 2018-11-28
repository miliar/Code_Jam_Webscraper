#include <cstdio>
#include <cstring>
#include <utility>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

const int INF = 1070000000;

int main(){
    int cs;
    scanf("%d",&cs);
    for(int t=1;t<=cs;t++){
        int n,k,sum=0,bit=0,lo=INF;
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%d",&k);
            sum+=k;
            bit^=k;
            lo=min(lo,k);
        }
        printf("Case #%d: ",t);
        if(bit) puts("NO"); else printf("%d\n",sum-lo);
    }
}
