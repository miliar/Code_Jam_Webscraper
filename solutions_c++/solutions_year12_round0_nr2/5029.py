# include <math.h>
# include <stdlib.h>
# include <stdio.h>
long long int max ( long long int a ,long long int b)
{
     if ( a>=b) return a;
     return b;
 }

int main()
{
    long long int T,i,j,k,S,N,p,result,n1,n2,n3;
    float m;
    FILE *f,*f1 ;
    
    f = fopen("B-large.in","r");
    f1 = fopen("out.txt","w");
    fscanf(f,"%lld",&T);
    for ( i = 0; i < T;i++)
    {
       // printf("douleuw\n");
        fscanf(f,"%lld",&N);
        
        fscanf(f,"%lld",&S);
        
        fscanf (f,"%lld",&p);
        result = 0 ;
        for ( j = 0 ; j<N;j++)
        {
            fscanf(f,"%lld",&k);
            if ( k > 0 )
            {
                 if ( k % 3 == 0 )
                 {
                      m = k/3.0;
                      n1 = n2 = n3 = (long long int) m;
                 }
                 else
                 {
                     m = ceil(k/3.0);
                     n1 = (long long int)m;
                     n2 = n1-1;
                     n3 = k - n2 - n1;
                 }
                 
                 if ( n1 >= p ) { result++;}
                 long long int fotis = max(n2,n3);
                 if (   (S>0 ) && ( n1 < p) && ( n1 + 1 >= p ) && (n1 + 2 - fotis <= 2)  ) 
                 {
                      result++;
                      S--;
                 }
                 
            }
            else
            {
                if ( k >= p ) { result ++;}
            }
            
        }
        printf("Case #%lld: %lld\n",i+1,result);
        fprintf(f1,"Case #%lld: %lld\n",i+1,result);
        
        
    }
    fclose(f);
    fclose(f1);
    system("pause");
    return 0;
}
