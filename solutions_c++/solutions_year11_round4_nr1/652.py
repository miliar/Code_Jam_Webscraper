#include <iostream>
using namespace std;
typedef struct Seg {
    int start,end,speed;
    double val;
    bool operator<(const Seg& s) const {
        return val>s.val;
    }
};
Seg segs[1001];
int main() {
    int T; scanf("%d",&T); for (int tt=1; tt<=T; tt++) {
        int X,S,R,t,N; scanf("%d %d %d %d %d",&X,&S,&R,&t,&N);
        int extra = X;
        for (int i=0; i<N; i++) {
            scanf("%d %d %d",&segs[i].start,&segs[i].end,&segs[i].speed);
            extra -= segs[i].end-segs[i].start;
        }
        segs[N].start = 0;
        segs[N].end = extra;
        segs[N].speed = 0;
        N++;
        for (int i=0; i<N; i++) {
            segs[i].val = 1.*(R-S)/(S+segs[i].speed);
        }
        sort(segs,segs+N);
        double runleft = t;
        double tottime = 0;
        for (int i=0; i<N; i++) {
            int dist = segs[i].end-segs[i].start;
            double runsecs = min(runleft,1.*dist/(R+segs[i].speed));
//            printf("Can run for up to %f secs\n",runsecs);
            double distleft = dist - runsecs*(R+segs[i].speed);
//            printf("DIstleft is %f\n",distleft);
            tottime += runsecs + 1.*distleft/(S+segs[i].speed);
//            printf("So %f + %f\n",runsecs,1.*distleft/(S+segs[i].speed));
//            printf("Time so far %f\n",tottime);
            runleft -= runsecs;
        }
        printf("Case #%d: %.8f\n",tt,tottime);
    }
}
