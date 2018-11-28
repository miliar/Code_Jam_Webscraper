#include <stdio.h>
#include <bitset>

using namespace std;

int g[1001];
long long sum[1001];
int next[1001];

void debugAr( int ar[], int n)
{
    for(int i = 0; i < n; i++)
            printf("%d ", ar[i]);
            
    printf("\n");
     
}

int main()
{
    int z,zz;
    int r, k, n, i;
    
    scanf("%d", &zz);
    
    for(z = 0; z < zz; z++)
    {
       
       scanf("%d%d%d", &r, &k, &n);
       for(i=0;i<n;i++)
       {
            scanf("%d", &g[i]);                            
            sum[i]=0;
            next[i]=0;                       
       }       
       
       for(i = 0; i<n; i++)
       {
           long long tmpsum = g[i];
           int count = 0;      
           int j = (i+1)%n;  
           while( tmpsum <= k  && count < n)
           {
                count++;  
                tmpsum += g[j];  
                j = (j+1) % n;       
           }
           
           j = (j + n - 1) % n;
           tmpsum -= g[j];
           
           sum[i] = tmpsum;
           next[i] = count - 1;
             
       }
       
      // debugAr(sum, n);
      // debugAr(next, n);
       
       long long sumtot = 0;
       int indx = 0;
       for(i = 0; i < r; i++)
       {
          sumtot += sum[indx];
          indx = (indx + 1 + next[indx]) % n;  
                    
             
             
       }
       
       printf("Case #%d: %I64d\n", z+1, sumtot);
          
    }  
    
    
    
    
}
