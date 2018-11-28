#include<cstdio>
#include<cstdlib>
#include <algorithm>

using namespace std;

const int inf = 0x3ffffff;
int num[1010];
int n;
int ans = -inf;
void dfs(int op, int a, int b, int asum, int bsum)
{
    //printf("%d %d %d\n", cc++, a, b);
    if (op == n) {
        if (a == b && asum && bsum) {
            ans = max(ans, max(asum, bsum));
          //  printf("%d\n", ans);
        }
    } else {
        dfs(op + 1, a^num[op], b, asum + num[op], bsum);
        dfs(op + 1, a, b^num[op], asum, bsum + num[op]);
    }
}

int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        ans = -inf;
        scanf("%d", &n);
        int tmp = 0;
        for (int i = 0; i < n; i++) {
            scanf("%d", num + i);
            tmp ^= num[i];
        }
        printf("Case #%d: ", cas);
        if (tmp) puts("NO");
        else {
            dfs(0, 0, 0, 0, 0);
            if(ans == -inf) puts("NO");
            else printf("%d\n", ans);
        }
    }
    return 0;
}



////#include <cstdlib>
////#include <cstdio>
////#include <algorithm>
////
////using namespace std;
////
////int oq[1000], bq[1111];
////int ocnt = 0, bcnt = 0;
////
////struct Node {
////    char bot[11];
////    int sta;
////
////    void input() {
////        scanf("%s%d", bot, &sta);
////        if (bot[0] == 'O') oq[ocnt++] = sta;
////        else bq[bcnt++] = sta;
////    }
////} input[10000];
////
////void init() {
////    ocnt = 0, bcnt = 0;
////}
////
////void go(int &now, int next) {
////    if (now < next) now++;
////    else if (now > next) now--;
////}
////
////int main() {
////    freopen("in", "r", stdin);
////       freopen("out", "w", stdout);
////    int t;
////    scanf("%d", &t);
////    for (int cas = 1; cas <= t; cas++) {
////        init();
////        int n;
////        scanf("%d", &n);
////        for (int i = 0; i < n; i++) {
////            input[i].input();
////        }
////        int cnt = 0;
////        int now_o = 1, now_b = 1;
////        int next_o = 0, next_b = 0;
////        for (int i = 0; i < n;) {
////            cnt++;
////            bool unlock = true;
////            if (input[i].bot[0] == 'O' && input[i].sta == now_o && unlock) {
////                i++;
////                next_o++;
////              //  printf("%d O press %d\n", cnt, now_o);
////                unlock = false;
////            } else{
////                int tmp = now_o;
////                go(now_o, oq[next_o]);
////            //    printf("time: %d   Orange %d---->%d\n",cnt, tmp, now_o);
////            }
////            if (input[i].bot[0] == 'B' && input[i].sta == now_b && unlock) {
////                i++;
////                next_b++;
////           //     printf("%d B press %d\n", cnt, now_b);
////            } else{
////                int tmp = now_b;
////                go(now_b, bq[next_b]);
////          //      printf("time: %d  Black %d----->%d\n", cnt, tmp, now_b);
////            }
////        }
////        printf("Case #%d: %d\n", cas, cnt);
////    }
////    return 0;
////}
////
//#include<cstdio>
//#include<cstdlib>
//#include<algorithm>
//#include<cstring>
//using namespace std;
//
//char mer[500][500];
//bool clr[500][500];
//char str[1000];
//char out[1000];
//
//bool canclr(int cnt, char c)
//{
//    for(int i = 0; i <= cnt; i ++){
//        if(clr[out[i]][c]) return true;
//    }
//    return false;
//}
//int main()
//{
//    freopen("in", "r", stdin);
//    freopen("out", "w", stdout);
//    int T;
//    scanf("%d", &T);
//    for(int cas = 1; cas <= T; cas++){
//        memset(mer, 0, sizeof(mer));
//        memset(clr, 0, sizeof(clr));
//        int c, d, n;
//        scanf("%d", &c);
//
//        for(int i = 0; i < c; i ++){
//            scanf("%s", str);
//            mer[str[0]][str[1]] = str[2];
//            mer[str[1]][str[0]] = str[2];
//        }
//        scanf("%d", &d);
//        for(int i = 0; i < d; i ++){
//            scanf("%s", str);
//            clr[str[0]][str[1]] = true;
//            clr[str[1]][str[0]] = true;
//        }
//        scanf("%d", &n);
//        scanf("%s", str);
//        int len = strlen(str);
//        int cnt = -1;
//        bool unlock = true;
//        for(int i = 0; i < len; i ++){
//            if(cnt == -1){
//                out[++cnt] = str[i];
//                continue;
//            }
//            if(mer[out[cnt]][str[i]]) unlock = false, out[cnt] = mer[out[cnt]][str[i]];
//            else if(canclr(cnt, str[i])){
//                cnt = -1;
//                unlock = true;
//            }
//            else out[++cnt] = str[i], unlock = true;
//        }
//        printf("Case #%d: [", cas);
//        for(int i = 0; i <= cnt; i ++){
//            if(i != 0) printf(", %c", out[i]);
//            else putchar(out[i]);
//        }
//        printf("]\n");
//    }
//    return 0;
//}