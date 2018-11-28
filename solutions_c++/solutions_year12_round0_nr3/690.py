#include <iostream>
#include <cstdio>
#include <cstring>

#define MP 9999991
#define P 19993LL

typedef long long i64;

using namespace std;

char buff[1010];

int a, b;

struct Hash {
    struct Node {
        int a, b;
        Node *next;
    } v[MP], *head[MP];

    int tot;

    void clear() {
        memset(head, 0, sizeof(head));
        tot = 0;
    }

    void insert(int a, int b) {
        i64 key = ((i64)a * P + b) % MP;
        Node *p;
        for (p = head[key]; p; p = p->next) {
            if (a == p->a && b == p->b) return;
        }
        v[tot].a = a; v[tot].b = b; v[tot].next = head[key];
        head[key] = v + tot++;
    }

    bool find(int a, int b) {
        i64 key = ((i64)a * P + b) % MP;
        Node *p;
        for (p = head[key]; p; p = p->next) {
            if (a == p->a && b == p->b) return true;
        }
        return false;
    }

} h;

void rev(char *l, char *r) {
    if (l >= r) return;
    swap(*l, *r);
    rev(l + 1, r - 1);
}

int cal(int n) {
    int ret = 0, i, l, x;

    sprintf(buff, "%d", n);
    if ((l = strlen(buff)) <= 1) return 0;
    for (i = 0; i < l - 1; ++i) {
        rev(buff, buff + l - 2);
        rev(buff, buff + l - 1);
        sscanf(buff, "%d", &x);
        if (buff[0] != '0' && x > n && x <= b) {
            if (!h.find(n, x)) {
                ++ret; h.insert(n, x);
            }
        }
    }

    return ret;
}

int main() {
    int t, ct = 0, i, ans;

    //freopen("C-large.in", "r", stdin);
    //freopen("C-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%d %d", &a, &b);
        ans = 0; h.clear();
        for (i = a; i <= b; ++i) ans += cal(i);
        printf("Case #%d: %d\n", ++ct, ans);
    }

    return 0;
}
