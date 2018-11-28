#include <cstdio>
#include <cstring>

int T , A , B;
double P[16] , p[4] , sum , ans;
int a[4];

int main () {
    freopen("password.in","r",stdin);
    freopen("password.out","w",stdout);
    
    scanf("%d\n",&T);
    int i , j , k , l , t , u;
    for (l = 0;l < T;l++) {
        printf("Case #%d: ",l+1);
        scanf("%d %d\n",&A,&B);
        memset(P,0,sizeof(P));
        for (i = 0;i < A;i++) scanf("%lf\n",&p[i]);
        t = 1;
        for (i = 0;i < A;i++) t *= 2;
        for (i = 0;i < t;i++) {
            memset(a,0,sizeof(a));
            k = i;
            for (j = A-1;k;j--,k/=2)
                a[j] = k % 2;
            P[i] = 1.0;
            for (j = 0;j < A;j++)
              if (!a[j]) P[i] *= p[j];
                else P[i] *= (1-p[j]);
        }
        ans = 10000000.0*10000000.0;
        for (k = 0;k <= A;k++) {
            sum = 0;
            for (i = 0;i < t;i++) {
                memset(a,0,sizeof(a));
                u = i;
                for (j = A-1;u;j--,u/=2)
                    a[j] = u % 2;
                bool flag = true;
                for (j = 0;j < A-k;j++)
                  if (a[j]) flag = false;
                if (flag) sum += P[i]*(B-(A-k)+1+k);
                  else sum += P[i]*(B-(A-k)+2+B+k);
            }
            if (ans > sum) ans = sum;
        }
        sum = 0;
        for (i = 0;i < t;i++)
          sum += P[i]*(B+2);
        if (sum < ans) ans = sum;
        printf("%.6f\n",ans);
    }
    return 0;
}
