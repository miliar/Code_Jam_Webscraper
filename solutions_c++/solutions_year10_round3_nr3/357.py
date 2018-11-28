/*
TASK: third
LANG: C++
*/
#include <iostream>
#include <vector>
#include <cstdio>
#include <cmath>
#include <iomanip>
#include <set>
#include <queue>
#include <cstring>
#include <algorithm>
#define foreach(_v,_c) for( typeof((_c).begin()) _v = (_c).begin() ; _v != (_c).end() ; ++_v )

using namespace std;

unsigned long long int map[32][32];
unsigned long long int size[534];

void fromInt( int row, unsigned long long k , int M ){
    for( int i = M-1 ; i >= 0 ; i-- ){
        map[row][i] = k % 2;
        k/=2;
    }
}

bool has( int N , int M , int lx , int ly , int w ){
    int expected = map[lx][ly];
    for( int i = 0 ; i < w ; i++ ){
        for( int j = 0 ; j < w ; j++ ){
            if( expected != map[lx+i][ly+j] )
                return false;
            expected = !expected;
        }
        expected = (i%2)==0 ? !map[lx][ly] : map[lx][ly];
    }
    return true;
}

int biggest( int N , int M , int lx , int ly ){
    int big = 1;
    for( ; big+lx <= N and  big+ly <= M and has(N,M,lx,ly,big) ; big++ );
    --big;
    return big;
}

int solve( int N , int M ){
    int maxsz = 0;
    int maxx = 0;
    int maxy = 0;
    
    for( int i = 0 ; i < N ; i++ ){
        for( int j = 0 ; j < M ; j++ ){
            if( map[i][j] == 2 )
                continue;
            int b = biggest(N,M,i,j);
            
            if( b > maxsz ){
                maxsz = b;
                maxx = i;
                maxy = j;
            }
            
        }
    }
    
    if( maxsz == 0 ){
        return 0;
    }
    
    size[maxsz]++;
    
    for( int i = 0 ; i < maxsz ; i++ ){
        for( int j = 0 ; j < maxsz ; j++ ){
            map[maxx+i][maxy+j] = 2;
        }
    }
    //printf("MAXSIZE is %d\n", maxsz );
    return 1;
}

int main(){
	freopen("third.in","r",stdin);
	freopen("third.out","w",stdout);
	
	int T,N,M;
	
	cin >> T;
	
	for( int i = 0 ; i < T ; i++ ){
	    cin >> dec >> N >> M;
	    memset( map , 0 , sizeof(map) );
	    memset( size , 0 , sizeof(size) );
	    
	    for( int j = 0 ; j < N ; j++ ){
	        unsigned long long k;
	        cin >> hex >> k;
	        fromInt( j , k , M );
	    }
	    /*
	    for( int j = 0 ; j < N ; j++ ){
	        for( int k = 0 ; k < M ; k++ ){
                printf("%2d", map[j][k]);
	        }
	        printf("\n");
	    }
	    */
	   /* 
	    for( int i = 0 ; i < N ; i++ ){
	        for( int j = 0 ; j < M ; j++ ){
	            printf("%2d", biggest(N,M,i,j));
	        }
	        printf("\n");
	    }
	    */
	    while( solve(N,M) );
	    /*
	    for( int i = 0 ; i < N ; i++ ){
	        for( int j = 0 ; j < M ; j++ ){
	            printf("%2d", biggest(N,M,i,j));
	        }
	        printf("\n");
	    }*/
	   /* 
	    for( int i = 1 ; i < 10 ; i++ ){
	        printf("%d %d\n", i,size[i]);
	    }
	    */
	    int count = 0;
	    for( int k = 1 ; k <= 300 ; k++ ){
	        if( size[k] ) 
                count++;
	    }
	    
        printf("Case #%d: %d\n", i+1, count);
        
        for( int k = 300 ; k >= 1 ; k-- ){
            if( size[k] )
                printf("%d %d\n", k , size[k]);
                
        }
	    
	}
	
	return 0;
}
