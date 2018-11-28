#include <stdio.h>
#include <stdint.h>
#include <math.h>
#include <vector>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

const int32_t N=201;
const double eps=1e-9;

int32_t C,D;
int32_t P[N];
int32_t V[N];

double pos[1000001];

bool ok(double second){
    int32_t pos_cnt=0;
    for(int32_t i=0;i<C;i++){
        for(int32_t j=0;j<V[i];j++){
            if(pos_cnt==0){
                pos[pos_cnt]=P[i]-second;
            }else{
                if(P[i]-second>pos[pos_cnt-1]+D){
                    pos[pos_cnt]=P[i]-second;
                }else if(P[i]+second>pos[pos_cnt-1]+D){
                    pos[pos_cnt]=pos[pos_cnt-1]+D;
                }else return 0;
            }
            pos_cnt++;
        }
    }
    return 1;
}

int32_t main(){
    int32_t cas, ic;
    scanf("%d",&cas);
    for(ic=1;ic<=cas;ic++){
        scanf("%d%d",&C,&D);
        for(int32_t i=0;i<C;i++){
            scanf("%d%d",&P[i],&V[i]);
        }
        double min=0;
        double max=1e13;
        double mid=0;
        while(min<max){
            mid=(min+max)/2;
            if(ok(mid)){
                max=mid-eps;
            }else{
                min=mid+eps;
            }
        }
        printf("Case #%d: %lf\n",ic,mid);
    }
    return 0;
}
