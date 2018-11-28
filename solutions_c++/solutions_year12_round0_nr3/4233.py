#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;



int main()
{
	long long int t,i,ii,j,k,jj,a,b,N,result,m;
	int d [7];
	int pow[7];
	   FILE *f,*f1 ;
    
    f = fopen("C-small-attempt0.in","r");
    f1 = fopen("out.txt","w");
    fscanf(f,"%lld",&t);
//	bool pin[2000001];
	pow[0] = 1;
	pow[1] = 10;
	pow[2] = 100;
	pow[3] = 1000;
	pow[4] = 10000;
	pow[5] = 100000;
	pow[6] = 1000000;

	for ( i = 0 ;i < t;i++)
	{
        	result = 0;
      
		fscanf(f,"%lld",&a);
		fscanf(f,"%lld",&b);
	
		int number =1;
		m = a/10;
		while (m) { number++; m = m/10;}
		for ( jj = a; jj<=b;jj++)
		{
                j = jj;
               // if ( pin[jj] == false )
                {
    			  for ( k = number-1; k>=0;k--)
    			  {
    				  d[k] = j % 10;
    				  j = j/10;
        			}
    			 int m1;

    			 for ( ii = 1;ii<=number-1;ii++)
    			 {
    			     int My,temp1;
                     temp1 = d[number-1];
                     for ( My = number-1 ;My>=1;My--)
    			     {
    					d[My] = d[My-1];
                     }
    			    d[0] = temp1;
                       int m2;N = 0;
    				   for ( m2 = 0 ; m2<number;m2++)
                       {
                         N = N + d[m2]*pow[number-1-m2];
                       }
    				    if ( (N >= a) && (N <= b) && (jj<N) && (d[0]>0))
    				    {
                         //printf("To jj einai  %lld to N einai %lld\n",jj,N);
                        // fprintf(f1,"To jj einai %lld to N einai %lld\n",jj,N);
    					result++;
    				
						}
					
				 }
				 
             }
		}
        printf("Case #%lld: %lld\n",i+1,result);
        fprintf(f1,"Case #%lld: %lld\n",i+1,result);
	}
	system("pause");
return 0;
}
