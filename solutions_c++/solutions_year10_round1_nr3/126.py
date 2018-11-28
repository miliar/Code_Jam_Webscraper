#include <iostream>
using namespace std;
const int MaxN = 1000010;
int a1, a2, b1, b2, quesnum;
long long a[MaxN];
void work()
{
    scanf ( "%d %d %d %d", &a1, &a2, &b1, &b2 );
    int i;
    long long l, r;
    long long tot;
    tot = 0;
    for (i=a1;i<=a2;i++) {
        l = a[i-1]+1;
        r = a[i-1]+i;
        if (b1<l) {
            if (b2<l) {
                tot = tot+b2-b1+1;
            }
            else {
                tot = tot+l-b1;
                if (b2>r)
                    tot = tot+b2-r;
            }
        }
        else if (b1<=r) {
            if (r<b2)
                tot= tot+b2-r;
        }
        else 
            tot = tot+b2-b1+1;
    }
    cout << tot << endl;
}
int main()
{
    freopen ( "game.in", "r", stdin );
    freopen ( "game.out", "w", stdout );
    a[0] = 0;
    for (int i=1;i<MaxN;i++) {
        a[i] = i-a[a[i-1]];
//       printf ( "%d\n", a[i] );
    }
    scanf ( "%d", &quesnum );
    for (int i=1;i<=quesnum;i++) {
        printf ( "Case #%d: ", i );
        work();
    }
    return 0;
}
