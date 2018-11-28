#include <iostream>
#include <vector>
using namespace std;
bool SORTIT = false;
typedef struct Person {
    int r, pos, x, y;
    bool operator<(const Person& p) const {
        if (!SORTIT) {
            return r>p.r;
        } else {
            return pos < p.pos;
        }
    }
};
typedef struct Rect {
    int W,L,x,y;
    Rect(int a, int b, int c, int d) {
        W=a;L=b;x=c;y=d;
    }
};
Person pp[1000];
vector<Rect> rects;
vector<int> xposs, yposs;
int main() {
    int T; scanf("%d",&T); for (int t=1; t<=T; t++) {
        int N,W,L; scanf("%d %d %d",&N,&W,&L);
        for (int i=0; i<N; i++) {
            scanf("%d",&pp[i].r);
            pp[i].pos = i;
        }
        SORTIT = false;
        sort(pp,pp+N);
        
        xposs.clear();
        yposs.clear();
        
        for (int i=0; i<N; i++) {

            for (int j=-1; j<(int)(xposs.size()); j++)
            for (int k=-1; k<(int)(yposs.size()); k++) {

                for (int a=-1; a<=1; a+=2)
                for (int b=-1; b<=1; b+=2) {
                    int x = (j==-1 ? 0 : (xposs[j]+a*pp[i].r));
                    int y = (k==-1 ? 0 : (yposs[k]+b*pp[i].r));
                    if (x<0 || y<0 || x>W || y>L) continue;

                    bool bad = false;
                    for (int l=0; l<i; l++) {
                        // can we put person at [a-b]
                        if (abs(x-pp[l].x)<pp[l].r+pp[i].r && abs(y-pp[l].y)<pp[l].r+pp[i].r) {

                            bad = true;
                        }
                    }
                    if (!bad) {
                        pp[i].x = x;
                        pp[i].y = y;
                        xposs.push_back(x-pp[i].r);
                        xposs.push_back(x+pp[i].r);
                        yposs.push_back(y-pp[i].r);
                        yposs.push_back(y+pp[i].r);                                                            
//                        printf("Put at %d,%d\n",x,y);
                        goto done;                    
                    }
                }
    
            }
            assert(false);
            done:;
        }
        
        
        SORTIT = true;
        sort(pp,pp+N);
        printf("Case #%d: ",t);
        for (int i=0; i<N; i++) {
            printf("%d %d ",pp[i].x,pp[i].y);
        }
        
        printf("\n");
    }
}
