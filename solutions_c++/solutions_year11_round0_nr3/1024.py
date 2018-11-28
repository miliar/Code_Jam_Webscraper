///  Mahesh
#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int a[2000], v1[2000], v2[2000];
int add(int c){
    int ans  = 0;
    for(int i=0;i<c;i++) ans+=v1[i];
    return ans;
}
int main()
{
    freopen("1.txt", "r", stdin);
    freopen("jam.txt", "w", stdout);

    int t;
    cin>>t;
    for(int T=0;T<t;T++){
        int n; cin>>n;
        int x = 0, sum =0;
        for(int i=0; i<n; i++){
            cin>>a[i];
            x^=a[i];
            sum += a[i];
        }
        if (x) printf("Case #%d: NO\n", T+1);
        else {
            int ans = sum - *min_element(a, a+n);
            printf("Case #%d: %d\n", T+1, ans);
        }
    }
    return 0;
}
