#include<iostream>
#include<set>
using namespace std;

set<int> st;
int n, a, b, dc[10];

void init() {
   dc[0] = 1;
   for( int i = 1; i < 10; i++ ) {
        dc[i] = dc[i-1] * 10;
   } 
}

int cutted( int v, int c, int mc ) {
    //cout << ( v / ( dc[c] ) ) << "+" << ( v % ( dc[c] ) ) << "*" << dc[mc-c] << "*";
    return ( v / ( dc[c] ) ) + ( v % ( dc[c] ) ) *  dc[mc - c];
}

int casas( int v ) {
    int c = 1;    
    while( v / 10 > 0 ) { c++; v /= 10; }
    return c;
}

int main() {
    cin >> n;
    init();

    for( int cas = 1; cas <= n; cas++ ) {
         st.clear();
         cin >> a >> b;
         int c = casas( a );
         int r = 0;
         for( int v = a; v <= b; v++ ) {
              //cout << v << " - ";
              //st.insert(v);
              for( int i = 1; i < c; i++ ) {
                   int g = cutted( v, i, c );
                   //cout << g << " ";
                   if(g > v && g <= b ) 
                   {
                       r++;
                       if( st.count( g ) == 0 ) {
                           st.insert( g ); 
                       } else {
                              //r++;
                           //cout << g << "(" << v <<")*";
                       }
                   }
              }
         }
         //cout << "    lasting" << r << "  --  " << ( r + st.size() ) << endl;
         cout << "Case #" << cas << ": " << r /*st.size()*/ << endl;
    }

    return 0;
}
