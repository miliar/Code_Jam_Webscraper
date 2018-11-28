#include <iostream>
#include <vector>
#include <utility>
#include <cassert>

using namespace std;

int N, W, L;
int R[1024];

void scan(){
    cin >> N >> W >> L;
    for ( int i = 0; i < N; ++i )
        cin >> R[i];
}

void solve(int cs){
    vector < pair < double, double > > v;

    double MxW = R[0], curL = R[0], lastW = -1e9;
    v.push_back ( make_pair ( 0, 0 ) );

    for ( int i = 1; i < N; ++i ){
        if ( curL + R[i] > L ){
            curL = -1e9;
            lastW = MxW;
        }

        double x = lastW + R[i], y = curL + R[i];
        x = max ( x, 0.0 );
        y = max ( y, 0.0 );
        v.push_back ( make_pair ( x, y ) );
        MxW = max ( MxW, x + R[i] );
        curL = y + R[i];
    }

    cout << "Case #" << cs << ":";

    for ( int i = 0; i < v.size(); ++i ){
        assert (  v[i].first <= W || v[i].second <+ L );
        cout << " " << (int)v[i].first << " " << (int)v[i].second;
    }
    cout << endl;


}

int main(){
    int tests;
    cin >> tests;


    for ( int i = 1; i <= tests; ++i ){
        scan();
        solve(i);
    }
}
