#include<iostream>
#include<algorithm>
#include<cassert>
#include<utility>
#include<limits>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<sstream>
#include<cmath>
#include<ctime>
#include<vector>
#include<bitset>
#include<string>
#include<map>
#include<set>
#include<iomanip>
#include<queue>
#include<stack>
#include<numeric>
using namespace std;
typedef long long ll;
#define EPS (1e-8)
#define ALL(x) (x).begin(),(x).end()
#define AS assert
#define clr clear
#define PB push_back
#define SZ(x) ((int)(x).size())
#define MP make_pair
#define X first
#define Y second
#define PII pair<int,int>
#define VI vector<int>
#define VD vector<double>
#define VS vector<string>
#define FORD(i,b,c) for(int (i)=(b);(i)>=c;(i)--)
#define REPD(i,c) FORD(i,c,0)
#define FOR(i,b,c) for(int (i)=(b);(i)<(c);(i)++)
#define REP(i,c) FOR(i,0,c)
#define PQ priority_queue
#define LL(x) ((x)<<1)
#define RR(x) ((x)<<1|1)
#define READ freopen("data.in","r",stdin)
#define see(x) (cerr<<"[Line:"<<__LINE__<<"]: "<<#x<<"="<<x<<'\n')
#ifndef INT_MAX
#define INT_MAX (numeric_limits<int>::max())
#define INT_MIN (numeric_limits<int>::min())
#endif
#define ll_max (numeric_limits<long long>::max())
#define ll_min (numeric_limits<long long>::min())
#define CB __builtin_popcount
//prime 999983 100003 899981 900001 900007
const int dm[8][2]={{0,1},{-1,1},{-1,0},{-1,-1},{0,-1},{1,-1},{1,0},{1,1}};
//const int dm[8][2]={{2,-1},{2,1},{1,2},{-1,2},{-2,1},{-2,-1},{-1,-2},{1,-2}};
//const int dm[4][2]={{0,1},{1,0},{-1,0},{0,-1}};
template<class itype,class otype>void convert(otype&out,const itype&in){istringstream str(in);str>>out;}//slow
int main(){
	int T,cas=0;
	scanf("%d",&T);
	while(T--){
		cas++;
		int n;
		scanf("%d",&n);
		double ret=0;
		for(int i=1;i<=n;i++){
			int val;
			scanf("%d",&val);
			if(val!=i)ret++;
		}
		printf("Case #%d: %.6lf\n",cas,ret);
	}
}
