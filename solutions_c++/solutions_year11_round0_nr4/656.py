#include <cstdio>
#include <cstring>
#include <utility>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

typedef pair<int,int> PII;
PII a[1000];

int main(){
    int cs,n;
    scanf("%d",&cs);
    for(int t=1;t<=cs;t++){
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%d",&a[i].first);
            a[i].second=i;
        }
        sort(a,a+n);
        double ans=n;
        for(int i=0;i<n;i++) if(a[i].second==i) ans--;
        printf("Case #%d: %.8f\n",t,ans);
    }
}
