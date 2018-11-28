#include <iostream>
#include <vector>
using namespace std ;

struct tree
{
       tree *next[26] ;
       int p ;
       tree(){
              int i ;
              p = -1 ;
              for( i = 0 ; i < 26 ; i ++ )
                   next[i] = NULL ;
       }       
};
int l , n , m ;
void Insert( char str[] , tree *root )
{
     int i ;
     for( i = 0 ; i < l ; i ++ )
     {
          if( root->next[str[i]-'a'] == NULL )
              root->next[str[i]-'a'] = new tree() ;
          root = root->next[str[i]-'a'] ;     
     }     
     root->p = 1 ;
}
int ans ;
vector<int>a[16] ;
void Dfs( tree *root , int p )
{
     if( p == l )
     {
         ans ++ ;
         return ;
     }
     int i , t ;
     for( i = 0  ; i < a[p].size() ; i ++ )
     {
          t = a[p][i] ;
          if( root->next[t] == NULL )
              continue ;
          else
              Dfs( root->next[t] , p + 1 ) ;
     }
}
int main(){
    freopen("A-large.in" , "r" , stdin);
    freopen("A-large.out" , "w" , stdout);
    while( scanf("%d%d%d" , &l , &n , &m ) == 3 )
    {
           int i , j , t , k , p ;
           char str[16] ;     
           tree *root = new tree() ;
           for( i = 0 ; i < n ; i ++ )
           {
                scanf("%s" , str ) ;
                Insert( str , root ) ;   
           }
           char s[450] ;
           for( i = 0 ; i < m ; i ++ )
           {
                scanf("%s" , s);
                for( j = 0 ; j < l ; j ++ )
                     a[j].clear();
                t = 0 , p = 0 ;
                k = strlen(s) ;
                for( j = 0 ; j < k ; j ++ )
                {
                     if( s[j] == '(' )
                         t = 1 ;
                     else if( s[j] == ')' )
                     {
                          t = 0 ;
                          p ++ ;
                     }
                     else
                     {
                         if( t == 0 )
                         {
                             a[p].push_back( s[j] - 'a') ;
                             p ++ ;
                         }
                         else
                             a[p].push_back( s[j] - 'a') ;
                     }
                }
                ans = 0 ;
                Dfs( root , 0 ) ;
                printf("Case #%d: %d\n" , i + 1 , ans ) ;
           }                  
    }
    return 0 ;    
}
