#include <stdio.h>
#include <stdint.h>
#include <vector>
#include <algorithm>
using namespace std;

int32_t X, S, R, T, N;

typedef struct Point{
    int32_t b, e, s;
}Point;

vector<Point> walker;
vector<Point> all;

bool cmp1(const Point& a, const Point& b){
    return a.b<b.e;
}
bool cmp2(const Point& a, const Point& b){
    return a.s<b.s;
}

int32_t main(){
    int32_t cas, ic;
    scanf("%d",&cas);
    for(int32_t ic=1;ic<=cas;ic++){
        scanf("%d%d%d%d%d",&X,&S,&R,&T, &N);
        walker.clear();
        for(int32_t i=0;i<N;i++){
            Point p;
            scanf("%d%d%d",&p.b,&p.e,&p.s);
            p.s+=S;
            walker.push_back(p);
        }
        sort(walker.begin(), walker.end(), cmp1);
        /*
        for(int32_t i=0;i<walker.size();i++){
            printf("walker %d b=%d, e=%d, s=%d\n", i, walker[i].b, walker[i].e, walker[i].s);
        }
        */
        all.clear();
        int32_t curb=0;
        for(int32_t i=0;i<walker.size();i++){
            if(curb!=walker[i].b){
                Point pp;
                pp.b=curb;
                pp.e=walker[i].b;
                pp.s=S;
                all.push_back(pp);
                curb=walker[i].b;
            }
            all.push_back(walker[i]);
            curb=walker[i].e;
        }
        if(curb!=X){
            Point pp;
            pp.b=curb;
            pp.e=X;
            pp.s=S;
            all.push_back(pp);
        }
        sort(all.begin(), all.end(), cmp2);
        /*
        for(int32_t i=0;i<all.size();i++){
            printf("all %d b=%d, e=%d, s=%d\n", i, all[i].b, all[i].e, all[i].s);
        }*/
        double left_time = T;
        double delta = R-S;
        //printf("left_time =%lf delta = %lf\n", left_time, delta);
        double ans = 0.0;
        for(int32_t i=0;i<all.size();i++){
            double l = all[i].e-all[i].b;
            if(l<left_time*(delta+all[i].s)){
                left_time-=l/(all[i].s+delta);
                ans+=l/(all[i].s+delta);
            }else if(left_time>=0.0){
                ans+=left_time + (l-left_time*(all[i].s+delta))/all[i].s;
                left_time = -1e-10;
            }else{
                ans+=l/(all[i].s);
            }
            //printf("ans=%lf, left_time=%lf\n", ans, left_time);
        }
        printf("Case #%d: %.12lf\n", ic, ans);
    }
    return 0;
}
