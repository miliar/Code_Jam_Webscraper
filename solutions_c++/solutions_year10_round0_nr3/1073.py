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
        int R, k, N;
        cin >> R >> k >> N;

        vector<int> groups(1000);
        for ( int i = 0; i < N; i++ )
            cin >> groups[i];
        vector<long long> euro_acc(1000,0);
        vector<int> ride_acc(1000,0);
        vector<bool> flag(1000,false);

        int p = 0;
        bool rem = false;
        long long euro = 0;
        int ride = 0;
        while ( ride < R )
        {
            int pirc = 0;
            int p_beg = p;
            while ( pirc + groups[p] <= k )
            {
                pirc += groups[p];
                p++;
                if ( p == N )
                    p = 0;
                if ( p == p_beg )
                    break;
            }
            euro += pirc;
            ride++;

            if ( flag[p] == false )
            {
                euro_acc[p] = euro;
                ride_acc[p] = ride;
                flag[p] = true;
            }
            else if ( rem == false )
            {
                int cycle_length = ride - ride_acc[p];
                int rem_ride_cycle = (R - ride_acc[p])/cycle_length;
                euro = euro_acc[p] + ( euro - euro_acc[p])*rem_ride_cycle;
                ride = ride_acc[p] + rem_ride_cycle*cycle_length;
                rem = true;
            }
        }

        cout << "Case #" << case_num + 1 << ": " << euro << endl;
    }

    return EXIT_SUCCESS;
}
