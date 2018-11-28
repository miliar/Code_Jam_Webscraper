#include<iostream>
#include<fstream>

using namespace std;

int main( void ){
    
    int n,m,i,j,k,sum,tmp,x;
    ofstream outFile( "ans3.txt" );
    
    cin >> n;
    for( i = 0 ; i < n ; i++ ){
        
        cin >> m;
        k = 10000000;
        sum = 0;
        x = 0;
        
        for( j = 0 ; j < m ; j++ ){
            
            cin >> tmp;
            if( tmp < k ) k = tmp;
            x = x ^ tmp;
            sum += tmp;
            
        }
        outFile << "Case #" << i+1 << ": ";
        if( x ){
            outFile << "NO" << endl;
        }else{
            outFile << sum - k << endl;
        }
        
    }
    
    return 0;
    
}
