#include <iostream>

using namespace std;

bool snap_on(long n, long k) {
    return ((k & ((1 << n) - 1)) == (1 << n) - 1);
}

int main(int argc, char **argv) {
    int cnt, i, j;
    int R, k, N;
    int *queue;
    int pos, init_pos, cur_load;
    int profit;

    cin >> cnt;

    for(i = 1; i <= cnt; i++) {
        cout << "Case #" << i << ": ";

        cin >> R >> k >> N;
        queue = new int[N];
        init_pos = pos = 0;
        profit = 0;

        for(j = 0; j < N; j++)
            cin >> queue[j];

        while(R-- > 0) {
            init_pos = pos;
            cur_load = 0;
            while(queue[pos] <= (k - cur_load)) {
                cur_load += queue[pos++];
                if(pos == N)
                    pos = 0;
                if(pos == init_pos)
                    break;
            }
            profit += cur_load;
        }

        cout << profit << endl;

        delete[] queue;
    }
    
    return 0;
}

