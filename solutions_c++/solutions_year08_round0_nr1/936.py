// Tim  
#include <numeric>
#include <queue> 
#include <map> 

#include <set>
#include <stack> 
#include <list> 

#include <iostream> 
#include <sstream> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 

using namespace std;
#pragma comment(linker, "/STACK:20000000")

#define sz(x) (int)(x).size()
#define For(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define Ford(i,a,b) for(int i=(int)(a);i>=(int)(b);--i) 
#define Rep(i,n) for (int i=0;i<(n);++i)
#define RepV(i,v) for (int i=0;i<sz(v);++i)
#define Fill(a,b) memset(&a,b,sizeof(a))   
#define All(c) (c).begin(),(c).end() 
#define sqr(a) (a)*(a)
typedef pair <int,int> PI;
typedef vector <int> VI;
typedef vector <string> VS;
typedef vector <PI> VP;

int n; 
int s, q;
char  ss[105];
map <string,int> mp;
vector <bool> vis;

int main() {
//	freopen("qqq.in","rt",stdin);
//	freopen("qqq.out","wt",stdout);
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	scanf("%d\n",&n);
	Rep(tt,n){
		scanf("%d\n",&s);
		vis.assign(s,false);
		mp.clear();
		Rep(i,s){
			gets(ss);
			mp[string(ss)]=i;
		}
		scanf("%d\n",&q);
		int cnt=0,res=0;
		Rep(i,q){
			gets(ss);
			int p=mp[string(ss)];
			if (!vis[p]){
				cnt++;
				vis[p]=1;
			}
			if (cnt==s){
				res++;
				cnt=1;
				vis.assign(s,false);
				vis[p]=1;
			}
		}
		printf("Case #%d: %d\n",tt+1,res);

	}

	
	return 0;
}

