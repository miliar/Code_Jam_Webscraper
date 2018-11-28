#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#define MAXN 1010
using namespace std;

int N;
double X, S, R, T;
struct way{
    double b, e, w;
};
way n[MAXN];
double d[MAXN];

int CMP(const void *a, const void *b){
    way x = *(way*)a;
    way y = *(way*)b;
    if(x.b > y.b) return 1;
    return -1;
}

int Case = 1;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.txt","w",stdout);
	int TTT;
	scanf("%d",&TTT);
	while(TTT--)
	{
		memset(n, 0, sizeof(n));
        memset(d, 0, sizeof(d));
        scanf("%lf%lf%lf%lf%d", &X, &S, &R, &T, &N);
        for(int i = 0;i < N; i++){
            scanf("%lf%lf%lf", &n[i].b, &n[i].e, &n[i].w);
        }


        qsort(n, N, sizeof(way), CMP);
        double walkdis = 0;
        double now = 0;
        for(int i = 0;i < N; i++){
            walkdis += n[i].b - now;
            now = n[i].e;
            d[(int)n[i].w] += n[i].e - n[i].b;
        }
        walkdis += X - now;
        d[0] += walkdis;

        double ans = 0;
        double rleft = T;
        for(int i = 0;i < MAXN; i++){
            if(d[i] == 0)continue;
            double rspeed = ((double)i + R);
            double wspeed = ((double)i + S);
            if(rleft * rspeed >= d[i]){
                ans += d[i] / rspeed;
                rleft = rleft - d[i] / rspeed;
            }
            else{
                d[i] = d[i] - rleft * rspeed;
                ans += rleft + d[i] / wspeed;
                rleft = 0;
            }
        }
        printf("Case #%d: %.8lf\n", Case++, ans);
	}
        return 0;
}
