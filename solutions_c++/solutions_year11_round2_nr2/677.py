#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;
#define I long long
#define inf ((1LL) << 60)

struct M {
    I x;
    I pos;
}p[20010];

bool cmp(M a, M b) {
    return a.x < b.x;
}

int n, nt;
I c;

bool check(I mid) {
    int i;
    p[0].pos = p[0].x - mid;
    p[nt-1].pos = p[nt-1].x + mid;
    for(i = 1; i < nt - 1; ++i) {
        if(p[i].x - p[i - 1].pos > c) p[i].pos = max(p[i].x - mid, p[i - 1].pos + c);
        else if(p[i].x - p[i - 1].pos == c) p[i].pos = p[i].x;
        else {
            p[i].pos = min(p[i - 1].pos + c, p[i].x + mid);
            if(p[i].pos - p[i - 1].pos < c) return false;
        }
    }
    if(p[nt - 1].pos - p[nt - 2].pos < c) return false;
    return true;
}

int main() {
    //freopen("d:\\in.txt","r",stdin);
    //freopen("d:\\out.txt","w",stdout);
	  freopen("d:\\B-small-attempt0.in","r",stdin);freopen("d:\\B-small-attempt0.out","w",stdout);
	//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	//  freopen("d:\\C-large.in","r",stdin);freopen("d:\\C-large.out","w",stdout);
	int cse, i, j, nn, g = 1;
	I pp, l, r;
	scanf("%d", &cse);
	while(cse--) {
        nt = 0;
        scanf("%d %I64d", &n, &c);
        c *= 2;
        for(i = 0; i < n; ++i) {
            scanf("%I64d %d", &pp, &nn);
            for(j = 0; j < nn; ++j) {
                p[nt++].x = 2 * pp;
            }
        }
        sort(p, p + nt, cmp);
        //for(i = 0; i < nt; ++i) printf("p = %I64d\n", p[i].x);
        l = 0, r = inf;
        while(l < r) {
            I mid = (l + r) /2;
            //printf("mid = %I64d\n", mid);
            if(check(mid)) r = mid;
            else
                l = mid + 1;
        }
        if(l & 1) printf("Case #%d: %I64d.5\n", g++, l / 2);
        else
            printf("Case #%d: %I64d.0\n", g++, l / 2);
    }
    //system("PAUSE");
	return 0;
}
