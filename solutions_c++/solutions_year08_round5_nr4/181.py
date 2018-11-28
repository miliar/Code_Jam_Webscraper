#include <iostream>
#include <cmath>
#include <list>
#define sf(x) scanf("%d",&x)
using namespace std;
typedef struct Rock {
    int x,y;
    bool operator<(const Rock& b) const {
        if (x!=b.x) return x<b.x;
        return y<b.y;
    }
};
Rock rocks[10];
int choose[300][300];
int R,H,W;
int count(int x) {
    int tmp = 0;
    while (x) {
        tmp+=x%2;
        x/=2;
    }
    return tmp;
}
int get(int a, int b) {
    //printf("get[%d][%d]\n",a,b);
    // a across, b down
    // total steps = a+b
    // so a+b mult of 3
    if ((a+b)%3!=0) return 0;
    int jumps = (a+b)/3;
    a-=jumps;
    b-=jumps;
    if (a<0 || b<0) return 0;
    //printf("%d\n",choose[a+b][a]);
    return choose[a+b][a];
}
int solve(int bits) {
    //printf("Solve[%d]\n",bits);
    int x=1, y=1;
    int here = 1;
    for (int i=0; i<R; i++) {
        if (bits&(1<<i)) {
            // x,y to rock i
            int tx = rocks[i].x-x;
            int ty = rocks[i].y-y;
            if (tx<=0 || ty<=0) return 0;
            int g = get(tx,ty);
            here = here*g;
            here%=10007;
            x=rocks[i].x;
            y=rocks[i].y;
        }
    }
    int tx = H-x;
    int ty = W-y;
    if (tx<0 || ty<0) return 0;
    here = (here*get(tx,ty))%10007;
    return here;
}
int main() {
    for (int i=0; i<300; i++) {
        choose[i][0]=choose[i][i]=1;
        for (int j=1; j<300; j++) {
            choose[i][j] = (choose[i-1][j]+choose[i-1][j-1])%10007;
        }
    }
    int T; sf(T);
    for (int t=1; t<=T; t++) {
        sf(H);sf(W);sf(R);//printf("R = %d\n",R);
        for (int i=0; i<R; i++)
        {sf(rocks[i].x);sf(rocks[i].y);}
        sort(rocks,rocks+R);
        //printf("here\n");
        int ans = 0;
        for (int i=(1<<R)-1; i>=0; i--) {
            int ct = count(i)%2;
            int s = solve(i);
            if (ct%2==0) ans+=s;
            else ans-=s;
            //printf("%d: %d\n",i,s);
            ans%=10007;
            ans+=10007;
            ans%=10007;
        }
        printf("Case #%d: %d\n",t,ans);
    }
}
