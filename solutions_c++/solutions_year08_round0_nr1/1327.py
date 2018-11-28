#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <functional>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <queue>
#include <vector>
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
#define fora(i,v) for(int i = 0; i < (v).size(); i++)
#define all(v) (v).begin(), (v).end()
int main()
{
    ifstream input( "test.in" );
    ofstream output( "test.out" );
    int N; input >> N;
    for( int n = 0; n < N; ++n )
    {
        int result = 0;
        int S; input >> S;
        map<string, int> M;
        vi A(S), B(S), C;
        char buf[1000];
        input.getline( &buf[0], 200 );
        for( int s = 0; s < S; ++s )
        {
            input.getline( &buf[0], 200 );
            string x = string(buf);
            M[x] = s;
        }
        int Q; input >> Q;
        input.getline( &buf[0], 200 );
        for( int q = 0; q < Q; ++q )
        {
            input.getline( &buf[0], 200 );
            string x = string(buf);
            int k = M[x];
            fora(i, B)
            {
                C = A; C[k] = 1000; --C[i];
                B[i] = *min_element( all(C) ) + 1;
            }
            B.swap( A );
        }
        result = *min_element( all(A) );
        output << "Case #" << n + 1 << ": " << result << endl;
    }        
	return 0;
}