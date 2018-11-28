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
#define For(i,a,b)  for (int i=int(a); i<=int(b); ++i)
#define Ford(i,a,b) for (int i=int(a); i>=int(b); --i) 
#define Rep(i,n)    for (int i=0; i<int(n); ++i)
#define RepV(i,v)   for (int i=0; i<sz(v); ++i)
#define Fill(a,b) memset(&a,b,sizeof(a))   
#define All(c) (c).begin(),(c).end() 
typedef pair <int,int> PI;
typedef vector <int> VI;
typedef vector <string> VS;
typedef vector <PI> VP;
typedef long long LL;

const string pr_name="Al";
const int oo=10000;
int T,n,s,a,b,m;
int arr[50000];
bool ch[50000];

int go(int p){
	if (p<=m) {
		if (arr[p] ^ s) {
			return min(go(2*p+1),go(2*p));
		}
		else {
			int a=go(2*p+1),b=go(2*p);
			if (ch[p])
				return min(a+b,min(a,b)+1);
			else 
				return a+b;
		}
	}else {
		if (arr[p]==s) return 0;
		else return oo;
	}
}

int main() {
	freopen((pr_name+".in").c_str(),"rt",stdin);
	freopen((pr_name+".out").c_str(),"wt",stdout);
	
	scanf("%d\n",&T);
	For(TT,1,T){
		scanf("%d%d\n",&n,&s);
		Fill(arr,0);
		Fill(ch,0);
		m=(n-1)/2;

		Rep(i,(n-1)/2){
			scanf("%d%d\n",&a,&b);
			arr[i+1]=a;
			ch[i+1]=b;
		}
		Rep(i,(n+1)/2){
			scanf("%d\n",&a);
			arr[i+1+m]=a;
		}
		
		int res=go(1);
		if (res<oo) 
			printf("Case #%d: %d\n",TT,res);
		else 
			printf("Case #%d: IMPOSSIBLE\n",TT,res);
	}


	return 0;
}


