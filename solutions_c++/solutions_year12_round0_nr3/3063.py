#pragma comment(linker, "/STACK:65777216")
#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <stack>
#include <map>
#include <queue>
#include <string>
#include <memory.h>
#include <iterator>
#define y1 trololoy1
#define y0 trololoy0
#define mem(A,X) memset(A,X,sizeof(A))
#define memo(A) memset(A,0,sizeof(A))
#define forn(I,B) for (int I=1;I<=(B);I++)
#define forg(H,V) for (int H=first[V];h;h=next[H])
#define rep(I,B) for (int I=0;I<(B);I++) 
#define labs(X) (((X)>0)?(X):(-(X)))
#define ropen(X) freopen(X,"r",stdin)
#define wopen(X) freopen(X,"w",stdout)
#define rwopen(X) freopen(X".in","r",stdin);freopen(X".out","w",stdout)
#define pb push_back
#define mp make_pair
#define all(X) (X).begin(),(X).end()
#define sqr(X) ((X)*(X))

using namespace std;

typedef pair <int,int> pii;
typedef double ld;
typedef long long ll;
typedef pair <ll,ll> pll;
typedef vector<int> vi;
const int N=501;
const int M=20001;
const int INF=111111111;
const double eps=1e-9;
const double pi=3.14159265358979;

int t,n,a,b;

inline bool check(int x,int y){
	char value1[11],value2[11];
	memo(value1);memo(value2);
	string val1,val2;
	sprintf(value1,"%d",x);
	sprintf(value2,"%d",y);
	val1=value1;
	int n=val1.length();
	val1+=val1;val2=value2;
	if (val1.length()!=2*val2.length()) return 0;
	rep(i,n){
		bool ok=1;
		rep(j,n) if (val1[i+j]!=val2[j]) ok=0;
		if (ok) return 1;
	}
	return 0;
}    	

void solve(int num){
	printf("Case #%d: ",num);
	int ans=0;
	for (int i=a;i<=b;i++)
		for (int j=a;j<i;j++) ans+=check(i,j);
	printf("%d\n",ans);
}

int main(){
	ropen("input.txt");
	wopen("output.txt");
	scanf("%d\n",&t);
	forn(i,t){
		scanf("%d%d",&a,&b);
		cerr<<i<<" ";
		solve(i);
	}
	return 0;
}