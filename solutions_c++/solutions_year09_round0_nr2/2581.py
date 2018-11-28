#include<cstdio>
#include<vector>
#include<algorithm>
#define MAXN 110


using namespace std;

int vert[5] = { -1 , 0 , 0 , 1 };
int oriz[5] = { 0 , -1 , 1 , 0 };

int i , j , k , T , N , M , A[MAXN][MAXN] , B[MAXN][MAXN] , C[MAXN][MAXN] , current , coresp[30];


/*
void fill (int X , int Y) {
          
          int mins = A[X][Y] , pozmin , j;
          
          if ( X < 1 || X > N || Y < 1 || Y > N ) return ;
          
          B[X][Y] = current;
          
          for( j = 0 ; j <= 3 ; ++j)
           if ( X + vert[j] >= 1 && X + vert[j] <= N && Y + oriz[j] >= 1 && Y + oriz[j] <= N )  {
               if ( A[ X + vert[j] ][ Y + oriz[j]] <  mins) {
                       mins = A[X + vert[j]][Y + oriz[j]];
                       pozmin = j;
                       }
               }
          fill ( X + vert[pozmin] , Y + oriz[pozmin] );


}
 */
 
int find ( int X , int Y ) {
    
    int j , minn = A[X][Y], pozmin = 4 , Result;
    
    for( j = 0 ; j <= 3;  ++j)
          if ( X + vert[j] >= 1 && X + vert[j] <= N && Y + oriz[j] >= 1 && Y + oriz[j] <= M )  {
               if ( A[ X + vert[j] ][ Y + oriz[j]] <  minn) {
                       minn = A[X + vert[j]][Y + oriz[j]];
                       pozmin = j;
                       }
               }
    
    Result = ( X + vert[pozmin] ) * 1000 + ( Y + oriz[pozmin] );
    
return Result;
}

inline int code ( int i , int j )  {
       return i * 1000 + j;
}

void fill ( int X , int Y ) {
     
          int j;
          
          if ( X < 1 || X > N || Y < 1 || Y > M ) return;
     
          C[X][Y] = current;
          
          for( j = 0 ; j <= 3; ++j)
               if ( X + vert[j] >= 1 && X + vert[j] <= N && Y + oriz[j] >= 1 && Y + oriz[j] <= M )  {
                    if ( B[X + vert[j]][Y + oriz[j]] == code ( X , Y )) fill ( X + vert[j] , Y + oriz[j] );
                    }

}

int main () {
    
         freopen("B.in","r",stdin);
         freopen("B.out","w",stdout);
         
         scanf("%d",&T);
         
         for( k = 1 ; k <= T ; ++k ) {
              
              current = 0;
              scanf("%d %d",&N,&M);
              
              for( i = 1 ; i <= N ; ++i)
                   for( j = 1 ; j <= M ; ++j)
                        scanf("%d",&A[i][j]);
              
              for( i = 1 ; i <= N ; ++i)
                   for( j = 1 ; j <= M ; ++j)
                        B[i][j] = find ( i , j );
              
              for( i = 1 ; i <= N ; ++i)
                   for( j = 1; j <= M ; ++j)
                        if ( B[i][j] == code ( i , j ) ) {
                             C[i][j] = ++current;
                             fill ( i , j );
                             }
                             
              
              /*
              for( i = 1 ; i <= N ; ++i ){
                   for( j = 1; j <= M ; ++j)
                        printf("%d ",C[i][j]);
                   printf("\n");
                   }
                   
                           */
                           
              printf("Case #%d: \n",k);
              
              current = 97;
              
              for( i = 1 ; i <= 30 ; ++i )
                   coresp[i] = 0;
                            
              for( i = 1 ; i <= N ; ++i){
                   for( j = 1 ; j <= M ; ++j){
                        if ( coresp[C[i][j]] == 0 ) coresp[C[i][j]] = current ++;
                        printf("%c ", char ( coresp[C[i][j]])) ;
                        }
                   printf("\n");
                   }
                   
              }
                   
                   
return 0;
}
