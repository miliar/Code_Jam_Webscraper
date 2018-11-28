#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;

typedef long long LL;
const int N = 11000;
LL num[N];
map<int, bool> sta;
int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++){
        LL n, l , h;
        sta.clear();
        scanf("%lld%lld%lld", &n, &l, &h);
        for(int i = 0; i < n; i ++){
            scanf("%lld", num + i);
            sta[num[i]] = true;
        }
        sort(num, num+n);
        printf("Case #%d: ", cas);
        int ans = -1;
        for(int i = l; i <= h; i ++){
            bool flag = true;
            for(int j = 0; j < n; j ++){
                if(num[j]%i&&i%num[j]){
                    flag = false;
                    break;
                }
            }
            if(flag){
                ans = i;
                break;
            }
        }
        if(ans == -1) puts("NO");
        else printf("%d\n", ans);
    }
    return 0;
}


//#include <cstdio>
//#include <cstdlib>
//#include <cstring>
//#include <algorithm>
//
//using namespace std;
//
//const int N = 100;
//const int M = 100;
//int n, m;
//char g[N][M];
//bool rep(int x, int y)
//{
//    if(x == n - 1 || y == m - 1) return false;
//    if(g[x][y+1] == '#' && g[x+1][y] == '#' && g[x+1][y+1] == '#')
//        return true;
//    return false;
//}
//int main()
//{
//    freopen("in", "r", stdin);
//    freopen("out", "w", stdout);
//    int T;
//    scanf("%d", &T);
//    for(int cas = 1; cas <= T; cas++){
//        scanf("%d%d", &n, &m);
//        for(int i = 0; i < n; i ++){
//            scanf("%s", g+ i);
//        }
//        bool over = false;
//
//        for(int i = 0; i < n && !false; i ++){
//            for(int j = 0; j < m && !false; j ++){
//                if(g[i][j] == '#'){
//                    if(rep(i, j)){
//                        g[i][j] = '/';
//                        g[i][j+1] = '\\';
//                        g[i+1][j] = '\\';
//                        g[i+1][j+1] = '/';
//                    }
//                    else over = true;
//                }
//            }
//        }
//        printf("Case #%d:\n", cas);
//        if(over) puts("Impossible");
//        else{
//            for(int i = 0; i < n; i ++){
//                puts(g[i]);
//            }
//        }
//    }
//    return 0;
//}