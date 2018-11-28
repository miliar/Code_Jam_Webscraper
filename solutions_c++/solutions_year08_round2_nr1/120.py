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

const string problem_name = "1";

inline bool d(int x1, int y1, int x2, int y2){
	return (x1!=x2 || y1!=y2);
}

int main(){
	freopen((problem_name+".in").c_str(),"rt",stdin);
	freopen((problem_name+".out").c_str(),"wt",stdout);
	
	int t;
	scanf("%d",&t);
	
	For(z,1,t){
		printf("Case #%d: ",z);
		
		long long n, A, B, C, D, x0, y0, m;
		cin >> n >> A >> B>>C>>D>>x0>>y0>>m;
		
		vector<long long> x, y;
		
		long long cat[3][3];
		Fill(cat,0);
		
		x.push_back(x0); y.push_back(y0);
		++cat[x0%3][y0%3];
		
		For(i,1,n-1) {
			long long nx = (A*x0+B)%m;
			long long ny = (C*y0+D)%m;
			x.push_back(nx); y.push_back(ny);
			++cat[nx%3][ny%3];
			x0=nx; y0=ny;
		}
		
		long long res = 0;
		
		For(x1,0,2) For(y1,0,2) For(x2,0,2) For(y2,0,2) For(x3,0,2) For(y3,0,2) {
			
			if ((x1+x2+x3)%3!=0 || (y1+y2+y3)%3!=0) continue;
			
			long long c1 = cat[x1][y1];
			long long c2 = cat[x2][y2];
			long long c3 = cat[x3][y3];
			
			if ( d(x1,y1,x2,y2) && d(x1,y1,x3,y3) && d(x2,y2,x3,y3) ) {
				
				res += c1*c2*c3;
				
			} else if (!d(x1,y1,x2,y2) && !d(x1,y1,x3,y3) && !d(x2,y2,x3,y3)){
				
				if (c1 >= 3) {
					res += c1*(c1-1)*(c1-2);
				}
				
			} else {
				
				if (!d(x1,y1,x2,y2)) {
					
					if (c1 >= 2){
						res += (c1*(c1-1))*c3;
					}
					
				} else if (!d(x1,y1,x3,y3)){
					if (c1 >= 2){
						res += (c1*(c1-1))*c2;
					}
				} else {
					if (c2 >= 2){
						res += (c2*(c2-1))*c1;
					}
				}
				
			}
			
		}
		
		cout << res/6LL << endl;
	}
	
	return 0;
}
