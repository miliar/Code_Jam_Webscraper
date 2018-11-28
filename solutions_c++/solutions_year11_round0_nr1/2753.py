#include <iostream>
using namespace std ;

struct Node{
    char type ;
    int pos ;
} node[1000] ;

int main()
{
    //freopen("in.txt", "r", stdin );
    //freopen("out.txt", "w", stdout );
    
    int sets ;
    
    cin >> sets ;
    for(int s=1; s<=sets; ++s ){
        
        int oPos = 1 ;
        int bPos = 1 ;
        int time = 0 ;
        
        int n ;
        cin >> n ;
        for(int i=0; i<n; ++i ){
            cin >> node[i].type ;
            cin >> node[i].pos ;
        }
        
        int lastO = 0 ;
        int lastB = 0 ;
        for(int i=0; i<n; ++i ){
            if( node[i].type == 'O' ){
                if( lastO+abs(node[i].pos-oPos) < time ){
                    ++time ;
                }
                else{
                    time += lastO+abs(node[i].pos-oPos)-time+1 ;
                }
                
                oPos = node[i].pos ;
                lastO = time ;
            }
            else{
                if( lastB+abs(node[i].pos-bPos) < time ){
                    ++time ;
                }
                else{
                    time += lastB+abs(node[i].pos-bPos)-time+1 ;
                }
                
                bPos = node[i].pos ;
                lastB = time ;
            }
        }
        
        cout << "Case #" << s << ": " ;
        cout << time << endl ;
    }
    
    //system("pause") ;
    return 0 ;
} 
