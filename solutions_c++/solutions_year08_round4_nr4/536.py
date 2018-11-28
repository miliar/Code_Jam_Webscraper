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
#define fora(i,v) for(int i = 0; i < (v).size(); i++)
#define all(v) (v).begin(), (v).end()
int main()
{
	ifstream input( "test.in" );
	ofstream output( "test.out" );
    int N; input >> N;
    for( int n = 0; n < N; ++n )
    {
        int k; input >> k;
        string S; input >> S;
        int s = S.size();
        int result = s;
        vi A(k);
        fora(i, A)
            A[i] = i;
        string T(S);
        do 
        {
            fora(i, T)
                T[i] = S[i / k * k + A[i % k]];
            int current = 1;
            for( int i = 1; i < s; ++i )
                if ( T[i] != T[i - 1] )
                    ++current;
            result = min(result, current);
        } while (next_permutation(all(A)));
        output << "Case #" << n + 1 << ": " << result << endl;
    }        
	return 0;
}