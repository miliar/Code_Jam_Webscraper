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
#define SEIVE 1000005
int arr[SEIVE+1]={0};
int primes[1000000],ind=0,factor[SEIVE+1];
void seive()
{
   int i,j;
   REP(i,SEIVE+1)factor[i]=1;
   for(i=2;i<=10000;i++)
   {
     if(!arr[i])for(j=2*i;j<=SEIVE;j+=i){arr[j]=1;factor[j]=i;}
     if(!arr[i])factor[i]=i;
   }
   ind=0;
   FOR(i,2,SEIVE)if(!arr[i])primes[ind++]=i;
   return;
}
#define MAXSET 101050
class DisjointSet{
	public:
	int parent[MAXSET],rank[MAXSET];
	void makeSet(int x){
		parent[x] = x;
		rank[x] = 0;
	}
	int findSet(int x){
		if(parent[x] != x) parent[x] = findSet(parent[x]);
		return parent[x];
	}
	void link(int x,int y){
		if(rank[x] > rank[y]) parent[y] = x;
		else {
			parent[x] = y;
			if(rank[x] == rank[y]) rank[y]++;
		}
		return;
	}
	void doUnion(int a,int b){
		link(findSet(a),findSet(b));
	}
};
int gcd(int a,int b){
	if(!b)return a;
	return gcd(b,a%b);
}
int main(){
	seive();
	int t;
	cin>>t;
	REP(cas,t){
		int A,B,P;
		scanf("%d%d%d",&A,&B,&P);
		DisjointSet obj;
		FOR(i,A,B+1)obj.makeSet(i);
		FOR(i,A,B+1)FOR(j,i+1,B+1){
			if(factor[(gcd(i,j))]>=P){
					obj.doUnion(i,j);
			}
		}
		int xx[1001],ans=0;
		memset(xx,0,sizeof(xx));
		FOR(i,A,B+1){
			int x=obj.findSet(i);
			if(!xx[x]){
				xx[x]=1;
				ans++;
			}
		}
		printf("Case #%d: %d\n",cas+1,ans);
	}
	return 0;
}
