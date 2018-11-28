#include <cstdio>
#include <algorithm>
using namespace std;

#define REP(I, N) for(int I=0; I < (N); ++I)

typedef long long int LL;
typedef pair< int, LL> PIL;
int R, N, K, T;
const int MAXN = 1009;
int g[MAXN];
int s[MAXN];
LL c[MAXN];
bool v[MAXN];
LL cost[MAXN];


PIL next(int p)
{
    int s=p;
    LL sum=0;
    while( sum + g[ (p) ] <= K)
    {
	sum += g[ p++ ];
	p%=N;
	if(p==s) break;
    }
    return PIL(p, sum);
}

LL bf(int p, int M)
{
    LL ret = 0;
    REP(i, M)
    {
	PIL tmp= next(p);
	p = tmp.first;
	ret += tmp.second;
    }
    return ret;
}
LL solve()
{
    LL ret = 0;
     
    scanf("%d%d%d", &R, &K, &N);
    REP(i, N) 
    {
	scanf("%d", g+i);
	v[i]=0;
	c[i]=0;
	s[i]=0;
    }
    
    int p=0;
    int step=0;
    LL cost=0;
    do
    {
	v[p] = 1;
	s[p] = step;
	c[p] = cost;
	
	PIL tmp = next(p);
// 	printf("? %d -> %d\n", p, tmp.first);
	p = tmp.first;
	cost += tmp.second;
	++step;
    } while(!v[p] && step<R);
    
/*    printf("%lld + %lld * ( %d / %d) + %lld = (%d, %d)\n", 
	   c[p], cost-c[p],   ( R - s[p]),  (step - s[p]), 
         bf( p, ( R - s[p])  ),  p,  (step - s[p]) );*/
	  
if(step-s[p] == 0 ) ret = cost;
else
    ret = c[p] + (cost-c[p]) * ( ( R - s[p]) / (step - s[p]))
          + bf( p, ( R - s[p]) % (step - s[p]) );
	  
    return ret;
}

int main()
{
    scanf("%d", &T);
    for(int it=1; it<=T;++it)
    {
	printf("Case #%d: %lld\n", it, solve());
    }
    return 0;
}