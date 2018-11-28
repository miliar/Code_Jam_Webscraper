
#include <cstdlib>
#include <cstdio>


int main(int argc, const char * argv[])
{
    int cn;
    int dn, sn, bn;
    int r;
    int n;
    
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
    
    scanf("%d\n", &cn);
    for (int ci = 1; ci <= cn; ci++) {
        r = 0;
        scanf("%d %d %d", &dn, &sn, &bn);
        for (int i = 0; i < dn; i++) {
            scanf("%d", &n);
            int d = n / 3;
            int m = n % 3;
            if (d >= bn) {
                r++;
            }
            else if (d + 1 == bn && m > 0) {
                r++;
            }
            else if (d + 1 == bn && m == 0 && d > 0 && sn > 0) {
                r++;
                sn--;
            }
            else if (d + 2 == bn && m == 2 && sn > 0) {
                r++;
                sn--;
                }
        }
        printf("Case #%d: %d\n", ci, r);
    }
    return 0;
}

