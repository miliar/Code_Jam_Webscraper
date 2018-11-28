#include <cstdlib>
#include <iostream>
#include <deque>
#include <queue>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

string welcome = "welcome to code jam";


using namespace std;

int main(int argc, char *argv[])
{
    int N;
    cin >> N;
    char bufer [3]; 
    cin.getline(bufer, 2);
    
    for ( int caseno = 1; caseno <= N; caseno ++ ) {
        char buf [1000];
        cin.getline(buf, 900);
        
        string s = buf;
         
        int tab[501][21];
        

        tab [ s.size()][0] = 1;
        for ( int i = 1; i < 21; i ++)
            tab[ s.size()] [i] = 0;
        for ( int i = 0; i < s.size(); i++)
            tab[i][0] = 1;
        int wpos, spos;
        for ( wpos = 1; wpos <= welcome.size() ; wpos ++) {
            for ( spos = s.size()-1; spos >= 0; spos --) { 
                tab [spos][wpos] = tab [ spos +1][wpos];
                if ( s [ spos ] == welcome [welcome.size() - wpos] ) 
                    tab [ spos ][ wpos ] += tab [ spos +1][wpos -1];
                tab [spos][wpos] %= 10000; 
            }
        }
           
        int result = tab[0][19];
        cout << "Case #" << caseno << ": ";
        cout << result / 1000;
        result %= 1000;
        cout << result / 100;
        result %= 100;
        cout << result / 10;
        result %= 10;
        cout << result << endl;
    }
    
    return EXIT_SUCCESS;
}
