#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>

#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>

using namespace std;

int main()
{
    int num_cases;
    cin >> num_cases;

    for ( int case_num = 0; case_num < num_cases; case_num++ )
    {
        int N, K;
        cin >> N >> K;

        vector<bool> power( N, false ), on( N, false );
        power[0] = true;

        for ( int snap = 0; snap < K; snap++ )
        {
            for ( int i = 0; i < N; i++ )
            {
                if ( power[i] == true )
                    on[i] = not on[i];
                if ( i != 0 && power[i-1] && on[i-1] )
                    power[i] = true;
                else if ( i != 0 )
                    power[i] = false;
            }

        }

        cout << "Case #" << case_num + 1 << ": ";
        if ( power[N-1] == true && on[N-1] == true ) 
            cout << "ON" << endl;
        else
            cout << "OFF" << endl;
    }

    return EXIT_SUCCESS;
}
