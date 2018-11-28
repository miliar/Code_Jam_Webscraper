#include<iostream>
using namespace std;
int L, D, N;
char s[5010][20];
char A[2048];
int main()
{
    int cs = 0;
    int r;
    int i, j, k;
    int p;
    bool flag;
    freopen("A_L.in", "r", stdin);
    freopen("A_L.out", "w", stdout);
    while(scanf("%d%d%d", &L, &D, &N) != EOF)
    {
        for(i = 0; i < D; ++i)
        {
            scanf("%s", s[i]);
        }
        for(i = 0; i < N; ++i)
        {
            scanf("%s", A);
            r = 0;
            for(p =0; p < D; ++p)
            {
                j = 0;
                flag = 0;
                for(k = 0; A[k]; k++)
                {
                    if(A[k] == '(')
                    {
                        flag = 1;
                         continue;
                    }
                    if(A[k] == ')')
                    {
                        break;
                    }
                    if(A[k] == s[p][j])
                    {
                        j++;
                        if(flag)
                        {
                            for(; A[k] != ')'; k++);
                            flag = 0;
                        }
                    }
                    
                }
                /*if(p == 16)
                {
                    printf("%s\n", s[p]);
                    printf("%d\n", j);
                }*/
                if(j == L) ++r;
            }
            printf("Case #%d: %d\n", i + 1, r);
        }
    }
   // while(1);
}
