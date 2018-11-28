using namespace std;

#include <iostream>
#include <string>
#include <map>
#include <list>
#include <stdio.h>

bool findKinline( unsigned long long *table, int tsize, int K )
{
    int ii, jj, xx; 
    // find horizontal 
    unsigned long long mask = ( 1 << K ) -1;  
    unsigned long long tmp; 
    for( ii = 0; ii < tsize; ++ii ){
         tmp = table[ii]; 
         for( jj = 0; jj <= tsize - K; ++jj ){
            if( (tmp & mask) == mask ) 
                return true; 
            tmp = tmp >> 1; 
         }
    }

    // find vertical 
    int count; 
    mask = 1; 
    for( ii = 0; ii < tsize; ++ii ){
        count = 0;
        mask = 1 << ii; 
        for( jj = 0; jj < tsize; ++jj ){
            if( table[jj] & mask ){
                ++count; 
            }else{
                count = 0; 
            }
            
            if( count == K ) 
                return true; 
        }
    }

    // find diagonals 
    int l2r, r2l; 
    unsigned long long r2l_mask, l2r_mask;
    for( ii = 0; ii < tsize; ++ii ){
        l2r_mask = ( 1 << (tsize -ii -1) );
        r2l_mask = ( 1 << ii );
        
        l2r = r2l = 0; 

        for( jj = 0; jj < tsize; ++jj ){
            if( table[jj] & l2r_mask ){
                ++l2r; 
            }else{
                l2r = 0; 
            }

            if( table[jj] & r2l_mask ){
                ++r2l;
            }else{
                r2l = 0; 
            }

            if( l2r == K || r2l == K ) 
                return true;

            l2r_mask = l2r_mask >> 1; 
            r2l_mask = r2l_mask << 1; 
        }
    }


    for( ii = 1; ii < tsize; ++ii ){
        l2r_mask = 1 << (tsize -1);
        r2l_mask = 1;
        
        l2r = r2l = 0; 

        for( jj = ii; jj < tsize; ++jj ){
            if( table[jj] & l2r_mask ){
                ++l2r; 
            }else{
                l2r = 0; 
            }

            if( table[jj] & r2l_mask ){
                ++r2l;
                //std::cout <<  "hhhhh " << r2l << std::endl; 
            }else{
                r2l = 0; 
            }

            if( l2r == K || r2l == K ) 
                return true;

            l2r_mask = l2r_mask >> 1; 
            r2l_mask = r2l_mask << 1; 
        }
    }
    
    return false; 
}

void printB( int n, unsigned long long *r, unsigned long long *b )
{
    std::cout << "----------------------" << std::endl; 
    for( int i=0; i < n; ++i ){
        std::cout << r[i] << std::endl; 
    }
    
    std::cout << std::endl; 
    for( int j=0; j < n; ++j ){

        std::cout << b[j] << std::endl; 
    }
    std::cout << "----------------------" << std::endl; 
}


int main( int argc, char* argv[] )
{

    int ncases, curcase;

    std::cin >> ncases; 
    int N, K;
    unsigned long long rtable[50]; 
    unsigned long long btable[50]; 
    unsigned long long rline;
    unsigned long long bline; 

    string line; 
    int ii, jj; 

    bool bres; 
    bool rres; 
    for( curcase = 0; curcase < ncases; ++curcase ){
        std::cin >> N; 
        std::cin >> K; 

        for( ii=0; ii < N; ++ii ){
            std::cin >> line;
            
            rline = 0; 
            bline = 0; 
            
            //std::cout << line << std::endl;
            // build the bitmap lines 
            for( jj=0; jj < N; ++jj ){
                
                if( line[jj] == 'R' ){
                    rline = rline << 1;
                    bline = bline << 1; 

                    rline = rline | 1; 
                }else if( line[jj] == 'B' ){
                    rline = rline << 1; 
                    bline = bline << 1;
          
                    bline = bline | 1; 
                }
            }

            btable[ii] = bline;
            rtable[ii] = rline; 
        }
       
        //printB( N, rtable, btable ); 
        bres = findKinline( btable, N,  K );
        rres = findKinline( rtable, N,  K ); 
        if( bres ){
            if( rres ){
                std::cout << "Case #" << (curcase +1) << ": " << "Both" << std::endl;  
            }else{
                std::cout << "Case #" << (curcase +1) << ": " << "Blue" << std::endl;  
            }
        }else{
            if( rres ){
                std::cout << "Case #" << (curcase +1) << ": " << "Red" << std::endl;  
            }else{
                std::cout << "Case #" << (curcase +1) << ": " << "Neither" << std::endl;  
            }
        }

        //std::cout << std::endl << std::endl; 
    }

    return 0;
}
