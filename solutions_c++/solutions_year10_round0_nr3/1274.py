#include <stdlib.h>

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main(int argc, char** argv) {
    if( argc != 2 )
        return 0;

    ifstream in( (string(argv[1])+".in").c_str() );
    ofstream out( (string(argv[1])+".out").c_str() );

    int T;
    long long G[1000];
    int pos[1000];
    long long num[1000];
    int steps[1000];
    long long sums[1000];

    in >> T;
    for( int i=1; i<=T; ++i ) {
        long long R;
        long long k;
        int N;
        in >> R >> k >> N;
        for( int j=0; j<N; ++j )
            in >> G[j];

        for( int j=0; j<N; ++j) {
            long long sum = 0;
            int x=0;
            for( x=0; x<N; ++x ) {
                int xr = (j+x)%N;
                if( sum+G[xr] > k )
                    break;
                sum += G[xr];
            }
            pos[j] = (x+j) % N;
            num[j] = sum;
        }
        
        long long result = 0;
        int tmp = N;
        if( R <= tmp ) {
           int cur_ind = 0;
           for( long long j=0; j<R; ++j ) {
               result += num[cur_ind];
               cur_ind = pos[cur_ind];
           }
        } else {
            for( int j=0; j<N; ++j ) {
                steps[j] = -1;
                sums[j] = 0;
            }
            long long cycle_shift = 0;
            long long cycle_len = 0;
            long long cycle_sum = 0;

            int cur_ind = 0;
            long long current_sum = 0;
            for( int j=0; j<=N; ++j) {
                if( steps[cur_ind] != -1 && j != 0 ) {
//                    cout << "j = " << j << " cur_ind = " << cur_ind << " current_sum = " << current_sum << endl;
                    cycle_shift = steps[cur_ind];
                    cycle_len = j - cycle_shift;
                    cycle_sum = current_sum - sums[cur_ind];
                    break;
                }
                steps[cur_ind] = j;
                sums[cur_ind] = current_sum;

                current_sum += num[cur_ind];
                cur_ind = pos[cur_ind];
//                cout << " cur_ind = " << cur_ind << endl;
            }

//            cout << "cycle_shift = " << cycle_shift
//                    << " cycle_len = " << cycle_len << " cycle_sum = " << cycle_sum << endl;

            long long j = 0;
            cur_ind = 0;
            for( ; j<cycle_shift; ++j ) {
                result += num[cur_ind];
                cur_ind = pos[cur_ind];
            }
            long long cycle_num = ( R - cycle_shift ) / cycle_len;
            result += cycle_num * cycle_sum;
            for( j=cycle_shift+cycle_num*cycle_len; j<R; ++j ) {
                result += num[cur_ind];
                cur_ind = pos[cur_ind];
            }

        }
        out << "Case #" << i << ": " << result << endl;

    }

    return 0;
}
