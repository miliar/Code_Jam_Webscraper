#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;

struct train{
    int trains [2000];
    int departure [2000];        
    vector <int> arrival [2000];
} A, B;

int init(){
    memset( A.departure, 0, sizeof( A.departure ) );
    memset( B.departure, 0, sizeof( B.departure ) );   
    
    for ( int i = 0; i < 2000; ++i ) {
        A.arrival[i].clear();
        B.arrival[i].clear();    
    }
}

int main(){
    int tc, tcase = 0;
    char ta[6], td[6];
    int h, m;
    int T, NA, NB, Arr, Dep;
    
    freopen("f:/gcjb.txt", "w", stdout);
    
    scanf("%d", &tc);
    
    while ( tc-- ){
        scanf("%d", &T);
        scanf("%d %d", &NA, &NB);
        init();
        
        for ( int i = 0; i < NA; ++i ){
            scanf("%d:%d", &h, &m );
            Dep = h * 60 + m;
//            cout << Dep << endl;
            scanf("%d:%d", &h, &m );
            Arr = h * 60 + m;
//            cout << Arr << endl;
            A.departure [ Dep ]++;  A.arrival [ Dep ].push_back ( Arr );
        }
        
        for ( int i = 0; i < NB; ++i ){
            scanf("%d:%d", &h, &m );
            Dep = h * 60 + m;
//            cout << Dep << endl;
            scanf("%d:%d", &h, &m );
            Arr = h * 60 + m;
//            cout << Arr << endl;
            B.departure [ Dep ]++; B.arrival [ Dep ].push_back ( Arr );
        }
        
        
        int flag;
        
        for ( int tot = 0; tot <= 500; ++tot ){
            flag = false;

            for ( int na = 0; na <= tot; ++na ){
                int nb = tot - na;

                memset( A.trains, 0, sizeof( A.trains ) );
                memset( B.trains, 0, sizeof( B.trains ) );
                                
                flag = true;
                A.trains[0] = na;
                B.trains[0] = nb;                
                
                for ( int tm = 0; tm < 2000; ++tm ){
                    if ( tm ){
                        A.trains[ tm ] += A.trains[ tm - 1 ];                        
                        B.trains[ tm ] += B.trains[ tm - 1 ];
                    }

                    if( A.departure[ tm ] ) {
                        for ( int i = 0; i < A.arrival[ tm ].size(); ++i ) {
                            B.trains[ A.arrival[ tm ][i] + T ]++;
                            A.trains[ tm ]--;
                        }
                        if( A.trains[ tm ] < 0 ) {
//                            cout << "ja1" << endl;
                            flag = false;
                            break;
                        } 
                    }

                    if( B.departure[ tm ] ) {
                        for ( int i = 0; i < B.arrival[ tm ].size(); ++i ) {
                            A.trains[ B.arrival[ tm ][i] + T ]++;
                            B.trains[ tm ]--;
                        }
                        if( B.trains[ tm ] < 0 ) {
//                            cout << "ja2\n";
                            flag = false;
                            break;
                        } 
                    }

                }
                if( flag ) {
                    printf("Case #%d: %d %d\n", ++tcase, na, nb);
                    break;
                }                
            }
            if ( flag ) break;
            
        }
        
        
    }
    
}
