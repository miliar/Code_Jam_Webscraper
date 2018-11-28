#include <iostream>
using namespace std;

#define MaxN 105
#define INF 9876543

int d[MaxN][MaxN];
int t,p,q;
int a[MaxN];

int main()
{
    scanf("%d",&t);
    for (int T = 0; T < t; T++) {

        scanf("%d%d",&p,&q);

        for (int i = 0; i < q; i++) {
          scanf("%d",&a[i]);
          a[i]--;
        }
        a[q] = 0;
        a[q+1] = p-1;
        q += 2;
        sort(a, a+q);

        for (int i = 0; i < q; i++)
          for (int j = i+1; j < q; j++)
            if ( j-i == 1 || j == i ) d[i][j] = 0;
            else                      d[i][j] = INF;


        for (int j = 2; j < q; j++)
          for (int i = 0; i+j < q; i++)
            for (int k = i+1; k < i+j; k++)
               d[i][i+j] = min( d[i][i+j], d[i][k]+d[k][i+j]+(a[i+j]-a[i]-2)+ ( i == 0 ? 1 : 0 ) + ( i+j == q-1 ? 1 : 0 ) );

        printf("Case #%d: %d\n",T+1,d[0][q-1]);
    }

    return 0;
}
