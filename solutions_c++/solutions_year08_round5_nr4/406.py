#include <iostream>

using namespace std;
const int MMOD = 10007;
int _mod[MMOD];
int pass[20];
int H, W, R;
struct{
    int x, y;
} rock[20];
int seq[20];
bool visit[20];
int ext_euclid(int a,int b,int& x,int& y)
{
    int t,d;
    if(b==0) {x=1;y=0;return a;}
    d=ext_euclid(b,a%b,x,y);
    t=x,x=y,y=t-a/b*y;
    return d;
}
int modular_linear_equation(int a,int b,int n)
{
    int d,x,y;
    d=ext_euclid(a,n,x,y);
    if(b%d!=0) return -1;
    else return (x*(b/d)%n+n)%n;
}
int getfac(int t){
    if (t >= MMOD) return 0;
    return _mod[t];
}
int cmn(int a, int b){
    int na = getfac(a);
    int nb = getfac(b);
    int nab = getfac(a + b);
    //cout << na*nb % MMOD << ' ' << nab << endl;
    return modular_linear_equation((na*nb)%MMOD, nab, MMOD);
}
int gen(int x0, int y0, int x1, int y1){
    if (x0 < x1 || y0 < y1) return 0;
    int tp = (x0 + y0 - x1 - y1);
    if (tp % 3 != 0) return 0;
    tp /= 3;
    int a = x0 - x1 - tp;
    int b = y0 - y1 - tp;
    if (a < 0 || b < 0) return 0;
    //cout << a << ' ' << b << endl;
    return cmn(a, b);
}
void dfs(int l, int num){
    if (num == 0) return;
    pass[l] = (pass[l] + num * gen(H, W, rock[seq[l - 1]].x, rock[seq[l - 1]].y) % MMOD) % MMOD;
    if (l == R) return;
    for(int i = 0; i < R; ++ i)
        if (!visit[i]){
            visit[i] = true;
            seq[l] = i;
            dfs(l + 1, num * gen(rock[i].x, rock[i].y, rock[seq[l - 1]].x, rock[seq[l - 1]].y) % MMOD);
            visit[i] = false;
        }
}
int calc(){
    cin >> H >> W >> R;
    for(int i = 0; i < R; ++ i)
        cin >> rock[i].x >> rock[i].y;
    memset(visit, false, sizeof(visit));
    memset(pass, 0, sizeof(pass));
    pass[0] = gen(H, W, 1, 1);
    for(int i = 0; i < R; ++ i){
        visit[i] = true;
        seq[0] = i;
        dfs(1, gen(rock[i].x, rock[i].y, 1, 1));
        visit[i] = false;
    }
    int ret = 0;
    for(int i = 0; i <= R; ++ i)
        if (i % 2 == 0)
            ret = (ret + pass[i]) % MMOD;
        else ret = ((ret - pass[i]) % MMOD + MMOD) % MMOD;
    return ret;
}
void init(){
    _mod[0] = 1;
    for(int i = 1; i < MMOD; ++ i)
        _mod[i] = (_mod[i - 1] * i) % MMOD;
}
int main(){
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w+", stdout);
    init();
    int N;
    scanf("%d", &N);
    for(int nn = 1; nn <= N; ++ nn)
        printf("Case #%d: %d\n", nn, calc());
    return 0;
}

