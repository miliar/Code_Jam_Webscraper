#include <iostream>

using namespace std;

#define forn(i,n) for (int (i)=0; (i) < (n); (i)++)

int tt, n, k;
int d, res;

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> tt;
    forn(t,tt)
    {
        cin >> n >> k;
        d = 2<<(n-1);
        res = (((k%d)+d)%d)-d;
        cout << "Case #" << t+1 << ": ";
        if (res == -1) cout << "ON";
        else cout << "OFF";
        cout << endl;
    }
    return 0;
}
