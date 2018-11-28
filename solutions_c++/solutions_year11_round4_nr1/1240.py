#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
using namespace std;

struct M {
    int st, ed, w;
}p[2010];

bool cmp(M a, M b) {
    return a.w < b.w;
}

int N;
double x, S, R, t, rem;

int main() {
    //freopen("d:\\in.txt","r",stdin);
    //freopen("d:\\out.txt","w",stdout);
	//freopen("d:\\A-small-attempt0.in","r",stdin);freopen("d:\\A-small-attempt0.out","w",stdout);
	//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	  freopen("d:\\A-large.in","r",stdin);freopen("d:\\A-large.out","w",stdout);
	int cse, i, g = 1;
	double ans, tt, len;
	scanf("%d", &cse);
	while(cse--) {
        scanf("%lf %lf %lf %lf %d", &x, &S, &R, &t, &N);
        rem = t;
        ans = 0.0;
        len = 0.0;
        for(i = 0; i < N; ++i) {
            scanf("%d %d %d", &p[i].st, &p[i].ed, &p[i].w);
            len += p[i].ed - p[i].st;
        }
        sort(p, p + N, cmp);
        len = x - len;
        if(len / R < rem) {
            ans += len / R;
            rem -= len / R;
        }
        else {
            ans += rem + (len - rem * R) / S;
            rem = 0.0;
        }
        for(i = 0; i < N; ++i) {
            tt = 1.0*(p[i].ed - p[i].st) / (1.0 * (p[i].w + R));
            if(rem - tt < 0) {
                tt = rem + 1.0 * (p[i].ed - p[i].st - (p[i].w + R) * rem) / (p[i].w + S);
                ans += tt;
                rem = 0.0;
            }
            else{
                ans += tt;
                rem -= tt;
            }
        } 
        printf("Case #%d: %.7lf\n", g++, ans);
    }
    //system("PAUSE");
    return 0;
}
