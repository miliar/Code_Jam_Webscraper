#include <map>
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

#define ll long long
long long tab [ 110][110];




int min ( int a, int b) {
    if ( a < b )
    return a;
    return b;
}

// a - gcd
// b - x
// c - y



int main(int argc, char *argv[])
{
    int dx []  = { -1, -2};
    int dy [] = { -2 , -1};
    
    
    int testCases;
    cin >> testCases;

    for ( int testCase = 1; testCase <= testCases; testCase ++ ) {
        long long H, W, R;
        cin >> H >> W >> R;
        vector < int > xv;
        vector < int > yv;
        memset ( tab , 0, sizeof ( tab ));
        tab [ H][W] = 1;
        for ( int i = 0 ; i < R; i++ ) {
            long long tmpx, tmpy; cin >> tmpx >> tmpy ; 
            xv.push_back ( tmpx );
            yv.push_back ( tmpy );
            tab [tmpx][tmpy] = -1;
        }

        for ( int h = W ; h >= 1; h --)
         for ( int w = H; w >= 1; w -- ) {
               if ( tab [ w][h] != -1) {
               if ( w + dx[0] >= 1 && h + dy[0] >= 1 && tab [w+ dx[0]][h + dy[0]] != -1 ) {
                  tab [w+ dx[0]][h + dy[0]] += tab [w][h];
                  tab [w+ dx[0]][h + dy[0]] =  (tab [w+ dx[0]][h + dy[0]]) % 10007 ; 
               }
               if ( w + dx[1] >= 1 && h + dy[1] >= 1  && tab [w+ dx[1]][h + dy[1]]!= -1) {
                  tab [w+ dx[1]][h + dy[1]] += tab [w][h];
                  tab [w+ dx[1]][h + dy[1]] =  (tab [w+ dx[1]][h + dy[1]])  % 10007 ;
                  }
             }  
       
       
          
    }
      cout << "Case #" << testCase << ": "<< tab[1][1]<< endl;
    }   
    
      
    return 0;
}
