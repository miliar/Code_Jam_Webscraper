#include <map>
#include <queue>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main(int argc, char *argv[])
{

   
    int testCases;
    cin >> testCases;

    for ( int testCase = 1; testCase <= testCases; testCase ++ ) {
        int N, M, A;
        cin >> N >> M >> A;
        int x1, x2, y1, y2;
        for (  x1 = 0; x1 <= N; x1 ++ )
            for (  y1 = 0; y1 <= M; y1 ++ )
                for (  x2 = 0; x2 <= N; x2 ++ )
                    for (  y2 = 0; y2 <= M; y2 ++)
                        if ( abs ( x1 * y2 - x2 * y1 ) == A )
                           goto done; 
          cout << "Case #" << testCase << ": IMPOSSIBLE" << endl;
          continue;               
       done: 
        cout << "Case #" << testCase << ": "<< x1 << " " << y1 << " " << x2 << " " << y2 << " " << 0 << " " << 0 << endl;
    }
    //cout << "done";

    
    
    return 0;
}
