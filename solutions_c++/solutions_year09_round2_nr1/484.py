#include <cmath>
#include <cstring>
#include <string>
#include <set>
#include <algorithm>
#include <vector>
#include <iostream>
#include <map>
#include <queue>
using namespace std;
#define maxint 0x7FFFFFFF
#define maxn 110
#define Mlen 90
struct node {
    string st;
    double p;
    int l, r;
} ret[maxn * Mlen];

set<string> data;
int pre[maxn*Mlen];
char st[maxn*Mlen], stp[Mlen];
int num;

void build(char *s, int n);
void solve();
void prework();
int main(){
	//freopen("Al.in", "r", stdin);
   // freopen("Al.out", "w", stdout);
    int Case, t = 0;
    scanf("%d", &Case);
    while (Case--) {
        prework();
        printf("Case #%d:\n", ++t);
        solve();
    }
 //   while (1);
    return 0;
}

void solve(){	
    int n;
    scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
        data.clear();
        int k;
        scanf("%s%d", st, &k);
        for (int j = 0; j < k; ++j) {
            scanf("%s", stp);
            data.insert(string(stp));
        }
        int now = 1;
        double ans = ret[now].p;
        while (ret[now].st[0]) {
            if (data.find(ret[now].st) != data.end()) {
                now = ret[now].l;
            } else {
                now = ret[now].r;
            }
            ans *= ret[now].p;
        }
        printf("%.7lf\n", ans);
    }
}
void build(char *s, int n) {
    int now = 0, next;
    for (int i = 0; i < n; i = next) {
        next = i + 1;
        if (st[i] == ' ') continue;
        if (st[i] == '(') {
            pre[num] = now;
            if (ret[now].l == 0) ret[now].l = num;
            else ret[now].r = num;
            now = num++;
        } else if (st[i] == ')') {
            now = pre[now];
        } else if (isdigit(st[i])) {
            sscanf(s + i, "%lf", &ret[now].p);
            while (st[next] != ')' && st[next] != ' ') ++next;
        } else if (isalpha(st[i])) {
            sscanf(s + i, "%s", stp);
            ret[now].st = string(stp);
            while (st[next] != ' ') ++next;
        }
    }
}
void prework(){
	int l;
	scanf("%d\n", &l);
    st[0] = 0;
    while (l--) {
        gets(stp);
        strcat(st, stp);
        strcat(st, " ");
    }
    num = 1;
    for (int i = 0; i < maxn * Mlen; ++i) {
        ret[i].st = string();
        ret[i].p = ret[i].l = ret[i].r = 0;
    }
    build(st, strlen(st));
}

