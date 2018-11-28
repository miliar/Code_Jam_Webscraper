#include <stdio.h>
#include <iostream>
using namespace std;


char text[]="welcome to code jam";

int result[100];



int w(char *t,int s, int c, int next)
{
    //printf("%s\n", t);
    if( next==19 )
    {
        result[c]=(result[c]+1)%10000;
        return 0;
    }
    while( t[s]!=0 )
    {
           
           if( t[s]==text[next] )
           {
               //printf("%c %c", t[s],text[next]  );
               w( t, s, c,  next+1 );
               //printf("found");
               
           }
           s++;
    }    
}

int main()
{
    char input[500][500];
    
    result[0]=0;
    int n, i, j;
    
    for(i=0; i<100; i++ )
    {
             result[i]=0;         
    }
    
    scanf("%d", &n);
    cin.getline (input[0],500);
    for(i=0; i<n; i++ )
    {
             //printf("in %d:", i+1);
             cin.getline (input[i],500);
    }
    for(i=0; i<n; i++ )
    {
             w( input[i], 0, i, 0 );
    } 
    for(i=0; i<n; i++ )
    {
             printf("Case #%d: %04d", i+1, result[i]);
             if( n-i>1 )
             {
                 printf("\n");
             }
    }  
     
    
    //w("wweellccoommee to code qps jam", 0, 0, 0);
    
    //printf("%d", result[0]);
    return 0;
}
