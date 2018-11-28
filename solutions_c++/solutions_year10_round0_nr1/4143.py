#include<stdio.h>
#include<math.h>
#include<memory.h>
#include<string.h>
#include<stdlib.h>
long long int n,k;
main()
{       
        int t;
        
       // long long int n;
        //long long int j;
        
        int i;
        //char *str;
        FILE *fs, *ft,*ft3,*fs2;
        char ch ;
        fs = fopen( "a.in", "r" ) ;
       
        ft = fopen ( "asgaurav.out", "w" ) ;
        
        fscanf(fs,"%d",&t);
        for(i=1;i<=t;i++)
        {
             //  ch = fgetc( fs ) ;
               fs2=fs;
                fscanf(fs2,"%Ld%Ld",&n,&k); 
               ft3=ft;
            //fprintf(ft3, " Case #%Lu %Lu:", n,k );
            //  if ( ch == EOF )
              //     break ;
               
               
                 
                {
                 //ft2=ft;
                 //fprintf(ft, "Case #%d:", i );
                 //i++;
                 
                long long int p=(long long int)pow(2,n);
                 
                // fprintf(ft, " %Ld%Ld:", p,n );
                 //while(k > p)
                 //k=(k-p)+1);
                long long int j=(k+1)%p;
                if(j==0) 
                 fprintf(ft,"Case #%d: %s\n", i, "ON");
                else
                 fprintf(ft,"Case #%d: %s\n", i, "OFF");
                
                }//t--;
                
       }
}
      

                    
