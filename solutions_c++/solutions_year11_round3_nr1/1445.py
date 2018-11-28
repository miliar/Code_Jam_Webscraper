#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <bitset>
#include <string.h>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<string> vs;
typedef long long int64;

#define forit(a,b) for(typeof((b).end()) a=(b).begin();a!=(b).end();a++)
#define clr(a,b) memset(a,b,sizeof a)
#define all(a) a.begin(),a.end()
#define sorta(a) sort(all(a))
#define scan(a) scanf("%d",&a)


int N,K;





int main(){
	
   int tes,m,R,C,impossible;
   //char *ans;
   char  square[50][50];
   //char  tempteams[100][100];
   //float WP[100]; 

 
    scan( tes );
    
	for( int ttes = 1 ; ttes <= tes ; ttes++ )
    {      
  
        scan(R);
        scan (C);
        impossible = 0;
             
        for (int i = 0 ; i < R ; i++)
          {           
                 scanf("%s",square[i]);                       
          }        
                    
        for (int i = 0; i < R - 1; i++)
          {
             for (int j = 0 ; j < C -1; j++)
               {
                   if (square[i][j] == '#' && square[i][j+1] == '#' && square[i+1][j]=='#' && square[i+1][j+1] == '#')
                     {
                        square[i][j] = '/';
                        square[i][j + 1] = '\\'; 
                        square[i + 1][j] = '\\'; 
                        square[i + 1][j + 1] = '/';
                        i = 0;
                        j = 0;            
                     }                     
               }      
          }
        for (int i = 0 ;i < R ; i++)
          {
              for (int j =0 ; j < C ; j++)
                 {
                       if (square[i][j] == '#')
                         {
                            impossible = 1;
                            break;
                         }
                 }
                 
          }   
        
        
          printf("Case #%d:\n",ttes); 
          if (impossible == 1)
            {
               printf ("Impossible\n");
            }       
          else
           {           
              for(int i = 0 ; i < R ; i++)
                { 
                   for ( int j = 0 ;  j< C ; j++)
                       {
                            printf("%c",square[i][j]);
                       }
                       printf("\n");
                }
            }
	}
//	scan(m);
	return 0;
}
