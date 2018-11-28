/**********************************************************************
Author: littlekid@whu_Dolphin
Created Time:  Sat 26 Jul 2008 08:59:50 AM CST
Modified Time: Sat 26 Jul 2008 09:13:02 AM CST
File Name: 
Description: 
**********************************************************************/
#include <iostream>
using namespace std;

#define out(x) printf("%s: %lld\n", #x, (long long)(x))
const int maxint=0x7FFFFFFF;
template <class T> void get_max(T& a, const T &b) {b > a? a = b:1;}
template <class T> void get_min(T& a, const T &b) {b < a? a = b:1;}

const int MAXN = 808;///

int n;
int a[MAXN], b[MAXN];
long long ans;///

void get_input()
{
    scanf("%d", &n);
    for (int ix = 1; ix <= n; ++ ix)
    {
        scanf("%d", &a[ix]);
    }
    for (int ix = 1; ix <= n; ++ ix)
    {
        scanf("%d", &b[ix]);
    }
}

void print_ans(int ca)
{
  //  cout << "Case #" << ca << ": " << ans << endl;//
    printf("Case #%d: %lld\n", ca, ans);
}

void solve()
{
    sort(a+1, a+1+n);
    sort(b+1, b+1+n);
    ans = 0;
    long long tmp;
    for (int ix = 1; ix <= n; ++ ix)
    {
        tmp = a[ix]; tmp *= b[n+1-ix];
        ans += tmp;
    }
}

int main() {
    freopen("a.out", "w", stdout);
    int T; scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ ca)
    {
        get_input();
        solve();
        print_ans(ca);
    }
    return 0;
}

