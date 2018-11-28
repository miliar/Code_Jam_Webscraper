#include<iostream>
#include<algorithm>
using namespace std;
int f[1<<20];
int A1, A2, B1, B2;
typedef long long  LL;
int main()
{
    int i, j;
    f[0] = 0;
    f[1] = 2;
    f[2] = 4;
    f[3] = 5;
    for(i = 4; i <= 1000000; ++i)
    {
        j=upper_bound(f, f + i, i) - f;
        f[i] = i + j;
        //printf("%d %d\n", i, f[i]);
    }
    int t, cs  = 0;
    LL res;
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d%d%d%d", &A1, &A2, &B1, &B2);
        res = 0;
        for(i =  A1; i <= A2; ++i)
        {
            if(B1 >= f[i]) res += B2 - B1  + 1;
            else if(B2 >= f[i])
               res += B2 - f[i] + 1;
            
        }
        swap(A1, B1);
        swap(A2, B2);
        for(i =  A1; i <= A2; ++i)
        {
            if(B1 >= f[i]) res += B2 - B1  + 1;
            else if(B2 >= f[i])
               res += B2 - f[i] + 1;
            
        }
        printf("Case #%d: %I64d\n", ++cs, res);
    }
              
    //while(1);
}
