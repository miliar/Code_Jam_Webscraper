#include<iostream>
#include<algorithm>
#include<ctime>
#include<stdio.h>
#include<string.h>
#include<map>
#include<vector>
#include<cmath>
#include<string>
#include<queue>
#include<sstream>
using namespace std;

const int maxn = 105;
char mat[ maxn ][ maxn ];

int n;

typedef double db;

void get(){
     cin >> n;
     int i;
     for(i = 0; i < n; ++ i) scanf("%s", mat[i]);     
}

int cas = 0;

db WP[ maxn ], OWP[ maxn ], OOWP[ maxn ];
int cnt[ maxn ], win[ maxn ];

void get_wp(){
     int i, j, k, tot;
     for(i = 0; i < n; ++ i){
           tot = k = 0;
           for(j = 0; j < n; ++ j) if(mat[i][j] != '.') {
                 ++ tot;
                 if(mat[i][j] == '1') ++ k;      
           }      
           WP[ i ] = (db) k / tot;
           cnt[ i ] = tot;
           win[ i ] = k;
     }  
    // for(i = 0; i < n; ++ i) printf("WP[ %d] = %.3f\n", i, WP [ i ]);   
}

void get_owp(){
     int i, j;
     for(i = 0; i < n; ++ i){
           OWP[ i ] = 0.0;
           for(j = 0; j < n; ++ j){
                 if( mat[i][j] == '.') continue;
                 // j
                 OWP[ i ] += (db)( win[ j ] - (mat[j][i] == '1') ) / (cnt[ j ] - 1.0);      
           }
           OWP[ i ] /= cnt[ i ];
     }  
     //for(i = 0; i < n; ++ i) printf("OWP[ %d] = %.3f\n", i, OWP [ i ]);   
}

void get_oowp(){
     int i, j;
     for(i = 0; i < n; ++ i){
           OOWP[ i ] = 0.0;
           for(j = 0; j < n; ++ j){
                 if( mat[i][j] == '.') continue;
                 // j
                 OOWP[ i ] += OWP[ j ];      
           }
           OOWP[ i ] /= cnt[ i ];
     }  
     //for(i = 0; i < n; ++ i) printf("OWP[ %d] = %.3f\n", i, OOWP [ i ]);   
}

void work(){
     ++ cas;
     printf("Case #%d:\n", cas); 
     get_wp();  
     get_owp();  
     get_oowp();  
     int i;
     for(i = 0; i < n; ++ i)
           printf("%.10f\n", 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[ i ]);
}

int main(){
    freopen("D:\\ain.txt","r",stdin);
    freopen("D:\\aout.txt","w",stdout);
    int T;
    cin >> T;
    while(T --){
         get();
         work();           
    }
    //while( 1 ) ;
	return 0;
}
