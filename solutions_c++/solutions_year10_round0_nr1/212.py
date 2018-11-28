#include <iostream>
using namespace std;
int main()
{
    int i, flag, n, k, quesnum;
//    freopen ( "snapper.in", "r", stdin );
//    freopen ( "snapper.out", "w", stdout );
    scanf ( "%d\n", &quesnum );
    for (int ques=1;ques<=quesnum;ques++) {
        scanf ( "%d %d", &n, &k );
        flag = 1;
        for (i=0;i<n;i++) {
            if (k%2==0) {
                flag = 0;
                break;
            }
            k = k/2;
        }
        if (flag) {
            printf ( "Case #%d: ON\n", ques );
        }
        else {
            printf ( "Case #%d: OFF\n", ques );
        }
    }
    return 0;
}
