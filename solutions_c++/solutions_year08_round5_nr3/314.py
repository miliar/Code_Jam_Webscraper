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


#define ok(i,j) (i>=0 && j>=0 && i< m && j < n)
int poss[100][100],m,n,ans;
char str[100][100];
void move(int curX, int curY, int r){
	if ((m - curX)*n / 2 + r - curY/2 + 2 <= ans){
		return;
	}
	if(curX == m && curY == 0){
		ans = max(ans,r);
		return;
	}
	if(str[curX][curY]  == 'x' || poss[curX][curY] > 0){
		move(curX + (curY == n-1), (curY +1)%n, r);
	}
	else {
		move(curX + (curY == n-1), (curY +1)%n, r);
		if(ok(curX+1,curY+1)){
			poss[curX+1][curY+1]++;
		}
		if(ok(curX,curY+1)){
			poss[curX][curY+1]++;
		}
		if(ok(curX+1,curY-1)){
			poss[curX+1][curY-1]++;
		}
		move(curX + (curY == n-1), (curY +1)%n, r+1);
		if(ok(curX+1,curY+1)){
			poss[curX+1][curY+1]--;
		}
		if(ok(curX,curY+1)){
			poss[curX][curY+1]--;
		}
		if(ok(curX+1,curY-1)){
			poss[curX+1][curY-1]--;
		}
	}
}
int main(){
	int t;cin>>t;
	FOR(cas,1,t+1){
		printf("Case #%d: ",cas);
		memset(poss,0,sizeof(poss));
		cin>>m>>n;
		REP(i,m){
			scanf("%s",str[i]);
		}
		ans = 0;
		move(0,0,0);
		cout<<ans<<endl;
	}
}
