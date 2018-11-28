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

typedef pair<int,int> Wire;

bool intersect( Wire w1, Wire w2 )
{
    return ( w1.first < w2.first && w1.second > w2.second ) || ( w1.first > w2.first ) && ( w1.second < w2.second );
}

int main()
{
    int num_cases;
    cin >> num_cases;

    for ( int case_num = 0; case_num < num_cases; case_num++ )
    {
        cout << "Case #" << case_num + 1 << ": ";
        int N;
        cin >> N;
        vector<Wire> wires(N);
        for ( int i = 0; i < N; i++ )
            cin >> wires[i].first >> wires[i].second;

        sort( wires.begin(), wires.end() );
        int intersections = 0;
        for ( int i = 0; i < N; i++ )
            for ( int j = i+1; j < N; j++ )
                if ( intersect( wires[i], wires[j] ) )
                    intersections++;

        cout << intersections << endl;
    }

    return EXIT_SUCCESS;
}
