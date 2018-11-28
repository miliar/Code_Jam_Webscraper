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


//FILE *in = fopen( "f.in" , "r" );
//FILE *out = fopen( "output.txt" , "w" );
//
//int N , M , dp[ 111 ][ 111 ];
//char g[ 111 ][ 111 ];

//bool bad( char x ){
//	if( x == 'W' || x == 'R' || x == 'T' ) return 1;
//	return 0;
//}
//inline int sum( int x1 , int y1 , int x2 , int y2 ){
//	return dp[ x1 ][ y1 ] - dp[ x1 ][ y2 + 1 ] - dp[ x2 + 1 ][ y1 ] + dp[ x2 + 1 ][ y2 + 1 ];
//}

int C, D, N;
char  combine[50][3], oppose[30][2], list[100], temp[100];

int main(){
	
	int tes, start= 0, tempstart = 0,tempend = 0, tempflag=0, tempcnt = 1; 
 
    scan( tes );
	for( int ttes = 1 ; ttes <= tes ; ttes++ )
    {
         tempend = 0;
         tempcnt = 1;
		scan( C ); 
		
		//memset(temp,"\0",sizeof temp);
//		memset(combine,"\0",sizeof combine);
//		memset(oppose,"\0",oppose temp);
//		memset(list,"\0",sizeof list);
       
       for (int x = 0 ; x < 50 ; x++)
         {
           for  (int y = 0; y < 3 ; y++)
               combine[x][y] = '\0' ;                     
         }
         
         
       for (int x = 0 ; x < 30 ; x++)
         {
           for  (int y = 0; y < 2 ; y++)
               oppose[x][y] = '\0' ;                     
         }
       for (int x = 0 ; x  < 100 ; x++)
       {
           list[x] = '\0' ;      
           temp[x] = '\0' ;          
       }
       
		for( int q = 0 ; q < C ; q++ )
        {
	             scanf( "%s" ,combine[ q ] );
		}
        scan( D ); 
       
		for( int q = 0 ; q < D ; q++ )
        {
	             scanf( "%s" ,oppose[ q ] );
		}
		
		scan (N);
		scanf("%s",list);
	
		temp[tempstart] = list[0];
		for(int i = 1 ;  i < N ; i++)
		{
             int j = 0,k = 0,l =0;
              for (j = 0 ; j < C ; j++)
                  {
                       if (( temp[tempend] == combine[j][0] && list[i] == combine[j][1]) || ( temp[tempend] == combine[j][1] && list[i] == combine[j][0] ) )      
                        {
                             temp[tempend] = combine[j][2]; 
                              
                             break;                             
                        }
                        
                  } 
                  
              if( j == C)
              {               
                  for (k = 0 ; k < D ; k++)
                  {
                      for  ( l = 0 ; l <= tempend ; l++)
                           {                                
                                if((temp[l] == oppose[k][0] && list[i] == oppose[k][1]) || (temp[l] == oppose[k][1] && list[i] == oppose[k][0]))
                                    {
                                            //memset(temp,"\0",sizeof(temp));
                                            tempstart = 0;
                                            tempend = 0;
                                            tempflag = 1;
                                            ++i;
                                            if  (i < N)
                                             {
                                                   temp[tempstart] = list[i];
                                                   tempcnt = 1;
                                             }
                                             else
                                             {
                                                 tempcnt = 0;    
                                             }
                                            
                                            break;
                                    }                                
                           }
                           if (tempflag == 1)
                           {
                              tempflag = 0;             
                              break;
                           }
                   }
              } 
              else
                 continue;       
                 
              if (k == D)
                  {
                       temp[++tempend] = list[i];
                       tempcnt++;
                  }        
        }
        
        printf("Case #%d: [",ttes);
        
        for (int p = 0 ; p < tempcnt ; p++)
           {
                  
                   if ( p == tempcnt - 1 )
                      {
                         printf ("%c",temp[p]);
                      }
                      else 
                     {
                           printf("%c, ",temp[p]);                                                    
                     }
                 
           }
        printf ("]\n");




		
	}
	scanf("%d",D);
	return 0;
}
