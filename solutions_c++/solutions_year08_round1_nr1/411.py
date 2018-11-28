// Tim  

#include <queue> 
#include <map> 

#include <set>
#include <stack> 
#include <list>
#include <numeric>

#include <iostream> 
#include <sstream> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 

using namespace std;
#pragma comment(linker, "/STACK:20000000")

// useful defines
#define sz(x) (int)(x).size()
#define For(i,a,b)  for(int i=(int)(a);i<=(int)(b);++i)
#define Ford(i,a,b) for(int i=(int)(a);i>=(int)(b);--i) 
#define Rep(i,n)  for (int i=0;i<(n);++i)
#define RepV(i,v) for (int i=0;i<sz(v);++i)
#define Fill(a,b) memset(&a,b,sizeof(a))   
#define All(c) (c).begin(),(c).end() 
typedef pair <int,int> PI;
typedef vector <int> VI;
typedef vector <string> VS;
typedef vector <PI> VP;

int tt,n;
vector <long long> a,b;
long long res=0;

int main() {
//	freopen("qqq.in","rt",stdin);
//	freopen("qqq.out","wt",stdout);
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	scanf("%d\n",&tt);
	For(ii,1,tt){
		scanf("%d\n",&n);
		a.assign(n,0);
		b.assign(n,0);
		Rep(i,n)
			scanf("%lld\n",&a[i]);
		Rep(i,n)
			scanf("%lld\n",&b[i]);
		sort(All(a));
		sort(All(b));
		res=0;
		Rep(i,n)
			res+=a[i]*b[n-i-1];

		printf("Case #%d: %lld\n",ii,res);
	}
	



	return 0;
}
