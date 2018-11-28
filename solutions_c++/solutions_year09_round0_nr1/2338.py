#include<iostream>
#include<string>
#include<fstream>
#include<vector>
using namespace std;

int l, d, n ;
vector < string > A;

ofstream fout("AA1.out");
ifstream fin("AAA.in");

void unesi() {
     
     fin >> l >> d >> n;    
     
     string s;
     for( int i = 0; i < d; i++ ) {
          fin >> s;
          A.push_back( s );
     }
          
}

int ret() {
    
    string x;
    fin >> x;
    
    vector < string > v;
    
    v.resize( l );
    
    int k = 0;
    for( int i = 0; i < x.size(); i++ ) {
         
         if( x[ i ] == '(' ) {
             
             for( int j = i + 1; j < x.size(); j++ ) {
                  
                  if( x[ j ] == ')' ) { 
                      i = j; k++;
                      break;
                  }
                  v[ k ] += x[ j ];
                          
             }
                 
         } else v[ k++ ].push_back( x[ i ] );
                  
    }
    
    int rj = 0;
    for( int i = 0; i < d; i++ ) {
         
         bool moze = 1;
         
         for( int j = 0; j < l; j++ ) {
              
              bool ok = 0;
              for( int I = 0; I < v[ j ].size(); I++ ) 
              if( A[ i ][ j ] == v[ j ][ I ] ) ok = 1;
              
              if( !ok ) moze = 0;   
                   
         }
         
         rj += moze;     
    }
    
    return rj;
        
}

int main() {
    
    unesi();
    
    for( int i = 0; i < n; i++ ) {
         
         fout << "Case #" << i + 1 << ": " << ret() << endl;
              
    }    
    
    return 0;    
}
