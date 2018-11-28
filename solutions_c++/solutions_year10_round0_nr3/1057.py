#include <iostream>
#include <cstring>

using namespace std;

typedef unsigned long long ull;
typedef unsigned int uint;

const int MAX = 1000;

static uint g[MAX];         // 1 <= N <= 1000
static uint last[MAX];      // last starting idx of gi
struct roll {
    uint    next;       // next starting idx
    ull     cur_sum;    // sum of this batch
};
static roll m[MAX];
static uint T, R, k, N;

void prologue(void) {
#ifdef DEBUG
    cout << "N=" << N << endl;
#endif
    for(int i = 0; i < N; ++i ) {
        ull sum = g[i];
        int j = i+1;
        if(j == N) j = 0; 
        while(j != i) {
            if(sum+g[j] > k)
                break;
            sum += g[j++];
            if(j==N) j = 0;
            if(sum == k)
                break;
        }
        m[i].next = j;
        m[i].cur_sum = sum;
#ifdef DEBUG
        cout << "next=" << j << " cur_sum=" << sum << endl;
#endif
    }
}

ull run() {
    uint r = 0;
    uint idx = 0;
    ull sum = 0;
    bool loop = false;
    ull loop_sum = 0;
    
    while(r < R) {
        sum += m[idx].cur_sum;
        if(loop)
            loop_sum += m[idx].cur_sum;
        uint next_idx = m[idx].next;
        if(last[next_idx] != -1) {
            if(!loop) {
                loop = true;
#ifdef DEBUG
                cout << "r=" << r << endl;
#endif
            }
            else {
                uint loop_iter = r + 1 - last[next_idx];
                uint times = (R-r-1) / loop_iter;
                loop_sum += m[next_idx].cur_sum;
#ifdef DEBUG
                cout << "r=" << r << endl
                    << "loop_sum=" << loop_sum << endl
                    << "loop_iter=" << loop_iter << endl
                    << "times=" << times << endl
                    << "sum=" << sum << endl;
#endif
                if(times > 0) {
                    sum += loop_sum * times;
                    r += loop_iter * times;
                }
                loop = false;
            }
            loop_sum = 0;
            memset(last, -1, sizeof(last));
        }
        last[idx] = r;
        idx = next_idx;
        ++r;
    }
    return sum;
}

int main(int ac,char **av)
{    
    cin >> T;
    
    for(int i=1; i<=T; ++i) {
        ull sum = 0;
        
        memset(m, 0, sizeof(m));
        memset(g, 0, sizeof(g));
        memset(last, -1, sizeof(last));
        
        cin >> R >> k >> N;
        
        for(int j = 0; j < N; ++j)
            cin >> g[j];
        prologue();
        sum = run();
        cout << "Case #" << i << ": " << sum << endl;
    }
    return 0;
}

