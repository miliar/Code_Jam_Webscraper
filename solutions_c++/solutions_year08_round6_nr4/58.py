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
typedef pair<int,int>	PI;
int n,m;
VI graph1[101],graph2[101],graph[101];
int dfs(int *arr,int r1,int p1,int p2){
	//matching r to r
	int l2=graph1[r1].size(),l1=graph[arr[r1]].size();
	REP(i,l2){
		int y=graph1[r1][i],x=arr[graph1[r1][i]],valid=0;
		if(y==p1)continue;
		REP(j,l1)if(graph[arr[r1]][j]==x && x!=p2){
			valid=dfs(arr,y,r1,x);
		}
		if(!valid)return 0;
	}
	return 1;
}
int main(){
	int t;
	cin>>t;
	FOR(cas,1,t+1){
		cout<<"Case #"<<cas<<": ";
		REP(i,101){
			graph[i].clear();
			graph1[i].clear();
			graph2[i].clear();
		}
		cin>>n;
		REP(i,n-1){
			int a,b;
			cin>>a>>b;
			a--;b--;
			graph[a].PB(b);
			graph[b].PB(a);
		}
		cin>>m;
		REP(i,m-1){
			int a,b;
			cin>>a>>b;
			a--;b--;
			graph1[a].PB(b);
			graph1[b].PB(a);
		}
		int done=0;
		int arr[100];
		REP(i,n)arr[i]=i;
		do{
			int valid=1;
			REP(i,m)if(graph1[i].size()>graph[arr[i]].size())valid=0;
			if(!valid)continue;
			if(dfs(arr,0,-1,-1)){
				cout<<"YES\n";
				done=1;
				break;
			}
		}while(next_permutation(arr,arr+n));
		if(!done)cout<<"NO\n";
	}
	return 0;
}
