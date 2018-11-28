#include <cstdio>

int run() {
    int r, n, k;
    int tt[1000];
    int cc[1000];
    int dd[1000];
    int used[1000];

    scanf("%d %d %d", &r, &k, &n);

    for(int i=0;i<n;i++) {
        scanf("%d", &tt[i]);
    }
    for(int i=0;i<n;i++) {
        cc[i] = 0;
        dd[i] = 0;
        used[i] = 0;
        for(int j=0;j<n;j++) {
            int val = tt[ (i+j)%n ];
            if( val+cc[i] <= k ) {
                cc[i] += val;
                dd[i] += 1;
            } else {
                //printf("%d %d %d %d\n", j, dd[i], cc[i], val);
                break;
            }
        }
    }
    int cycle = 0;
    int cycle_nr = 0;
    int cycle_start = 0;

    int pos = 0;
    while(1) {
        if(used[pos]) {
            cycle_start = pos;
            break;
        }
        cycle_nr += 1;
        cycle += cc[pos];
        used[pos] = 1;
        pos += dd[pos];
        pos %= n;
    }
    //printf(" -- %d %d %d --\n", cycle, cycle_nr, cycle_start);
    pos = 0;
    while(1) {
        if(cycle_start == pos) {
            break;
        }
        cycle_nr -= 1;
        cycle -= cc[pos];
        pos += dd[pos];
        pos %= n;
    }
    //printf(" -- %d %d %d --\n", cycle, cycle_nr, cycle_start);

    pos = 0;
    int res = 0;
    while(1) {
        if(cycle_start == pos) {
            res += cycle * (r/cycle_nr);
            r = r % cycle_nr;
            if(!r)
                break;
        }
        r -= 1;
        res += cc[pos];
        pos += dd[pos];
        pos %= n;
        if(!r)
            break;
    }
    return res;
}

int main() {
    int n;
    scanf("%d", &n);
    for(int i=0;i<n;i++) {
        printf("Case #%d: %d\n", i+1, run());
    }
    return 0;
}
