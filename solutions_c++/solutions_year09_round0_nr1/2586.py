#include<cstdio>
#include<vector>
#define MAXN 6000
#define length 30
using namespace std;

int i , j , k , N , L , D ,  A[MAXN][length] , count , l;
vector <int> String[MAXN];
char c;
bool ok , ok2;

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    
    scanf("%d %d %d\n",&L ,&D ,&N);
    
    for ( i = 1 ; i <= D ; ++i ) {
        for( j = 1 ; j <= L ; ++j ) {
             scanf("%c",&c);
             A[i][j] = int ( c ) - 96;
             }
        scanf("\n");
        }
        
    /*
    for( i = 1 ; i <= D ; ++i){
         for( j = 1 ; j <= L ; ++j)
              printf("%d ",A[i][j]);
         printf("\n");
         }
    */
    for( i = 1 ; i <= N ; ++i )
         {
             j = 0;
             count = 0;
                
             do {
                   scanf("%c",&c);
                   if ( c != '\n') 
                          {
                   ++j;
                    
                   if( c == '(' ) {
                            while ( c != ')')  {
                                  scanf("%c",&c);
                                  if( c != ')') String[j].push_back(int ( c ) - 96);
                                  }
                                  }
                   else String[j].push_back( int ( c) - 96 );
                   }                           
                   
                 }
                   while ( c != '\n' ) ;
                   
             for( j = 1 ; j <= D ; ++j ){
                  ok = true;
                  
                  for( l = 1 ; l <= L ; ++l ) {
                       ok2 = false;
                         for( k = 0 ; k < String[l].size(); ++k)
                              if( String[l][k] == A[j][l] ) ok2 = true;
                              
                         if( ok2 == false) { ok = false ;break; }
                         }
                         
                  if ( ok ) count ++;
                  }
                  
             printf("Case #%d: %d\n",i , count);
             
             for( j = 1; j <= L ; ++j)
                  for( k = 0 ; k < String[j].size(); ++k)
                       String[j][k] = -1;
         }

return 0;
}
