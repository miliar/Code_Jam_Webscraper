
#include <cstdlib>
#include <cstdio>
#include <cstring>
//#include <string.h>

using namespace std;

int numOfDigit(int n)
{
    char str[8];
    sprintf(str, "%d", n);
    return strlen(str);
}

int rn(int num, int n)
{
    char str[8];
    char str1[8];
    sprintf(str, "%d", num);
    char len = strlen(str);
    
    memset(str1, 0, 8);
//    str1[0] = str[len - 1];
    strncpy(str1, &str[len - n], n);
    strcat(str1, str);
    str1[len] = 0;
    return atoi(str1);
}

int main(int argc, const char * argv[])
{
    int cn;
    int f, t;
    int nd;
    int r;
    int nra[7],nr;
    
    
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
    
    scanf("%d\n", &cn);
    for (int ci = 1; ci <= cn; ci++) {
        r = 0;
        scanf("%d %d", &f, &t);
        nd = numOfDigit(f); 
        for (int i = f; i < t; i++) {
            int tn = i;
            nr = 0;
            for (int j = 1; j < nd; j++) {
                tn = rn(i, j);
                int ignore = 0;
                if (i < tn && tn <= t) {
                    for (int k = 0; k < nr; k++) {
                        if (nra[k] == tn) {
                            ignore = 1;
                            break;
                        }
                    }
                    if (!ignore) {
                        nra[nr] = tn;
                        nr++;
                        r++;
                    }
                }
            }
        }
        printf("Case #%d: %d\n", ci, r);
    }
    return 0;
}
