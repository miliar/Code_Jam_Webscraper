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
        int result = 0;
        int M, V; input >> M; input >> V;
        vi G((M - 1) / 2), C((M - 1) / 2), A(M), x0(M), x1(M);        
        fora(i, G)
            input >> G[i] >> C[i];
        for( int i = 0; i < (M + 1) / 2; ++i )
            input >> A[(M - 1) / 2 + i];
        for( int i = (M - 1) / 2; i < M; ++i )
        {
            if ( A[i] == 1 )
            {
                x1[i] = 0; x0[i] = 10000;
            }
            else
            {
                x1[i] = 10000; x0[i] = 0;
            }
        }
        for( int i = (M - 1) / 2 - 1; i >= 0; --i )
        {
            if ( C[i] == 0 )
            {
                if ( G[i] == 0 )
                {
                    x0[i] = x0[i * 2 + 1] + x0[i * 2 + 2];
                    vi x;
                    x.push_back(x0[i * 2 + 1] + x1[i * 2 + 2]);
                    x.push_back(x1[i * 2 + 1] + x0[i * 2 + 2]);
                    x.push_back(x1[i * 2 + 1] + x1[i * 2 + 2]);
                    x1[i] = *min_element(all(x));
                }
                else
                {
                    x1[i] = x1[i * 2 + 1] + x1[i * 2 + 2];
                    vi y;
                    y.push_back(x0[i * 2 + 1] + x1[i * 2 + 2]);
                    y.push_back(x1[i * 2 + 1] + x0[i * 2 + 2]);
                    y.push_back(x0[i * 2 + 1] + x0[i * 2 + 2]);
                    x0[i] = *min_element(all(y));
                }
            }
            else
            {
                if ( G[i] == 0 )
                {
                    vi x;
                    x.push_back(x0[i * 2 + 1] + x1[i * 2 + 2]);
                    x.push_back(x1[i * 2 + 1] + x0[i * 2 + 2]);
                    x.push_back(x1[i * 2 + 1] + x1[i * 2 + 2]);
                    x1[i] = min(*min_element(all(x)), x1[i * 2 + 1] + x1[i * 2 + 2] + 1);
                    vi y;
                    y.push_back(x0[i * 2 + 1] + x1[i * 2 + 2]);
                    y.push_back(x1[i * 2 + 1] + x0[i * 2 + 2]);
                    y.push_back(x0[i * 2 + 1] + x0[i * 2 + 2]);
                    x0[i] = min(*min_element(all(y)) + 1, x0[i * 2 + 1] + x0[i * 2 + 2]);
                }
                else
                {
                    vi x;
                    x.push_back(x0[i * 2 + 1] + x1[i * 2 + 2]);
                    x.push_back(x1[i * 2 + 1] + x0[i * 2 + 2]);
                    x.push_back(x1[i * 2 + 1] + x1[i * 2 + 2]);
                    x1[i] = min(*min_element(all(x)) + 1, x1[i * 2 + 1] + x1[i * 2 + 2]);
                    vi y;
                    y.push_back(x0[i * 2 + 1] + x1[i * 2 + 2]);
                    y.push_back(x1[i * 2 + 1] + x0[i * 2 + 2]);
                    y.push_back(x0[i * 2 + 1] + x0[i * 2 + 2]);
                    x0[i] = min(*min_element(all(y)), x0[i * 2 + 1] + x0[i * 2 + 2] + 1);
                }                
            }
        }
        if ( V == 0 && x0[0] >= 10000 || V == 1 && x1[0] >= 10000 )
            output << "Case #" << n + 1 << ": IMPOSSIBLE" << endl;
        else 
        {
            if ( V == 0 )
                result = x0[0];
            else
                result = x1[0];
            output << "Case #" << n + 1 << ": " << result << endl;
        }
    }        
	return 0;
}