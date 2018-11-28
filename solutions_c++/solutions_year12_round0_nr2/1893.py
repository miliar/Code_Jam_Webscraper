#include <iostream>
#include <fstream>

using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");

int main() {
    int T, N, S, p;
    in >> T;

    for (int tcase = 1; tcase <= T; tcase++ ) {
        in >> N >> S >> p;
        int ans = 0;
        for( int i=0; i<N; i++ ) {
            int total, low;
            in >> total;
            if( total == 0 || total == 1 ) ans += (p<=total);
            else if( total == 29 || total == 30 ) ans ++;
            else {
                low = (total-p)/2;
                if( low < p-2 ) continue; //not possible
                else if( low == p-2 ) {
                    if( S > 0 ) {
                        S--, ans++;
                    }
                }
                else ans++;
            }
        }
        out << "Case #" << tcase << ": " << ans << endl;
    }
    return 0;
}


