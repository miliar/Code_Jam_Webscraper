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

FILE* cfin;
FILE* cfout;
int _Init(int argc, char* argv[]){
	if (argc<2){cout<<"Give filename as arg"<<endl; return 1;}
	cfin=fopen(argv[1],"r");
	cfout=fopen((string(argv[1])+".out").c_str(),"w");
	return 0;
}


int main(int argc, char* argv[]){
	if (_Init(argc, argv)) return 1;

	//Start here
	int ncases; fscanf(cfin,"%d",&ncases);
	for (int ncase=1;ncase<=ncases;++ncase){
		int n; i64  A,B,C,D,x0,y0,M; fscanf(cfin,"%d %lld %lld %lld %lld %lld %lld %lld",&n, &A, &B, &C, &D, &x0, &y0, &M);
		i64 x[n],y[n]; x[0]=x0, y[0]=y0; 
		for (int i=1;i<n;++i){
			 x[i]=(A*x[i-1]+B)%M;
			 y[i]=(C*y[i-1]+D)%M;
		}

		set<pair<i64,i64> > Set; 
		for (int i=0;i<n;++i) Set.insert(make_pair(x[i],y[i]));
		//brute
		i64 r=0;
		for (int i=0;i<n;++i) for (int j=0;j<i;++j) for (int k=0;k<j;++k){
			i64 vx=(x[i]+x[j]+x[k])/3,vy=(y[i]+y[j]+y[k])/3;
			if (vx*3==x[i]+x[j]+x[k]&&vy*3==y[i]+y[j]+y[k])	++r;
		}
		fprintf(cfout,"Case #%d: %lld\n",ncase,r);
	}
 	return 0;
}

