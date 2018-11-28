#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <vector>

using namespace std;
typedef long long LL;
const int Max = 256;
int P[Max],V[Max];
LL Abs(LL x){return x < 0?-x:x;}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int ct = 1;ct <= T;ct++){
        int C;
        LL D;
        scanf("%d%lld",&C,&D);
        for (int i = 0;i < C;i++){
            scanf("%d%d",&P[i],&V[i]);
            P[i] <<= 1;
        }
        D <<= 1;
        LL s = -1,t = 20000000000000000LL;
        while (s+1 < t){
            LL d = (s+t) >> 1;
            LL preT = -(1LL << 60);
            bool check = true;
            for (int i = 0;i < C;i++){
                LL cs = max(P[i]-d,preT);
                LL ct = cs+(V[i]-1)*D;
                LL dis = max(Abs(cs-P[i]),Abs(ct-P[i]));
                //printf("at %d(%lld) [%lld,%lld] %lld\n",i,preT,cs,ct,dis);
                if (dis > d){
                    check = false;
                    break;
                }
                preT = ct+D;
            }
            //printf("%lld : %d\n",d,check);
            if (check) t = d;
            else s = d;
        }
        printf("Case #%d: %.1f\n",ct,t*0.5);
    }
    fclose(stdout);
	return 0;
}
