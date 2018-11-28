#include <iostream>
#include <fstream>
using namespace std ;

int main()
{
    ifstream fin("B-small-attempt2.in");
    ofstream fout("B-small.out") ;
    int Case = 1 , c , N , M;
    long A ;
    fin >> c ;
    while( c-- > 0 ){
            fin >>N >> M >> A ;
            fout << "Case #" << Case << ": " ;  
            bool b = false ;                                  
                        for( int i = 0 ; i <= N ; ++i  ){
                          for( int j =0 ; j <= M ; ++j  ){
                               for( int m = 0 ; m <= N ; ++m  ){
                                    for( int n = 0 ; n <= M ; ++n  ){
                                         int t = i*n - m*j ;
                                         if( t < 0 ) t = -t ;
                                         if( t == A ){
                                              fout << "0 0 " << i<<' ' << j <<' '<< m<< ' ' << n << endl;
                                              b = true ;
                                         }
                                         if( b ) break ;                                          
                                    }
                                    if( b ) break ;
                               }
                               if( b ) break ;
                          }
                          if( b ) break ;
                        }
                              
                            
                             
            if( !b )  fout << "IMPOSSIBLE\n" ;  
            ++Case ;          
    } 
}  
