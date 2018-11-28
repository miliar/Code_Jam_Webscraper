#include <iostream>
#include <algorithm>
using namespace std;
int a[15];
int b[2][5000];
int c;
int main(){
    a[0] = 1;
    for (int i = 1; i < 12; ++i)
        a[i] = a[i-1]*2;
    int t,o;
    cin >> t;
    o = t;
    while (t--){
        cout << "Case #" << o-t << ": ";
        int n;
        cin >> n;
        for (int i = 0; i < a[n]; ++i)
            cin >> b[0][i];
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= a[n-i]; ++j)
                cin >> c;
        int ans = 0;
        for (int j = n-1; j >=0; --j)
            for (int i = 0; i < a[j]; ++i)
                if (b[(n-j+1)%2][i*2]>0 && b[(n-j+1)%2][i*2+1]>0)
                    b[(n-j)%2][i] = min(b[(n-j+1)%2][i*2],b[(n-j+1)%2][i*2+1])-1;
                else{
                    b[(n-j)%2][i] = 0;
                    ++ans;
                }
        cout << ans <<endl;
    }
}
