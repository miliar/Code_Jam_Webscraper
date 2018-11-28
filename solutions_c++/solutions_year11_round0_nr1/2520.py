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
	
   int tes,k;
   char  robots[100][1];
   int   buttons[100];
   int   distance[100];
 
    scan( tes );
	for( int ttes = 1 ; ttes <= tes ; ttes++ )
    {
         int total = 0,distCnt = 0,j=0;
         
        for (int i = 0 ; i < 100 ; i++) 
           {
                 buttons[i]= 0;
                 distance[i]= 0;
                 robots[i][0]= '\0';
           }
         
        scan( N);
        
        for (int i = 0 ; i < N ; i++)
            {
                 scanf("%s",robots[i]);
                 scanf("%d",&buttons[i]); 
            } 
        
        distance[0] = buttons[distCnt];
        for(int i = 0 ; i < N ; i++)
           {
                if (robots[0][0] != robots[i][0])
                  {
                        distance[i] = buttons[i];
                        break;
                  }
           }
            distCnt++;
        for (int i = 0 ; i < N ; i++)
            {
                 for( j = i + 1 ; j < N ; j++)
                     {
                          if (robots[i][0] == robots[j][0])
                             {
                                   distance[j] = abs(buttons[i] - buttons[j]) + 1;       
                                   break;     
                             }
                     }
            }    
            
        for (int i = 0; i < N ; i++)
            {
                 for ( j = i + 1 ; j < N ; j++)     
                     {
                          if (robots[i][0] != robots[j][0])
                             {
                                  
                                  if (distance[i] > distance[j])
                                     {
                                         distance[j] = 0;
                                         
                                            
                                         total += distance[i];
                                         distance[i] = 0;
                                     }
                                  else if (distance[i] != 0)
                                      {
                                         distance[j] -= distance[i];
                                         total += distance[i];
                                         
                                      }
                                  else
                                      {
                                          distance[j] -= 1;
                                          total += 1;
                                      }
                                      break;
                             }
                     }                    
                 
                 
                     if (j == N)
                      {
                           if (distance[i] == 0)
                               total += 1;
                           else
                               total += distance[i];
                                    
                      }
            }


          printf("Case #%d: %d\n",ttes,total);
		
	}
	scan(k);
	return 0;
}
