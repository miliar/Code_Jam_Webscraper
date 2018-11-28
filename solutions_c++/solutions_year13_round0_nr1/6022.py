#include<iostream>
#include<vector>
#include<cstdlib>
#include <cstdio>
#include<cstring>
#define SZ(S) S.size()
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

using namespace std ;
int check(vector<string>S)
{
    int cX = 0 , cO = 0 , cdot = 0 , cT = 0 ;
    bool b = 1 ;
    // 1st ofoki
    for(int i=0 ; i<4 ; i++)
    {
        cX = cO = cdot = cT = 0 ;
        for(int j=0 ; j<4 ; j++)
        {
            if( S[i][j] == 'X' )
                cX++;
            else if( S[i][j] == 'O' )
                cO++;
            else if( S[i][j] == 'T' )
                cT++;
        }
        if( ( cO == 3 && cT == 1 ) || ( cO == 4 ) )
            return 2 ;
        else if( ( cX == 3 && cT == 1 ) || ( cX == 4 ) )
            return 1 ;

    if( cT + cX + cO <  4 )
       b = 0 ;
    }

    for(int j=0 ; j<4 ; j++)
    {
        cX = cO = cdot = cT = 0 ;
        for(int i=0 ; i<4 ; i++)
        {
            if( S[i][j] == 'X' )
                cX++;
            else if( S[i][j] == 'O' )
                cO++;
            else if( S[i][j] == 'T' )
                cT++;
        }
        if( ( cO == 3 && cT == 1 ) || ( cO == 4 ) )
            return 2 ;
        else if( ( cX == 3 && cT == 1 ) || ( cX == 4 ) )
            return 1 ;
    }

    cT = cX = cO = 0;
    for(int i=0 ; i<4 ; i++)
    {
        if( S[i][i] == 'X' )
            cX++;
        else if( S[i][i] == 'O' )
            cO++;
        else if( S[i][i] == 'T' )
            cT++;

//        cout << cT << " " << cO << " " << cX << endl ;

        if( ( cO == 3 && cT == 1 ) || ( cO == 4 ) )
            return 2 ;
        else if( ( cX == 3 && cT == 1 ) || ( cX == 4 ) )
            return 1 ;
    }
//    cout << " ? " ;

    cT = cX = cO = 0;
    for(int i=0 ; i<4 ; i++)
    {

        if( S[i][3-i] == 'X' )
            cX++;
        else if( S[i][3-i] == 'O' )
            cO++;
        else if( S[i][3-i] == 'T' )
            cT++;

        if( ( cO == 3 && cT == 1 ) || ( cO == 4 ) )
            return 2 ;
        else if( ( cX == 3 && cT == 1 ) || ( cX == 4 ) )
            return 1 ;
    }

    if( b == 1 )
        return 3 ;
    return 4;

}
int main ()
{
    // Case #1
    READ("A-large.in");    // esm l downloaded file ay 7aga
    WRITE("A-large.out");  // esm l output file w dah hn3melo upload m3 l source pp

    int t ;
    cin >> t ;

    for(int k=1 ; k<=t ; k++)
    {
        vector<string>grid(4,"....");

        cin >> grid[0] >> grid[1] >> grid[2] >> grid[3] ;

        int res = check(grid) ;

        cout << "Case #" << k << ": " ;

        if( res == 1 )
           cout << 'X'<< " won\n";
        else if( res == 2 )
           cout << 'O'<< " won\n";
        else if( res == 3 )
           cout << "Draw\n";
        else
           cout << "Game has not completed\n";


    }

    return 0 ;
}

//freopen("in.txt", "rt", stdin); // change in.txt to ur input file name, doesn't have to end with .txt
//freopen("out.txt", "wt", stdout); // same for out.txt
/*
#include<algorithm>
#include<iostream>
#include<vector>
#include<cmath>
#define SZ(S) S.size()
using namespace std;
int main ()
{
    int n , m , mini , counter ,ind ;
    cin >> n >> m ;

    vector<int>vec(m,0) , far2(m,0) ;
    for(int i=0 ; i<n ; i++)
    {
        mini = 1000000 , counter = 1 ;

        for(int j=0 ; j<m ; j++)
        {
            if( mini > vec[j] )
            {
                counter = 1 ;
                mini = vec[j] ;
                ind = j ;
            }
            else if( mini == vec[j] )
                counter++;


            far2[j] = abs( (m+1)/2 - j -1 );
        }
  //      cout << "?" ;

//        for(int k = 0 ; k < m ; k++)
//            cout << far2[k] << " " ;
//        cout << endl ;


        if( counter > 1 )
//        {
//            vec[ind]++;
//            cout << ind + 1 ;
//        }
//        else
        {
            int min = *min_element( far2.begin() , far2.end() ) ;



            for(int j=(m+1)/2 , k=(SZ(vec)+1)/2 -1; k>=0 ; j++,k--){
                    cout << k << " " << j << endl ;
                if( vec[k] <= vec[j] && vec[k] == min )
                    ind = k ;
                else if( vec[k] > vec[j] && vec[j] == min )
                    ind = j ;
            }
        }
        cout << "---------\n";

        vec[ind]++;
   //     cout << ind + 1 << endl ;
    }

    return 0 ;
}*/
