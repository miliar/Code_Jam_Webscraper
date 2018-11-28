#include <iostream>
using namespace std;
int a[12];
int p, q;
int slv(){
    int ans = 0;
    bool used[128];
    memset(used, 0, sizeof(used));
    for ( int i = 0; i < q; ++i ){
        used[a[i]] = 1;
        int j = a[i] - 1;
        while ( j > 0 && used[j] == 0 ) {--j;++ans;}
        j = a[i] + 1;
        while ( j <= p && used[j] == 0 ){++j;++ans;}
    }
    return ans;
}
void solve(int z){
    int ans = 999999;
    cin >> p >> q;
    for ( int i = 0; i < q; ++i )
        cin >> a[i];
    do{
       ans = min(ans, slv());
    }
    while(next_permutation(a, a + q));
    cout << "Case #" << z << ": " << ans << endl;
}
int main(){
    int t;
    cin >> t;
    for ( int i = 0; i < t; ++i)
        solve(i + 1);
}
