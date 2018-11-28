#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
	int t;
	freopen("inp.txt", "r", stdin);
	freopen("k.txt", "w", stdout);
	scanf("%d\n",&t);
//	printf("\n scanning ::  %d",t);
	for(int tc = 1; tc <= t; tc++){
		printf("Case #%d: ", tc);
		//char c;
		int empty=0;
		char mat[4][4];
		int r[4]={0}, c[4]={0} , d[2]={0};
		char winner = 'd';
		for(int i=0; i<4;i++)
        {   for(int j=0; j<4;j++)
            {
                
                scanf("%c", &mat[i][j]);
               // printf("\n scanning %c", mat[i][j]);
                if( mat[i][j] == '.')
                empty = 1;
                if( i==j )
                { 
                  if(mat[i][j] == 'X')
                  d[0]++;
                  else if( mat[i][j] == 'O' )
                  d[0]--;
                  else if( mat[i][j] =='T')
                   {   if( d[0] >0) 
                         d[0]++ ;
                         else if( d[0] < 0)
                         d[0]--;
                   }
                   
                }
                 if( i+j == 3 )
                { if(mat[i][j] == 'X')
                  d[1]++;
                  else if( mat[i][j] == 'O' )
                  d[1]--;
                  else if( mat[i][j] =='T')
                   {   if( d[1] >0) 
                         d[1]++ ;
                         else if( d[1] < 0)
                         d[1]--;
                   }
                }
                              
                              if( mat[i][j] == 'X' )
                              {r[i]++; c[j]++; }
                              else if( mat[i][j] == 'O' )
                              {r[i]--; c[j]--;}
                              else if( mat[i][j] =='T')
                                     {  if( r[i] >0) 
                                        r[i]++ ;
                                        else
                                        r[i]--;
                                        if( c[j] >0) 
                                        c[j]++ ;
                                        else
                                        c[j]--;
                                     }
                    
            }
            scanf("\n");
        }
               if(mat[0][0] == 'T')
                {  if( mat[0][1] == 'X' ) 
                    r[0]++; 
                    else if( mat[0][1] == 'O' )
                    r[0]--; 
                    if( mat[1][0] == 'X' ) 
                    c[0]++;
                    else if( mat[0][1] == 'O' )
                    c[0]--;
                    if( mat[1][1] == 'X' )
                    d[0]++;
                    else if( mat[1][1] =='O' )
                    d[0]--;
                                  
                }
                    
                  if(mat[0][3] == 'T')   
                     {
                               if( mat[1][2] == 'X' )
                               d[0]++;
                                else if( mat[1][2] =='O' )
                                d[0]--;     
                       }  
 
              if( r[0] == 4 || r[1] == 4 || r[2] == 4 || r[3]==4 || c[0]==4 || c[1] == 4 || c[2] ==4 || c[3]==4 || d[1]==4 || d[0] ==4)
              printf("X won\n");
              else if( r[0] == -4 || r[1] == -4 || r[2] == -4 || r[3]==-4 || c[0]== -4 || c[1] == -4 || c[2] == -4 || c[3]== -4 || d[1]== -4 || d[0] == -4)
              printf("O won\n");
              else if (empty==1)
              printf("Game has not completed\n");
              else
              printf("Draw\n");
              scanf("\n");
                }
                     
                                
             
	
	return 0;
}
			
