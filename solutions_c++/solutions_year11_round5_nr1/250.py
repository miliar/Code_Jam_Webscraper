/*
    2011 Round 3 -
    Irregular Cakes
    by Dave Chang
*/
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std ;

    int T;
    int W, L, U, G;
    int BD[100][2], TD[100][2];
    double area[1001], H[1001];

int main() {
    scanf("%d", &T);
    for(int z=1; z<=T; ++z) {
        area[0] = 0.0;
        scanf("%d %d %d %d", &W, &L, &U, &G);
        for(int i=0; i<L; ++i)
        {
            scanf("%d %d", &BD[i][0], &BD[i][1]);
        }
        for(int i=0; i<U; ++i)
        {
            scanf("%d %d", &TD[i][0], &TD[i][1]);
        }
        /* calc all area */
        double all = 0;
        double ptop = TD[0][1], pbot = BD[0][1];
        H[0] = ptop - pbot;
        //printf("%lf %lf\n", ptop, pbot);
        for(int i=1, pt=1, pb=1; i<=W; ++i)
        {
            double ctop = 0.0, cbot = 0.0;
            if(TD[pt][0]==i)
            {
                ctop = TD[pt][1];
                ++pt;
            }
            else if(TD[pt][0]>i)
            {
                ctop = ptop + (TD[pt][1]-ptop)/(TD[pt][0]-i+1);
            }
            if(BD[pb][0]==i)
            {
                cbot = BD[pb][1];
                ++pb;
            }
            else if(BD[pb][0]>i)
            {
                cbot = pbot + (BD[pb][1]-pbot)/(BD[pb][0]-i+1);
            }
            all += (ctop-cbot + ptop-pbot) / 2.0;
            area[i] = all;
            H[i] = ctop - cbot;
            //printf("H%lf\n",H[i]);
            //printf("%lf %lf %lf %lf %lf\n", ctop, cbot, ptop, pbot, all);
            ptop = ctop;
            pbot = cbot;
        }
        //printf("%lf\n", all);
        printf("Case #%d:\n", z);
        double unit = all / G, cur = unit;
        for(int i=0, p=0; i<G-1; ++i, cur += unit)
        {
            while(area[p+1]<=cur)
            {
                ++p;
            }
            //printf("%lf %lf %lf %lf\n", cur, area[p], area[p+1]);
            double port = (cur-area[p]);
            //printf("%lf %lf %lf\n", H[p+1], H[p], port);
            double pppp = (-H[p] + sqrt(H[p]*H[p]+2*port*(H[p+1]-H[p])))/(H[p+1]-H[p]);
            double ansp = p + pppp;
            if(port==0)
            {
                ansp = p;
            }
            printf("%.14lf\n", ansp);
        }
    }
    return 0;
}
