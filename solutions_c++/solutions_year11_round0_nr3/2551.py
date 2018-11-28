#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
using namespace std;

int a[2000];
int main(){
        int t,cnt=1,n;
        scanf("%d", &t);
        while(t--){
                scanf("%d", &n);
                int ans = 0,ans2=0;
                for(int i=0; i<n;i++){
                        scanf("%d", &a[i]);
                        ans = ans^a[i];
                        ans2+=a[i];
                }
                sort(a,a+n);
                if(ans) printf("Case #%d: NO\n",cnt++);
                else printf("Case #%d: %d\n", cnt++,ans2 - a[0]);
        }
        return 0;
}
