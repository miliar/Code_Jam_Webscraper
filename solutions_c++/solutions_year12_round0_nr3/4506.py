#include <stdio.h>
#include <iostream>
using namespace std;
int check(int x, int y) {
    int p = 1;
    while (p<=x) p*=10;
    p/=10;
    int t= x;
    while (1) {
        t = (t % 10 * p) + t/10;
        if (t==y) return 1;
        if (t==x) return 0;
    }
}
int main() {
    int n;
    cin >> n ;
    for (int i = 1; i<=n ; i++) {
        int ans = 0 ;
        int a,b;
        cin >> a >> b;
        for (int x = a; x < b; x++)
            for (int y = x+1; y <=b; y++)
                 ans += check(x,y);
        cout << "Case #"<<i<<": "<<ans<<endl;
    }
}
