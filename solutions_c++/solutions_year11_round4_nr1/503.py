#include<iostream> 
#include<cstdio>
#include<queue>
#include<fstream>
using namespace std;

#define MAXN 1010

int N;
double X, S, R, T;

struct way{
    double b, e, w;
};

way n[MAXN];
double d[MAXN];

int cmp(const void *a, const void *b)
{
    way x = *(way*)a;
    way y = *(way*)b;
    if(x.b > y.b) return 1;
    return -1;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("a.out", "w", stdout);
	int i , t , casenum = 1;
    double walkdis;
    double now;
    double ans;
    double rleft;
    scanf("%d" , &t);
    while( t-- ) 
    { 
	    memset(n, 0, sizeof(n));
	    memset(d, 0, sizeof(d));
	 
	    scanf("%lf%lf%lf%lf%d", &X, &S, &R, &T, &N);
	    for( i = 0 ; i < N ; i++ )
		{
	        scanf("%lf%lf%lf", &n[i].b, &n[i].e, &n[i].w);
	    }

	    qsort(n, N, sizeof(way), cmp);
	    walkdis = 0;
	    now = 0;
	    for( i = 0 ; i < N ; i++ )
		{
	        walkdis += n[i].b - now;
	        now = n[i].e;
	        d[(int)n[i].w] += n[i].e - n[i].b;
	    }
	    walkdis += X - now;
	    //cout<<walkdis<<endl;
		d[0] += walkdis;

    	ans = 0;
	    rleft = T;
	    for( i = 0 ; i < MAXN ; i++ )
		{
	        if(d[i] == 0)
				continue;
	        double rrrrr = ((double)i + R);
	        double wwwww = ((double)i + S);
	        if(rleft * rrrrr >= d[i])
			{
	            ans += d[i] / rrrrr;
	            rleft = rleft - d[i] / rrrrr;
	        }
	        else
			{
	            d[i] = d[i] - rleft * rrrrr;
	            ans += rleft + d[i] / wwwww;
	            rleft = 0;
	        }
	    }
	    printf("Case #%d: %.8lf\n", casenum++, ans);
	} 
    return 0;
} 
