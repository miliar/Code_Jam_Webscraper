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


int N;




int main(){
	
   int tes;
   long int   piles[1000];
   
 
    scan( tes );
	for( int ttes = 1 ; ttes <= tes ; ttes++ )
    {
         long int total = 0,temp = 0,j=0,sum =0;
         
        for (int i = 0 ; i < 1000 ; i++) 
           {
                piles[i]= 0;
           }
         
        scan( N);
        
        for (int i = 0 ; i < N ; i++)
            {
                
                 scanf("%ld",&piles[i]); 
            } 
        
        
        for(int i = 0 ; i < N ; i++)
           {
                for (j = i + 1 ; j < N ; j++)
                    {
                         if (piles[i] < piles[j])
                            { 
                              temp = piles[j];
                              piles[j] = piles[i];
                              piles[i] = temp;                                     
                            }
                    }    
           }
           
        for(int i = 0 ; i < N - 1 ; i++)
            {
                total = total ^ piles[i];
                sum = sum + piles[i];
            }
            
        if (total == piles[N-1])
           {
                  printf("Case #%d: %ld\n",ttes,sum);                  
           }
        else
           {
                  printf("Case #%d: NO\n",ttes);                  
           }
        

          
		
	}
	scan(tes);
	return 0;
}
