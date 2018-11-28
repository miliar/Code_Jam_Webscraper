//17:03 2010-05-23 begin lsy
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN=1000;

struct Twire {
    int x1,x2;
};

inline bool operator < (const Twire &a,const Twire &b) {
    return (a.x1<b.x1);
}

/***********treearray***********/
struct treearray {
    static const int ARRAY_SIZE=10000;
    int c[ARRAY_SIZE+1],n;

    void reset(int _n=ARRAY_SIZE) {
        n=_n;
        memset(c,0,sizeof(c));
    }

    int lowbit(int a) {return (a&(a^(a-1)));}

    void ins(int p,int v) {
        int i;
        for (i=p;i<=n;i+=lowbit(i))
            c[i]+=v;
    }

    int get(int p) {
        int i,t=0;
        for (i=p;i;i-=lowbit(i))
            t+=c[i];
        return t;
    }

};
/***********treearray***********/

int n;
Twire w[MAXN+5];
treearray c;

inline void main_init() {
    memset(w,0,sizeof(w));
    c.reset();
}

inline void readin() {
    scanf("%d",&n);
    int i;
    for (i=1;i<=n;i++)
        scanf("%d%d",&w[i].x1,&w[i].x2);
}

inline int calc() {
    sort(w+1,w+n+1);
    int i,ans=0;
    for (i=n;i>=1;i--) {
        ans+=c.get(w[i].x2);
        c.ins(w[i].x2,1);
    }
    return ans;
}

int main() {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T,i;
    scanf("%d",&T);
    for (i=1;i<=T;i++) {
        main_init();
        readin();
        printf("Case #%d: %d\n",i,calc());
    }
    return 0;
}

