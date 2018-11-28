#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    int t, n, i, j;
    scanf("%d", &t);
    for(int k = 0; k < t; k++)
    {
            scanf("%d", &n);
            int exor1, exor2;
            int found = 0;
            int sum = 0;
            int *a = (int *)calloc(sizeof(int), n);
            for(i =0 ; i < n; i++)
                    scanf("%d", &a[i]);
            sort(a, a + n);
            exor1 = 0;     
            exor2 = 0;       
            for(i = 0;i < n-1; i++)
            {
                  exor1 ^= a[i];
                  for(j = n-1; j > i; j--)
                          exor2 ^= a[j];
                  if(exor1 == exor2)
                  {
                           found = 1;
                           break;    
                  }
            }
            if(found == 1)
            {
                     for(j = n-1; j >i; j--)
                           sum += a[j];
                     printf("Case #%d: %d%s", k+1, sum, k == t? "" : "\n");
            }
            else
                     printf("Case #%d: NO%s", k+1, k == t? "" : "\n");
    }    
    //system("pause");
}
