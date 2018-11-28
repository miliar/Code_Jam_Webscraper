#include<iostream>
#include<cstdio>
using namespace std;

void cal (int test)
{
     int N;
     int sum;
     int psum,v;
     int min,i;
     scanf ("%d", &N);
     psum = sum = 0; 
     min = 10000000;
     for (i = 0; i < N; i++ )
     {
         scanf ("%d", &v);
         sum += v;
         psum ^= v;
         if (v < min)
             min = v;
     }
     if (psum)
     {
         printf ("Case #%d: NO\n", test);
     }
     else
     {
         printf ("Case #%d: %d\n", test, sum - min);
     }
     
}



int main()
{
   int T,i;
   //freopen("C-large.in", "r", stdin);
  // freopen("C-large.out", "w", stdout);
    scanf("%d", &T);
    for (i = 1; i<= T; i++)
    {
        cal(i);
    }
  //  system("pause");
    return 0;
}
