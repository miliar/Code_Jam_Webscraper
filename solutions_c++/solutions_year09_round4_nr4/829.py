#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cstdlib>
#include<cctype>
#include<climits>
#include<cmath>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<stack>
#include<bitset>
#include<functional>
#include<numeric>
#include<utility>
#include<ctime>
#include<queue>
#include<ext/hash_map>
#include<ext/hash_set>
using namespace std;
using namespace __gnu_cxx;
 
#define ForEach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
typedef long long int i64;
template<class T,class U> T cast (U x) {T y;ostringstream a;a<<x;istringstream b(a.str());b>>y;return y;}
 
const double eps=1e-10;
int main(){
	int ncases; cin>>ncases;
	for (int ncase=1;ncase<=ncases;++ncase){
		int n; cin>>n;
		int x[3],y[3],z[3];
		for (int i=0;i<n;++i) cin>>x[i]>>y[i]>>z[i];
		if (n==1){
			x[1]=x[2]=x[0];
			y[1]=y[2]=y[0];
			z[1]=z[2]=z[0];
		}
		if (n==2){
			x[2]=x[0];
			y[2]=y[0];
			z[2]=z[0];
		}
		double rx=0,ry=1e4;
		double best=ry+1;
		for (int iter=0;iter<1000;++iter){
			double mr=(rx+ry)/2;
			bool ok=0;
			for (int i=0;i<3;++i){
				int j=(1+i)%3, k=(2+i)%3;
				bool t=1;
				t&=mr+eps>=z[i];
				t&=2*mr+eps>=hypot(x[j]-x[k],y[j]-y[k])+z[j]+z[k];
				ok|=t;
			}
			if (ok){
				best=mr; ry=mr;
			}else{
				rx=mr;
			}
		}
		printf("Case #%d: %.10f\n",ncase,best);
		//cout<<"Case #"<<ncase<<": "<<setprecision(10)<<best<<endl;
	}	
	return 0;
}

