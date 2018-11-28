#include<iostream>
#include<vector>
using namespace std;


char name[20];
char test[1000000];
bool hash[20][30];

vector < string > V;


int main(){
    
    freopen( "ulaz.txt", "r", stdin );
    freopen( "izlaz.txt", "w", stdout);
    
    int L, D, N;
    scanf("%d %d %d", &L, &D, &N );
    
    for(int i=0; i < D; i++ ) {
        scanf("%s", name );
        V.push_back ( (string)name );
    }    
    
    for(int t=1; t <= N; t++ ){
       
       int sol(0), group(-1); bool ok, open(0);
       
       for( int i=0; i < L; i++ )
         for(int j=0; j < 27; j++ )hash[i][j] = false;
       
       scanf( "%s", test );

       for( int i = 0; i < strlen( test ); i++ ){
           if(  test[i] == '(' ){ open = 1; group ++; }
           if(  test[i] == ')' )  open = 0;
           
           if( isalpha( test[i] ) ){
               if( open )hash[group][test[i]-'a'] = true;
               else hash[++group][test[i]-'a'] = true; 
           }  
       }
       
       for( int i = 0; i < D; i++ ){
          ok = false;
          for( int j = 0; j < L; j++ )
          { 
              ok = hash[j][V[i][j]-'a'];
              if( !ok )break;
          }
         if( ok ) sol ++;
       }
       
       printf("Case #%d: %d\n", t, sol );
    }  
    
    return 0;
}
            
                 
            
