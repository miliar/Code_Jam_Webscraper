
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>
using namespace std;

typedef pair<double,double> pdd;
#define f first
#define s second

int main(){
    int nn;scanf("%d",&nn);
    for(int npr=1;npr<=nn;npr++){
        double len,walk,run,tim;
        int n;scanf("%lf%lf%lf%lf%d",&len,&walk,&run,&tim,&n);
        double sta[n],end[n],speed[n];
        for(int i=0;i<n;i++)scanf("%lf%lf%lf",sta+i,end+i,speed+i);

        double pos=0.0;
        pdd v[2*n+1];
        for(int i=0;i<=2*n;i++){
            double dist;
            if(i==2*n)  dist=len-pos;
            else if(i&1)dist=end[i/2]-pos;
            else        dist=sta[i/2]-pos;
            double orig;
            if(i&1)orig=speed[i/2];
            else   orig=0.0;
            v[i]=pdd(orig,dist);
            pos+=dist;
        }
        sort(v,v+2*n+1);

        double ans=0.0;
        for(int i=0;i<=2*n;i++){
            double orig=v[i].f;
            double dist=v[i].s;

            if(1e-12<dist){
                if(1e-10<tim){
                    //cout<<"dist"<<dist<<" orig+run"<<orig+run<<endl;
                    double run_all=dist/(orig+run);
                    if(run_all<tim){
                        ans+=run_all;
                        tim-=run_all;
                    }else{
                        double extra=(dist-(orig+run)*tim)/(orig+walk);
                        //cout<<"tim"<<tim<<" extra"<<extra<<endl;
                        ans+=tim+extra;
                        tim=0.0;
                    }
                }else{
                    ans+=dist/(orig+walk);
                }
            }
        }

        printf("Case #%d: %.10lf\n", npr,ans);
    }
    return 0;
}
