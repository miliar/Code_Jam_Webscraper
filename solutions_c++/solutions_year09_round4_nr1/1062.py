# include <iostream>
# include <cmath>
# include <cstring>
# include <string>
# include <vector>
# include <set>
# include <queue>
# include <stack>
# include <algorithm>
# include <list>
# include <map>
#include <sstream>
# define MAX 42
using namespace std;

int main()
{
    int t, n, i, j, k, w[MAX], res, temp, tt=1;
    char c[MAX][MAX+1];
    scanf("%d", &t);
    while(t--) {
        res=0;
        scanf("%d", &n);
        for (i=0; i<n; i++) {
            scanf("%s", c[i]);
            w[i]=0;
            for (j=n-1; j>=0; j--) {
                if (c[i][j]=='1') {
                    w[i]=j;
                    break;
                }
            }
        }
        for (i=0; i<n; i++) {
            for (j=i; j<n; j++) {
                if (w[j]<=i) {
                    break;
                }
            }
            res+=abs(j-i);
            for (k=j; k>i; k--) {
                temp=w[k];
                w[k]=w[k-1];
                w[k-1]=temp;
            }
        }
        printf("Case #%d: %d\n", tt++, res);
    }
    return 0;
}
