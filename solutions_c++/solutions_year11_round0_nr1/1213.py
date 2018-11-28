#include<iostream>
#include<fstream>
#include<math.h>
#include<stdlib.h>

using namespace std;

int main( void ){
    
    int b,o,bt,ot,now,i,j,p,n,m;
    char c;
    ofstream outFile( "ans.txt" );
    
    cin >> n;
    for( i = 0 ; i < n ; i++ ){
        
        cin >> p;
        now = bt = ot = 0;
        b = o = 1;
        
        for( j = 0 ; j < p ; j++ ){
            cin >> c >> m;
            if( c == 'O' ){
                if( now - ot >= abs( o - m ) + 1 ){
                    now = ot = now + 1;
                    o = m;
                }else{
                    now = ot = ot + abs( o - m ) + 1;
                    o = m;
                }
            }else{
                if( now - bt >= abs( b - m ) + 1 ){
                    now = bt = now + 1;
                    b = m;
                }else{
                    now = bt = bt + abs( b - m ) + 1;
                    b = m;
                }
            }
        }
        outFile << "Case #" << i+1 << ": " << now << endl;
    }
    return 0;
}
