#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
const int MAXN = 3;

int C, N;
long long T[MAXN];

long long gcd(long long a, long long b)
{ return (b!=0)?gcd(b,a%b):a; }

int main()
{
    freopen("B-small.in","r",stdin);
    freopen("B-small.out","w",stdout);
    scanf("%d", &C);
    for(int cas = 1; cas <= C; cas++){
        scanf("%d", &N);
        long long D = 0;
        for(int i=0; i<N; i++){
            scanf("%I64d", &T[i]);
            for(int j=0; j<i; j++){
                D = gcd(abs(T[i]-T[j]), D);
            }
        }
        long long ans = (D-T[0]%D)%D;
        printf("Case #%d: %I64d\n", cas, ans);
    }
    return 0;
}

