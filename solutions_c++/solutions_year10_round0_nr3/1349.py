#include <iostream>
#include <algorithm>
#include <string>
#include <map>
using namespace std;

typedef long long ll;

int group[1024];
int R, k, N;

ll doit() {
    int horder[1024];
    ll gain[1024];

    int head = 0;
    memset(horder, -1, sizeof horder);    
    horder[0] = 0;
    gain[0] = 0;

    for (int proc=1; proc<=R; ++proc) {

        int all = 0, old = head;
        for (int i=head; i<N; ++i) {
            if (all + group[i] > k) {
                head = i;                
                break;
            }
            all += group[i];
        }
        if (head == old) {
            for (int i=0; i<head; ++i) {
                if (all + group[i] > k) {
                    head = i;
                    break;
                }
                all += group[i];
            }
        }

        gain[proc] = gain[proc-1] + all;

        if (horder[head] == -1) {        
            horder[head] = proc;           
        }
        else {
            ll total = gain[proc];
            ll loop = gain[proc] - gain[horder[head]];
            int time = proc - horder[head];
            int remain = R - proc;
            k = remain / time;
            total += k * loop;
            remain %= time;
            total += gain[horder[head]+remain] - gain[horder[head]];

            return total;
        }
    }
    return gain[R];
}

int main() {
	freopen("problem.in", "r", stdin);
	freopen("problem.out", "w", stdout);
	int T;
	scanf("%d", &T);
    
    for (int tid=1; tid<=T; ++tid) {
        scanf("%d %d %d", &R, &k, &N);
        for (int i=0; i<N; ++i) scanf("%d", group+i);
        ll total = doit();
        printf("Case #%d: %lld\n", tid, total);
	}
	return 0;
}
