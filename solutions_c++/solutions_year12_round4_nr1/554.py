#include <queue>
#include <cstdio>
#include <cstring>

using namespace std;

const int MAXN = 10005;
const int MAXM = 15;

int n;
int d[MAXN], l[MAXN];
int len[MAXN];
int dl;

bool check(){
    memset(len, -1, sizeof(len));
    len[0] = min(d[0], l[0]);
    int lst = 1;
    for (int i = 0;i < n;i++){
        if (len[i] >= 0){
            if (d[i] + len[i] >= dl) return true;
            for (int j = i + 1;j < n;j++){
                if (d[i] + len[i] >= d[j]){
                    len[j] = max(len[j], min(l[j], d[j] - d[i]));
                    lst = j;
                }
            }
        }
    }
    return false;
//    int cur = 0;
//    //int loc = 0;
//    int len = min(d[cur], l[cur]);
//    int lst = 1;
//    while (true){
//        if (d[cur] + len >= dl) return true;
//        int i = lst;
//        //lst = -1;
//        int jcur = d[cur];
//        int jlen = len;
//        for (;i < n;i++){
//            //printf("@ i %d %d %d\n", i, d[i], d[cur] + len);
//            if (d[i] <= jcur + jlen){
//                if (d[i] + min(l[i], d[i] - jcur) > d[lst] + len){
//                    lst = i;
//                    len = min(l[i], d[i] - jcur);
//                }
//            }
//            //if (d[i] > d[cur] + l[cur]) break;
//            //if (i == n - 1) break;
//        }
//        //printf("%d %d %d\n", lst, d[lst], len);
//        if (lst == -1 || lst == cur) return false;
//        //printf("lst = %d\n", lst);
////        loc = d[cur];
////        loc = max(loc, d[lst] - l[lst]);
//        cur = lst;
//        if (d[cur] + len >= dl) return true;
//        //printf("i = %d %d %d %d\n", i, cur, d[cur] + (d[cur] - loc), loc);
////        if (d[cur] + (d[cur] - loc) >= dl) return true;
//        //lst = i;
//    }
    return false;
}

int main(){
#ifdef ILOAHZ
    //freopen("a.in", "r", stdin);
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);
//    freopen("A-small-attempt1.in", "r", stdin);
//    freopen("A-small-attempt1.out", "w", stdout);
//    freopen("A-small-attempt2.in", "r", stdin);
//    freopen("A-small-attempt2.out", "w", stdout);
    //freopen("A-small-attempt3.in", "r", stdin);
    //freopen("A-small-attempt3.out", "w", stdout);
    //freopen("A-small-attempt6.in", "r", stdin);
    //freopen("A-small-attempt6.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif
    int T, t = 0;
    scanf("%d", &T);
    while (T--){
        scanf("%d", &n);
        for (int i = 0;i < n;i++) scanf("%d%d", &d[i], &l[i]);
        scanf("%d", &dl);
        printf("Case #%d: %s\n", ++t, check() ? "YES" : "NO");
    }
    return 0;
}
