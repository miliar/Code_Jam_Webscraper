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
#include<cassert>
//#include<ext/hash_map>
//#include<ext/hash_set>
using namespace std;
using namespace __gnu_cxx;
 
#define ForEach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
typedef long long int i64;
template<class T,class U> T cast (U x) {T y;ostringstream a;a<<x;istringstream b(a.str());b>>y;return y;}

double c[3];

double eps=1e-9;

double f(double t){
	double x=c[0]*t*t +  c[1]*t + c[2];
	assert(x>-eps);
	x=max(0.,x);
	return sqrt(x);
}
int main(){
	int ncases; cin>>ncases;
	for (int ncase=1;ncase<=ncases;++ncase){
		int n; cin>>n;
		int v[n][6];
		for (int i=0;i<n;++i) for (int j=0;j<6;++j) cin>>v[i][j];
		double w[3][2];
		for (int i=0;i<3;++i){
			for (int j=0;j<2;++j){
				w[i][j]=0;
				for (int k=0;k<n;++k){
					w[i][j]+=v[k][i+3*j];
				}
				w[i][j]/=n;
			}
		}
		c[0]=0; for (int i=0;i<3;++i) c[0]+=w[i][1]*w[i][1];
		c[1]=0; for (int i=0;i<3;++i) c[1]+=w[i][0]*w[i][1]*2;
		c[2]=0; for (int i=0;i<3;++i) c[2]+=w[i][0]*w[i][0];
		double t,d;
		if (fabs(c[0])<eps){
			if (fabs(c[1]<eps)){
				t=0;
			}
			else{
				t=-c[2]/c[1];
				t=max(0.,t);
			}
			d=f(t);
		}
		else{
			t=-c[1]/c[0]/2;
			if (t<0) t=0;
			d=f(t);
		}
		assert(t>=0);
		printf("Case #%d: %.10f %.10f\n",ncase, d, t);
	}
	return 0;
} 
