#include <stdio.h>
#include <string.h>

class c_tree{
public:
    double wei ;
    char str[11] ;
    
    c_tree *left, *right ;
} tree[1048576], *root ;
int n_tree ;

char str[1024], *s ;

void build( c_tree *now ){

    // wei
    if( *s == 0 ){
        scanf("%s", str) ;
        s = str ;
    }
    
    double v = 0 ;
    double base = 1 ;
    while( *s != '.' ){
        v += *s-'0' ;
        s ++ ;
    }
    s ++ ;
    
    while( '0'<=*s && *s<='9' ){
        base /= 10 ;
        v += (*s-'0') * base ;
//        printf("%f\n", v) ;
        s ++ ;
    }
    
    now->wei = v ;
    now->str[0] = 0 ;
    
    // term
    if( *s == 0 ){
        scanf("%s", str) ;
        s = str ;
    }
    if( *s == ')' ){
        s ++ ;
        return ;
    }
    
    // feature
    if( *s == 0 ){
        scanf("%s", str) ;
        s = str ;
    }

    int i ;
    for( i=0 ; s[i] && s[i]!='(' ; i++ )
        now->str[i] = s[i] ;
    now->str[i] = 0 ;
    s += i ;
    
    // left
    now->left = &tree[n_tree++] ;
    if( *s == 0 ){
        scanf("%s", str) ;
        s = str ;
    }
    s ++ ;
    build( now->left ) ;

    // right
    now->right = &tree[n_tree++] ;
    if( *s == 0 ){
        scanf("%s", str) ;
        s = str ;
    }
    s ++ ;
    build( now->right ) ;
    
    // end
    if( *s == 0 ){
        scanf("%s", str) ;
        s = str ;
    }
    s ++ ;
}

void input(){
    root = tree ;
    n_tree = 1 ;

    scanf("%s", str) ;
    s = &str[1] ;

    build( root ) ;
}

void dfs( c_tree*now, int shift ){
    for( int i=0 ; i<shift ; i++ )
        putchar(' ') ;
    printf( "%f:%s\n", now->wei, now->str ) ;
    
    if( now->str[0] ){
        dfs( now->left, shift+1 ) ;
        dfs( now->right, shift+1 ) ;
    }
}

char fea[128][16] ;

double ans(int n){
    c_tree*now = root ;
    double v = 1 ;
    
    while( 1 ){
        v *= now->wei ;
        if( now->str[0] == 0 )
            break ;
            
        int i ;
        for( i=0 ; i<n ; i++ ){
            if( strcmp(fea[i], now->str) == 0 )
                break ;
        }
        
        // match
        if( i<n )
            now = now->left ;
        else
            now = now->right ;
    }
    
    return v ;
}

int main(void){
    int T, L, A ;
    int n ;
    char str[32] ;
    
    scanf("%d", &T) ;
    for( int i_cases=1 ; i_cases<=T ; i_cases++ ){
        scanf("%d", &L) ;
        input() ;
        
//        dfs(root, 0) ;

        printf("Case #%d:\n", i_cases) ;
        
        scanf("%d", &A) ;
        for( int i=0 ; i<A ; i++ ){
            scanf("%s", str) ;
            
            scanf("%d", &n) ;
            for( int j=0 ; j<n ;j++ )
                scanf("%s", fea[j] ) ;

            printf("%.7f\n", ans( n ) ) ;
        }
    }

    return 0 ;
}
