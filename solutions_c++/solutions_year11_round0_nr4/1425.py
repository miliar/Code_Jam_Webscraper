#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 11;
int num[MAXN];
bool table[MAXN];
double DP[MAXN];
double fr[MAXN], c[MAXN][MAXN];

double C(int a, int b)
{
    if(b > a) return 0;
    if(b==0||a==b) return 1;
    if(c[a][b] != 0) return c[a][b];
    return c[a][b] = C(a-1,b)+C(a-1,b-1);
}

double fract(int n)
{
    if(n <= 1) return 1;
    if(fr[n] != 0) return fr[n];
    return fr[n] = n*fract(n-1);
}

double permu(int n)
{
    if(n<1) return 1;
    if(n==1) return 0;
    double ret = 0, sign = 1;
    for(int i = n; i>=0; i--)
        ret += sign*C(n,n-i)*fract(i), sign = -sign;
        
    return ret;
}

int main()
{
    freopen("out.txt", "w", stdout); 
    int T, N;
    scanf("%d", &T);
    DP[0] = DP[1] = 0;
    for(int i = 2; i < MAXN; i++)
    {
        DP[i] = 0;
        for(int j = 0; j < i; j++)
            DP[i] += DP[j]*C(i,i-j)*permu(j)/fract(i);
        DP[i] += 1;
        DP[i] /= (1-permu(i)/fract(i));
    }
    
    for(int t = 1; T--; ++t)
    {
        memset(table, 0, sizeof(table));
        scanf("%d", &N);        
        int cnt = 0;
        for(int i = 0; i < N; i++)
        {
            scanf("%d", &num[i]);
            if(num[i] != i+1) ++cnt;
        }
              
        
        printf("Case #%d: %.6f\n", t, DP[cnt]);
    }
    
    return 0;
}
