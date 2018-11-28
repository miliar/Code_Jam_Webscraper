#include <cstdio>
#include <string.h>
#include <algorithm>
using namespace std;

int main(){
        int T, ca=0;
        scanf("%d", &T);
        while (T--){
                int p, q, a[110], d[110][110];
                pair<int ,int> st[110], ost[110];
                memset(a, 0, sizeof(a));
                memset(d, 0, sizeof(d));
                scanf("%d%d", &p, &q);
                for (int i=0; i<q; i++) 
                        scanf("%d", &a[i]);
                a[q++] = 0;
                a[q++] = p+1;
                sort(a, a+q);


                for (int len=0; len<q; len++)
                        for (int i=0; i+len<q; i++){
                                int j=i+len;
                                if (len==1) d[i][j] = a[j]-a[i]-1;
                                else{
                                        d[i][j] = 2147483647;
                                        for (int k=i+1; k<j; k++)
                                                d[i][j] = min(d[i][k] + d[k][j] + a[j]-a[i]-1, d[i][j]);
                                }
                        }

                printf("Case #%d: %d\n", ++ca, d[0][q-1]-p);
        }
        return 0;
}
