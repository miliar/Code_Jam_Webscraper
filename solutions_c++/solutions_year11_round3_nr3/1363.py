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
	
   int tes,m,N,L,H,impossible;
   long long i,j,k;
   long long ans = 0;
   long long int  players[10000];
   //char  tempteams[100][100];
   //float WP[100]; 

 
    scan( tes );
    
	for( int ttes = 1 ; ttes <= tes ; ttes++ )
    {      
  
        scan(N);
        scan(L);
        scan(H);
        impossible = 0;
             
        for ( i = 0 ; i < N ; i++)
          {           
                 scanf("%Ld",&players[i]);                       
          }        
                    
        
        for ( k = L; k <= H ; k++)
         {
            for ( i = 0 ; i < N ; i++)
              {
                  if(players[i]%k == 0 or k%players[i] == 0)
                    {
                       continue;
                    }    
                  else
                    {
                         break;
                    }
              }
              
             if (i == N)
              {
                    ans = k;
                    break;
              }
         }
                
        if (k == H + 1)
         {
            impossible =  1; 
         }
        
          printf("Case #%d: ",ttes); 
          if (impossible == 1)
            {
               printf ("NO\n");
            }       
          else
           {           
              printf("%Ld\n",ans);
            }
	}
//	scan(m);
	return 0;
}
