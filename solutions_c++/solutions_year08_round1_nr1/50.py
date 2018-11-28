#include <algorithm>
#include <cstdio>
#include <iostream>
using namespace std;

long long a[1010],b[1010];
int tot,n;

int main(){
    cin >> tot;
    for (int cases=0;cases<tot;++cases){
        scanf("%d",&n);
        for (int i=0;i<n;++i) cin >> a[i];
        for (int i=0;i<n;++i) cin >> b[i];
        sort(a,a+n);
        sort(b,b+n);
        long long ans=0;
        for (int i=0;i<n;++i)
            ans+=a[i]*b[n-i-1];
        printf("Case #%d: ",cases+1);
        cout << ans << endl;
    }
    return 0;
}
