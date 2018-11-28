#include<iostream> 
#include<cstdio> 
#include<algorithm> 
#include<cstring> 
#include<string>
#include<cmath> 
#include<vector> 
#include<queue> 
#include<map>
#include<ctime>
#include<set>
typedef long long lld; 
using namespace std; 
#define debug(x) cout<<#x<<"="<<x<<endl;
#define here cout<<"_______________here "<<endl;
#define clr(NAME,VALUE) memset(NAME,VALUE,sizeof(NAME)) 
#define MAX 0x7f7f7f7f 
#define N 16000010
#define PRIME 999983

int main()
{
    //#ifndef ONLINE_JUDGE
    //freopen("a", "r", stdin);
    //#endif
    int T;
    scanf("%d", &T);
    int cas = 0;
    int n, s, p;
    int a[200];
    int ans;
    int tmp;
    while (T--) {
        ans = 0;
        tmp = 0;
        scanf("%d%d%d", &n, &s, &p);
        for (int i=0; i<n; ++i) {
            scanf("%d", &a[i]);
            if (a[i] == 0) {
                continue;
            }
            if (a[i] >= p*3 - 2) {
                ans++;
            } else if(a[i] >= p*3 - 4) { 
                tmp++;
            }
        }
        printf("Case #%d: ", ++cas);
        if (p == 0) {
            printf("%d\n", n);
        } else {
            printf("%d\n", ans + min(tmp, s));
        }
    }
}
