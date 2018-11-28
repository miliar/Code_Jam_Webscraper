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
int main()
{
	ifstream input( "test.in" );
	ofstream output( "test.out" );
    int T; input >> T;
    for( int t = 0; t < T; ++t )
    {
        int K, n; input >> K >> n;
        vi d(n);
        for( int i = 0; i < n; ++i )
            input >> d[i];
        vi X(K), A(K), B(K);
        fora(i, X)
            X[i] = i;
        int current = 0, size = K;
        for( int i = 0; i < K; ++i )
        {
            current = (current + i) % size;
            A[i] = X[current];
            X.erase( X.begin() + current );
            --size;
        }
        for( int i = 0; i < K; ++ i)
            B[A[i]] = i + 1;
        output << "Case #" << t + 1 << ":";
        fora(i, d)
           output << " " << B[d[i] - 1];
        output << endl;
    }        
	return 0;
}