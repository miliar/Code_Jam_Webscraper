/* Author - Anshuman Singh */
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<algorithm>
#include<iterator>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<deque>
#include<stack>
#include<bitset>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iomanip>
#include<string>
#include<cmath>
#include<ctime>
#include<complex>
using namespace std;

#define Debug 0
#define LET(x,a) 	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v)  	IFOR(it,v.begin(),v.end())
#define FOR(i,a,b)  	for(int i=(int)(a) ; i < (int)(b);++i)
#define FORD(i,a,b) 	for(int i=(a);i>=(b);--i)
#define	REP(i,n)    	FOR(i,0,n)
#define SZ		size()
#define PB		push_back
#define PF		push_front
#define PRINT(x)	cout<<#x<<" = "<<x<<endl
#define PRINTI(x,n)	REP(i,n) cout<<(x)[i]<<" ";cout<<endl
#define PRINTIJ(x,m,n)	for(__typeof(m) i=0;i<m;++i,cout<<"\n") REP(j,n) cout<<(x)[i][j]<<" "
#define PRESENT(c,x) 	((c).find(x) != (c).end())
#define CPRESENT(c,x) 	(find(c.begin(),c.end(),x) != (c).end())
#define EPS		1e-9
#define D_EQ(a,b) 	(a>b-EPS && a<b+EPS)
#define D_LT(a,b) 	((a)<((b)-EPS))
#define D_LTEQ(a,b) 	((a)<((b)+EPS))
#define D_GT(a,b) 	((a)>((b)+EPS))
#define D_GTEQ(a,b) 	((a)>((b)-EPS))
#define ABS(a) 		((a)>=0?(a):(-1.0*(a)))
#define ALL(f,x) 	({bool st=true;f if(!(x)) {st=false;break;};st;})
#define EXISTS(f,x) 	({bool st=false;f if(x) {st=true;break;};st;})
#define COUNT(f,x) 	({int cnt=0;f cnt+=(x);cnt;})
#define getint() 	({int e=0;for(gets(q=s);*q;)e=(e<<3)+(e<<1)+*q++-48;e;})
#define putint(a) 	({int tmp=a,tmp2;*(q=s+10)='\0';for(;;){tmp2=tmp/10;*--q=tmp-(tmp2<<3)-(tmp2<<1)+48;tmp=tmp2;if(!tmp)break;}puts(q);})
#define V(x) vector< x >
#define INF 100000000

typedef V(int)		VI;typedef V(VI)	VII;
typedef V(string) 	VS;typedef long long	LL;
typedef pair<int,int> II;
int main(){
	int t;
	cin>>t;
	REP(cas,t){
		LL n,a,b,c,d,x1,y1,M;
		LL cnt[10];
		set<II> S;
		memset(cnt,0,sizeof(cnt));
		scanf("%lld%lld%lld%lld%lld%lld%lld%lld",&n,&a,&b,&c,&d,&x1,&y1,&M);
		LL x=x1,y=y1;
		cnt[(x%3)*3+(y%3)]++;
		S.insert(make_pair(x,y));
		REP(i,n-1){
			x=(a*x+b)%M;
			y=(c*y+d)%M;
			if(S.find(make_pair(x,y))==S.end()){
				cnt[(x%3)*3+(y%3)]++;
			}
			S.insert(make_pair(x,y));
		}
		LL ans=0,tmp;
		REP(i,9)FOR(j,i,9)FOR(k,j,9){
			if((i%3+j%3+k%3)%3==0 && (i/3+j/3+k/3)%3==0){
				tmp=0;
				if(i==j && j==k){
					tmp=(cnt[i]*(cnt[i]-1)*(cnt[i]-2))/6;
				}
				else if(i==j){
					tmp=(cnt[i]*(cnt[i]-1))/2;tmp*=cnt[j];
				}
				else if(j==k){
					tmp=(cnt[j]*(cnt[j]-1))/2;tmp*=cnt[i];
				}
				else {
					tmp=cnt[i]*cnt[j]*cnt[k];
				}
				ans+=tmp;
			}
		}
		printf("Case #%d: %lld\n",cas+1,ans);
	}
	return 0;
}
