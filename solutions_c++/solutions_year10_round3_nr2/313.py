#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

int main(void)
{
    int test;
    cin >> test;
    for (int ti=1; ti<=test; ++ti) {
        double l, p, c;
        cin >> l >> p >> c;
        double ans,logdiv,logc,log2;
        logdiv = log(p/l);
        logc = log(c);
        log2 = log(2);
        ans = log(logdiv/logc) / log2;
        double intans;
        intans = ceil(ans);
        //cout << ans << " " << intans << endl;
        if (intans < 0) intans = 0;
        //cout << logdiv << " " << logc << " " << logdiv / logc << " " << log2 << " " << ans << endl;
        cout << "Case #" << ti << ": " << intans << endl;
    }
    return 0;
}
