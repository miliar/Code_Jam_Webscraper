#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char searchEngines[101][101];
char Queries[1001][101];
int N=0,TC[21];
int Query;

int Calculate(int i);

int main()
{
   
    
    int Result[21]={0,0,0};
    int i,j=0,k=0,l=0;

    scanf("%d",&N);
    i=1;

    //read the inputs i.e Test Cases
    while( i <= N)
    {
       // read no.of search engines and their names
       scanf("%d",&TC[i]);
       fflush(stdin);
       for( j=1; j<=TC[i]; j++)
       {
	        gets(searchEngines[j]);	        
       }
       fflush(stdin);
        
       // read no.of queries and their inputs
       
       scanf("%d",&Query);
       fflush(stdin);
       for( k=1; k<=Query; k++)
       {
	        gets(Queries[k]);	        
       }
       
       // call calculate to find the numbers
       Result[i]=Calculate(i);       
       
       i++;
    }
    for (i=1;i<=N;i++)
    {
        printf("Case #%d: %d\n",i,Result[i]);
    }

  system("pause");
  return 0;
}

int Calculate( int  i )
{
   int count=0,j=0,k=0,l=0;
   int num[TC[i]+1];
   int dummy=0;
          
          for(l=1;l<=TC[i];l++)
               num[l]=0;
               
   for( k=1; k<=Query; k++)
         {
                  for( j=1;j<=(TC[i]);j++)
                    {
                      if((num[j]==0) && (!(strcmp(searchEngines[j],Queries[k]))))
                      {
                        num[j]=1;
                        dummy++;                                                             
                      
                        if( dummy == (TC[i]) )
                         {
                              count++;
                              dummy=1;
                               for(l=1;l<=TC[i];l++)
                                  num[l]=0;
                               num[j]=1;
                               
                         }  
                        break;  
                      }
                    }
                    
                       
           }
    
   return count;   
}
