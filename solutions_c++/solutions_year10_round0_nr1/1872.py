#include <algorithm> 
#include <numeric>
#include <cmath> 

#include <string> 
#include <string.h>
#include <vector> 
#include <queue> 
#include <stack> 
#include <set> 
#include <map> 

#include <iostream> 
#include <sstream> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cassert> 

using namespace std;
#pragma comment(linker, "/STACK:20000000")

// useful defines
#define sz(x) (int)(x).size()
#define For(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define Ford(i,a,b) for(int i=(int)(a);i>=(int)(b);--i) 
#define Rep(i,n) for (int i=0;i<(n);++i)
#define RepV(i,v) for (int i=0;i<sz(v);++i)
#define Fill(a,b) memset(&a,b,sizeof(a))   
#define All(a) (a).begin(),(a).end()   
typedef long long LL;
typedef pair <int,int> PI;
typedef pair <double,double> PD;
typedef vector <int> VI;
typedef vector <string> VS;
typedef vector <PI> VP;

int tt;
LL n, k;

int main() {
	freopen("in.in","rt",stdin);
	//freopen("big.out","wt",stdout);


	cin>>tt;

	Rep(i,tt){
		cout<<"Case #"<<i+1<<": ";
		cin>>n>>k;
		if(k%(1ll<<n)==(1ll<<n)-1) cout<<"ON"<<endl;
		else cout<<"OFF"<<endl;
	}




	
	return 0;
}