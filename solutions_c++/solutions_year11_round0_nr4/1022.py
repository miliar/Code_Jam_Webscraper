///  Mahesh
#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    freopen("1.txt", "r", stdin);
    freopen("jam.txt", "w", stdout);
    int T; cin>>T;
    for(int t=1;t<=T;t++){
        int n, ans = 0; cin>>n;
        for(int i=0;i<n;i++){
            int x; cin>>x;
            if (x!=i+1) ans++;
        }
        printf("Case #%d: %d.000000\n", t, ans);
    }
    return 0;
}
