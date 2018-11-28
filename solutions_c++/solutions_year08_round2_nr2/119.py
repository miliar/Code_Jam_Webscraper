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

const string problem_name = "2";

int v[10000];

VI f[10000];

int getp(int u){
	if (v[u] != u) v[u]=getp(v[u]);
	return v[u];
}

void merge(int u, int t){
	getp(u);
	getp(t);
	if (rand()%2) v[v[u]] = v[t];
	else v[v[t]] = v[u];
}

int main(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
	
	int t;
	scanf("%d",&t);
	
	For(z,1,t){
		printf("Case #%d: ",z);
		
		int a, b, p;
		scanf("%d%d%d",&a,&b,&p);
		
		For(i,a,b) v[i] = i;
		
		For(i,a,b) {
			f[i].clear();
			
			int k=i;
			
			for (int j=2; j*j<=k; ++j) if (k%j==0){
				f[i].push_back(j);
				while (k%j==0) k/=j;
			}
			
			if (k>1) f[i].push_back(k);
			sort(All(f[i]));
		}
		
		For(i,a,b) For(j,a,b) if (getp(i)!=getp(j)) {
			
			bool ok=false;
			RepV(ii,f[i])RepV(jj,f[j]) if (f[i][ii]==f[j][jj] && f[i][ii]>=p) {ok=true; goto y;}
				
			y:
			
			if (ok) {
				merge(i,j);
			}
			
		}
		
		map<int,int> h;
		For(i,a,b) h[v[i]]=1;
		printf("%d\n",Size(h));
	}
	
	return 0;
}
