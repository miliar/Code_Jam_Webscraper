#include <iostream>
using namespace std;

int main() {
    int num_case; cin >> num_case;

    // repeat case, N = num snapper, K = num snap
    for(int c = 1; c <= num_case; ++c) {
        long N,K; cin >> N; cin >> K;
        long receive_power = 1;
        long on_off = 0;

        // repeat snap
        for(long snap = 0; snap < K; ++snap) {
            // *SNAP*
            // for each snap any snapper which receive power change state
            // receive_power op on_off
            // 1 op 1 -> 0
            // 1 op 0 -> 1
            // 0 op 1 -> 1
            // 0 op 0 -> 0
            on_off = receive_power ^ on_off;
            //cout << "on_off "<<on_off<<endl;


            // first snapper always receive power
            // n_th snapper receives power only if state is on and n-1_th, receives power
            // loop each snapper check if each receive power. Stop once
            // there is a snapper which does not receive power or all snapper has been
            // checked
            receive_power = 1l;
            long snapper = 0;
            bool cur_snapper_recv_power;
            do {
                if(snapper == 0) cur_snapper_recv_power = 1;
                else {
                    long prev_snapper_recv_power = (receive_power >> (snapper-1l) ) & 1l;
                    long prev_snapper_on_off = (on_off >> (snapper-1l)) & 1l;
                    cur_snapper_recv_power = prev_snapper_recv_power && prev_snapper_on_off;
                }
                receive_power = receive_power | (cur_snapper_recv_power << snapper);
                snapper++;
            } while (snapper < N && cur_snapper_recv_power);
            //cout << "receive_power "<<receive_power <<endl;
        }


        // check light
        bool light_on = ((receive_power >> (N-1l)) & 1l) && ((on_off >> (N-1l)) & 1l);

        cout << "Case #" << c << ": ";
        cout << (light_on ? "ON" : "OFF");
        cout << endl;
    }
}
