#include<iostream>
using namespace std;
int f[512][128];
int N;
char A[] = {"#welcome to code jam"};
char B[1024];
int main()
{
    int i, j, k, cs = 0;
    freopen("C_L.in", "r", stdin);
    freopen("C_L.out", "w", stdout);
    
    scanf("%d", &N);
    getchar();
    while(N--)
    {
        gets(B + 1);
        memset(f, 0, sizeof(f));
        f[0][0] = 1;
        
        for(i = 1; B[i]; i++)
        {
            for(j = 1; A[j]; j++)
            {
                if(B[i] == A[j])
                {
                    for(k = 0; k < i; ++k)
                        f[i][j] = (f[i][j] + f[k][j-1]) % 10000;
                    //if(i > 15) printf("%d  %d %d\n", i, j, f[i][j]);
                }
                
            }
            
        }
        int res = 0;
        for(i = 1; B[i]; i++)
            res = (res + f[i][j-1]) % 10000;
        printf("Case #%d: %04d\n", ++cs, res);
    }
    //while(1);
}
