#include <cstdlib>
#include <iostream>
#include <deque>
#include <queue>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>

bool isgood [11][40000000];
bool checked [11][40000000];
bool visited [11][40000000];

using namespace std;

// sprawdza i zapisuje
bool sprawdz ( int b, int n ) {
    //cout << ".";
    if ( checked [b][n]  )
        return isgood[b][n];   
    if ( visited [b][n] ) {
        return false;
    }
    visited[b][n] = true;
    
    int nextn= 0;
    int tempn = n;
    while ( tempn > 0 ) {
        nextn += (tempn%b) * (tempn%b);
        tempn /= b;
    }
    bool wynik = sprawdz ( b, nextn);
    checked [b][n] = true;
    isgood [b][n] = wynik;
    visited[b][n] = false;
    return wynik;
}

int main(int argc, char *argv[])
{
    memset ( checked, 0, sizeof ( checked ) );
    memset ( isgood, 0, sizeof ( isgood));
    isgood[2][1] = true;
    isgood[3][1] = true;
    isgood[4][1] = true;
    isgood[5][1] = true;
    isgood[6][1] = true;
    isgood[7][1] = true;
    isgood[8][1] = true;
    isgood[9][1] = true;
    isgood[10][1] = true;
    checked[2][1] = true;
    checked[3][1] = true;
    checked[4][1] = true;
    checked[5][1] = true;
    checked[6][1] = true;
    checked[7][1] = true;
    checked[8][1] = true;
    checked[9][1] = true;
    checked[10][1] = true;
    int n;
    int maxsat = 0;
    for (  n = 2; n < 40000000; n ++) {
        //cout << n << endl;
        // for each base 
        for ( int b = 2; b <= 10; b ++) {
       //     memset ( visited, 0, sizeof ( visited));   
            sprawdz ( b, n );
        }     
        // check if all bases good
        
        int count = 0;
        for ( int b = 2; b <= 10; b ++)
            if (  isgood[b][n] )
                count ++;
        if ( count > maxsat ) {
            cout << maxsat << endl;
            maxsat = count;      
    }    
//        cout << count << endl;
        if ( count == 9 )
            break;
        
    }
    //cout << "ha!" << endl;
    int cases ;
    cin >> cases;
    char buf [100];
    cin.getline (buf, 90);
    for ( int c = 1; c <= cases; c++) {
        vector < int > testy;
        
        cin.getline ( buf , 90);
        stringstream ss (buf);
        
        int temp, last = 0;
        ss >> temp;
        
        while ( temp != last) {
           // cout << temp;
            testy.push_back ( temp);
            last = temp;
            ss >> temp;    
         //   cout << " " << temp;
        }    
       // cout << " --- " << endl; 

        int best = 0;
        for ( int n = 2; n < 40000000; n ++)  {
            int good  = 1;   
            for ( int t = 0; t < testy.size(); t++) {
                if ( !isgood [testy[t]][n] )
                    good = 0;
            }
            if ( good ){
                best = n;
                break;}
            
        }
    
        cout << "Case #" << c << ": " << best << endl;
        
    }

    return EXIT_SUCCESS;
}
