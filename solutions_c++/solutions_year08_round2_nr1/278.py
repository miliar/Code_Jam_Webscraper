#include <map>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
long long tab [ 3][3];

int main(int argc, char *argv[])
{
    
    
    int testCases;
    cin >> testCases;

    for ( int testCase = 1; testCase <= testCases; testCase ++ ) {
        memset ( tab, 0, sizeof ( tab));
        int tri;
        cin >> tri;
        long long A, B, C, D, x0, y0, M;
        cin >> A >> B >> C >> D >> x0 >> y0 >> M;
        long long X = x0;
        long long Y = y0;
        vector < long long > xv; xv.push_back (X);
        vector < long long > yv; yv.push_back (Y);
        tab [ X % 3   ] [ Y % 3   ] += 1;
        long long zero, one , two;
        zero = 0; one = 0; two = 0;
        
        for ( int i = 1; i < tri; i++) {
            X = (A * X + B) % M;
            Y = (C * Y + D) % M;
            xv.push_back ( X);
            yv.push_back ( Y);
        //    cout << " x " << X << ", " << Y << endl;;
            tab [ X % 3   ] [ Y % 3   ] += 1;
            
        }
        long long alter = 0;
        for ( int a = 0 ; a < 9; a ++ )
            for ( int b = a; b < 9; b ++)
                for ( int c = b; c < 9; c++) 
                    if ( (a /3 + b/3 + c/3 )% 3 == 0 && (b %3 + a%3 + c%3) %3 == 0 ){
                    
                    if ( a != b && b != c )
                       alter += tab[ a/3 ][a % 3] * tab[ b / 3][b % 3] * tab [ c / 3][c % 3];
                    if ( a == b && a == c &&  tab[ a/3 ][a % 3] >= 3 )
                       alter += tab[ a/3 ][a % 3] * (tab[ b / 3][b % 3]-1) * (tab [ c / 3][c % 3]-2) / 6;
                    if ( a ==b && a != c && tab[ a/3 ][a % 3] >= 2 )  
                     alter += tab[ a/3 ][a % 3] * (tab[ b / 3][b % 3]-1) * (tab [ c / 3][c % 3]) / 2;
                    if ( a != c && b == c && tab[ b/3 ][b % 3] >= 2 )  
                     alter += tab[ a/3 ][a % 3] * (tab[ b / 3][b % 3]-1) * (tab [ c / 3][c % 3]) / 2;
                     
                }
                    
       // long long count = 0;
        /*for ( int i = 0; i < xv.size(); i++)
        for ( int j = i + 1; j < xv.size() ; j++)
        for ( int k = j + 1; k < xv.size(); k++)
            if ( i != k && j != k && i != j )
               if ( (xv[i] + xv[j] + xv [ k] ) % 3 == 0  && (yv[i] + yv[j] + yv [ k] ) % 3 == 0 )
                  count ++;*/
        cout << "Case #" << testCase << ": "<< alter  << endl;
    }
    //cout << "done";

    
    
    return 0;
}
