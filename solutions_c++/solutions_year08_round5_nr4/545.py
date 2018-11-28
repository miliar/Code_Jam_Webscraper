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

const string pr_name="ds";
const int oo=10000, modul=10007;
int T;
int h,w,r,a,b,arr[105][105];
bool mx[105][105];


int main() {
	freopen((pr_name+".in").c_str(),"rt",stdin);
	freopen((pr_name+".out").c_str(),"wt",stdout);
	
	scanf("%d\n",&T);
	For(TT,1,T){
		scanf("%d%d%d\n",&h,&w,&r);
		Fill(arr,0);
		Fill(mx,0);
		Rep(i,r){
			scanf("%d%d\n",&a,&b);
			mx[a-1][b-1]=1;
		}
		arr[0][0]=1;
		For(i,0,h-1) For(j,0,w-1)
		if (!mx[i][j]){
			arr[i+2][j+1]=(arr[i+2][j+1]+arr[i][j])%modul;
			arr[i+1][j+2]=(arr[i+1][j+2]+arr[i][j])%modul;
		}
		

		printf("Case #%d: %d\n",TT,arr[h-1][w-1]);

	}


	return 0;
}


