#include <iostream>

using namespace std;

int main( int argc, char** argv ) {
    int T, N, P;
    int total_time, orange_pos, blue_pos;
    char R;

    int delta;

    // time of last button press == tlbp
    int tlbp_o, tlbp_b;

    cin >> T;
    for ( int i = 0; i < T; ++i ) {
        cin >> N;
        total_time = 0;
        orange_pos = 1;
        blue_pos = 1;
        tlbp_b = 0;
        tlbp_o = 0;

        for ( int j = 0; j < N; ++j ) {
            cin >> R >> P;
            // move robot
            if ( R == 'O' ) {
                delta = orange_pos - P;
                orange_pos = P;
                if ( delta < 0 ) delta = -delta;

                if(total_time < tlbp_o + delta) {
                    total_time = tlbp_o + delta;
                }
                tlbp_o = total_time + 1;
            } else {
                delta = blue_pos - P;
                blue_pos = P;
                if ( delta < 0 ) delta = -delta;

                if(total_time < tlbp_b + delta) {
                    total_time = tlbp_b + delta;
                }
                tlbp_b = total_time + 1;
            }

            // press button
            ++total_time;
        }

        cout << "Case #" << (i + 1) << ": " << total_time << "\n";
    }
}
