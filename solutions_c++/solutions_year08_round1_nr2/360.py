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

int t,tt,n,m,nn,x,y;
vector <int> a;
VP arr[105];


bool qqq(){
	RepV(i,a){
		if (a[i]==1) a[i]=0;
		else {
			a[i]=1;
			return 1;
		}
	}
	return 0;
}

bool check(){	
	Rep(i,m){
		bool fl=0;
		RepV(j,arr[i]){
			if (a[arr[i][j].first]==arr[i][j].second){
				fl=1;
				break;
			}
		}
		if (!fl) return 0;
	}
	return 1;
}


int main() {
//	freopen("qqq.in","rt",stdin);
//	freopen("qqq.out","wt",stdout);
	freopen("B-small.in","rt",stdin);
	freopen("B-small.out","wt",stdout);

	scanf("%d",&t);
	For(tt,1,t){
		scanf("%d%d",&n,&m);
		a.assign(n,0);
		Rep(i,m){
			scanf("%d",&nn);
			arr[i].resize(0);
			Rep(j,nn){
				int a,b;
				scanf("%d%d",&a,&b);
				arr[i].push_back(make_pair(a-1,b));
			}
		}
		bool fl=0;
		do {
			if (check()) {
				fl=1;
				break;
			}
		} while(qqq());

		
		if (fl) {
			printf("Case #%d:", tt);
			RepV(i,a)
				printf(" %d",a[i]);
			printf("\n");
		}else {
			printf("Case #%d: IMPOSSIBLE\n", tt);
		}




	}

	return 0;
}
