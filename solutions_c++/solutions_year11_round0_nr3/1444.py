#include <fstream>

using namespace std;

int main(){
    int i, j, t, n;
    unsigned x, s, m, sum;
    ifstream f ( "candy.in" );
    ofstream g ( "candy.out" );
    f >> t;
    for ( j = 1; j <= t; ++ j ) {
        f >> n;
        s = sum = 0;
        m = 1000000000;
        for ( i = 0; i < n; ++ i ){
            f >> x;
            s ^= x;
            sum += x;
            m = min ( m, x );
        }
        if ( s ){
            g << "Case #" << j << ": NO" << endl;
        }
        else {
            sum -= m;
            g << "Case #" << j << ": " << sum << endl;
        }
    }
    f.close();
    g.close();
    return 0;
}
