#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int test, test1, i, j;
    vector< char > v( 26, 'a' );
    v[0] = 'y';
    v[1] = 'h';
    v[2] = 'e';
    v[3] = 's';
    v[4] = 'o';
    v[5] = 'c';
    v[6] = 'v';
    v[7] = 'x';
    v[8] = 'd';
    v[9] = 'u';
    v[10] = 'i';
    v[11] = 'g';
    v[12] = 'l';
    v[13] = 'b';
    v[14] = 'k';
    v[15] = 'r';
    v[16] = 'z';
    v[17] = 't';
    v[18] = 'n';
    v[19] = 'w';
    v[20] = 'j';
    v[21] = 'p';
    v[22] = 'f';
    v[23] = 'm';
    v[24] = 'a';
    v[25] = 'q';
    string s;
    getline( cin, s );
    test1 = atoi( s.c_str() );
    
    for ( test = 1; test <= test1; test ++ ) {
        getline( cin, s );
        cout << "Case #" << test << ": ";
        
        for ( i = 0; i < s.size(); i ++ ) {
            if ( s[i] >= 97 ) {
                 cout << v[s[i] - 97];
            } else {
                   cout << s[i];
            }
        }
        
        cout << "\n";
    }
    
    
    
   // system( "pause" );
    
    
    return 0;
}
        
