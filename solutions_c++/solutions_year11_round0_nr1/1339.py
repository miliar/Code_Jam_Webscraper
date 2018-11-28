#include<iostream>
using namespace std;
int N, T;
char A[128];
int B[128];
int pa, pb;
int ta, tb;
int Abs(int a)
{
    return a < 0 ? -a : a;
} 
int main()
{
    int i, res = 0;
    int cs = 0;
    freopen("A_L.in", "r", stdin);
    freopen("A_L.out", "w", stdout);
    scanf("%d", &T);
    while(T--)
    {
       scanf("%d", &N);
       for(i = 0; i < N; ++i)
       {
             scanf("%s %d", &A[i], &B[i]); 
       }
       res = 0;
       int la = 0, lb = 0, tmp, q;
       pa = pb = 1;
       for(i = 0; i < N; ++i)
       {
           if(A[i] == 'O')
           {
               tmp = Abs(B[i] - pa) + 1;
               q = tmp > la ? tmp - la : 1;
               res += q;
               la = 0;
               lb += q;
               pa = B[i];
           }
           else
           {
               tmp = Abs(B[i] - pb) + 1;
                q = tmp > lb ? tmp - lb : 1;
                res += q;
               lb = 0;
               la += q;
               pb = B[i];
           }
       }
       printf("Case #%d: %d\n", ++cs, res);
    }
}
