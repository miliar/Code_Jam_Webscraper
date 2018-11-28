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
int t, na, nb;
priority_queue< pair<int , int > > table;
priority_queue< int > qqq[2];
int a,b,aa,bb,res[2];

int main() {
//	freopen("qqq.in","rt",stdin);
//	freopen("qqq.out","wt",stdout);
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
	scanf("%d\n",&n); 
	Rep(tt,n){
		scanf("%d%d%d\n",&t,&na,&nb);
		table = priority_queue< pair<int , int > >();
		qqq[0] = priority_queue< int >();
		qqq[1] = priority_queue< int >();
		Fill(res,0);

		Rep(i,na+nb){
			scanf("%d:%d %d:%d\n",&a,&b,&aa,&bb);
			int t1=a*60+b, t2=aa*60+bb;		
			table.push(make_pair(-t1,i>=na));
			qqq[i<na].push(-t2-t);
		}

		while(!table.empty()){
			int t1=-table.top().first, p=table.top().second;
			table.pop();
			if (qqq[p].empty() || -qqq[p].top()>t1)
				res[p]++;
			else 
				qqq[p].pop();				
		}

		
		printf("Case #%d: %d %d\n",tt+1, res[0], res[1]);

	}

	
	return 0;
}

