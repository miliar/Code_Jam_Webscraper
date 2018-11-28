#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

struct R {
    int x1,y1,x2,y2;
};

int N,fa[1000];
R r[1000];

int Find(int x) {
    if(fa[x] == x)
        return x;
    return fa[x] = Find(fa[x]);
}

void Union(int x, int y) {
    int fx=Find(x),fy=Find(y);

    fa[fy] = fx;
}

bool Touch(R a, R b) {
    b.x1--;
    b.x2++;
    b.y1--;
    b.y2++;
    if(!(a.x1 > b.x2 || a.x2 < b.x1) && !(a.y1 > b.y2 || a.y2 < b.y1))
        return 1;
    return 0;
}

int main() {
    int T,i,j,xx[1000],yy[1000],ans,cas=1;

    scanf("%d", &T);
    while(T--) {
        scanf("%d", &N);
        for(i=0; i<N; i++)
            scanf("%d%d%d%d", &r[i].x1, &r[i].y1, &r[i].x2, &r[i].y2);
        for(i=0; i<N; i++)
            fa[i] = i;
        for(i=0; i<N; i++)
            for(j=0; j<N; j++)
                if(Touch(r[i], r[j]))
                    Union(i, j);
        memset(xx, 0xff, sizeof(xx));
        memset(yy, 0xff, sizeof(yy));
        //for(i=0; i<N; i++)
          //  printf("[%d %d]\n", i, Find(i));
        for(i=0; i<N; i++) {
            xx[Find(i)] = max(xx[Find(i)], r[i].x2);
            yy[Find(i)] = max(yy[Find(i)], r[i].y2);
        }
        ans = 0;
        for(i=0; i<N; i++)
            ans = max(ans, abs(xx[Find(i)]-r[i].x1)+abs(yy[Find(i)]-r[i].y1)+1);
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}

