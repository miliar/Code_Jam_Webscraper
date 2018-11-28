#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 1005;
const double EPS = 1e-8;
const double INF = 1e10;
const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};

int n, w, l;
int r[MAXN];
struct pnt{
    int r;
    int id;
    int x, y;
    //double x, y;
    bool operator < (const pnt& a)const{
        return r > a.r;
    }
}   p[MAXN];

void init(){
    scanf("%d%d%d", &n, &w, &l);
    for (int i = 0;i < n;i++){
        scanf("%d", &p[i].r);
        p[i].id = i;
    }
    sort(p, p + n);
}

void work(){
    //if (w < l) swap(w, l);
    int cur = 0;
    int lst = -p[cur].r;
    for (int i = cur;i < n;i++){
        p[i].x = lst + p[i].r;
        //printf("%d %d\n", i, p[i].x);
        if (p[i].x > w) break;
        lst = p[i].x + p[i].r;
        p[i].y = 0;
        cur = i;
    }
    cur += 1;
    lst = w + p[cur].r;
    for (int i = cur;i < n;i++){
        p[i].x = lst - p[i].r;
        if (p[i].x < 0){
            p[i].x = w;
        }
        lst = p[i].x - p[i].r;
        p[i].y = 0;
        for (int j = 0;j < i;j++){
            int lft = max(p[i].x - p[i].r, p[j].x - p[j].r);
            int rgt = min(p[i].x + p[i].r, p[j].x + p[j].r);
            if (lft < rgt){
                p[i].y = max(p[i].y, p[j].y + p[j].r + p[i].r);
            }
        }
    }
}

void check(){
    for (int i = 0;i < n;i++)
        for (int j = i + 1;j < n;j++){
            if (p[i].x < 0 || p[i].x > w || p[i].y < 0 || p[i].y > l){
                printf("out of range %d %d %d %d %d\n", p[i].x, p[i].y, w, l, i);
                exit(0);
            }
            if (p[j].x < 0 || p[j].x > w || p[j].y < 0 || p[j].y > l){
                printf("out of range %d %d %d %d %d\n", p[j].x, p[j].y, w, l, j);
                exit(0);
            }
            int l = max(p[i].x - p[i].r, p[j].x - p[j].r);
            int r = min(p[i].x + p[i].r, p[j].x + p[j].r);
            int u = min(p[i].y + p[i].r, p[j].y + p[j].r);
            int d = max(p[i].y - p[i].r, p[j].y - p[j].r);
            if ((l < r && d < u)){
                printf("invalid : %d %d\n", i, j);
                printf("%d %d %d\n", p[i].x, p[i].y, p[i].r);
                printf("%d %d %d\n", p[j].x, p[j].y, p[j].r);
                printf("%d %d %d %d\n", l, r, u, d);
                exit(0);
            }
        }
}

int main(){
#ifdef ILOAHZ
    //freopen("b.in", "r", stdin);
    //freopen("B-small-attempt2.in", "r", stdin);
    //freopen("B-small-attempt2.out", "w", stdout);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
#endif
    int T, t = 0;
    scanf("%d", &T);
    while (T--){
        init();
        work();
        check();
        printf("Case #%d:", ++t);
        for (int i = 0;i < n;i++)
            for (int j = 0;j < n;j++){
                if (p[j].id == i) printf(" %d %d", p[j].x, p[j].y);
            }
        printf("\n");
    }
    return 0;
}
