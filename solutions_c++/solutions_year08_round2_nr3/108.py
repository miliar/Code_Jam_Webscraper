#define _CRT_SECURE_NO_WARNINGS
#include <map> 
#include <set> 
#include <queue> 
#include <bitset> 
#include <valarray> 
#include <complex> 
#include <iostream> 
#include <sstream> 
#include <cmath> 
#include <algorithm> 
#include <string> 
#include <cassert> 

using namespace std;

// prewritten code

#define Size(x) (int)(x).size()
#define For(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define Ford(i,a,b) for(int i=(int)(a);i>=(int)(b);--i) 
#define RepV(i,v) for (int i=0;i<Size(v);++i)
#define All(c) (c).begin(),(c).end()
#define Fill(a,b) memset(&a,b,sizeof(a))
#define Min(a,b) ((a)<(b)?(a):(b))
#define Max(a,b) ((a)>(b)?(a):(b))
#define Abs(a) ((a)<0?-(a):(a))
#define VVI vector<vector<int> >
#define VI vector<int>
#define VVS vector<vector<string> >
#define VS vector<string>
#define ForEach(it,a) for (typeof((a).begin()) it=(a).begin(); it!=(a).end(); ++it)
#define DBG(x) cout << #x <<" = "<< x << endl;
#define DBGA(x) {cout << #x <<": "; for (int i=0; i<(int)sizeof(x)/(int)sizeof(x[0]); ++i) cout<<x[i]<<' '; cout<<endl;}
#define DBGV(x) {cout << #x <<": "; for (int i=0; i<(int)Size(x); ++i) cout<<x[i]<<' '; cout<<endl;}

const string problem_name = "3";

int a[10000], res[10000];
int st[10000];

int main(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
	
	int t;
	scanf("%d",&t);
	
	For(z,1,t){
		printf("Case #%d:",z);
		
		int k, n;
		scanf("%d%d",&k,&n);
		
		For(i,1,n) scanf("%d",&a[i]);
		
		Fill(st,0);
		For(i,1,k) st[i]=1;
		VI v;
		For(i,1,k) v.push_back(i);
		
		int cnt=0, pos=0;
		while (Size(v)) {
			++cnt;
			if (pos>=Size(v))pos=0;
			if (st[cnt]) {
				res[v[pos]] = cnt;
				v.erase(v.begin()+pos);
				st[cnt]=0;
				cnt=0;
			} else {
				++pos;
			}
			
		}
		
		For(i,1,n) printf(" %d",res[a[i]]);
		printf("\n");
		fflush(stdout);
	}
	
	return 0;
}
