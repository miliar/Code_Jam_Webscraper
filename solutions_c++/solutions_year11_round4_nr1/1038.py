#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>

using namespace std;
typedef long long LL;
const int MaxW = 1001;
struct box{
    int l,v;
}W[MaxW];
LL R,S;
bool cmp(const box &i,const box &j){
    return i.v < j.v;
}
int main(){
    int T;
    scanf("%d",&T);
    for (int ct = 1;ct <= T;ct++){
        int X,N,x,y;
        double t;
        scanf("%d%lld%lld%lf%d",&X,&S,&R,&t,&N);
        int rX = X;
        for (int i = 0;i < N;i++){
            scanf("%d%d%d",&x,&y,&W[i].v);
            rX -= (W[i].l = y-x);
        }
        W[N].l = rX,W[N].v = 0;
        ++N;
        sort(W,W+N,cmp);
        double Res = 0.0;
        for (int i = 0;i < N;i++){
            double cv = W[i].v+R+0.0;
            double cd = W[i].l / cv;
            //printf("(%d,%d) : %f %f\n",W[i].l,W[i].v,cv,cd);
            if (cd < t){
                t -= cd;
                Res += cd;
            }else{
                cd = t;
                t = 0.0;
                Res += cd;
                Res += (W[i].l-cv*cd) / (W[i].v+S+0.0);
            }
        }
        printf("Case #%d: %.6f\n",ct,Res);
    }
    return 0;
}

