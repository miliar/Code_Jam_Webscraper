#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>

#define FOR(i,m,n) for((i)=(m);(i)<(n);(i)++)
#define FORN(i,m,n) for((i)=(n)-1;(i)>=(m);(i)--)
#define _FORIT(it, b, e) for (__typeof(b) it = (b); it != (e); it++)
#define FORIT(x...) _FORIT(x)
#define ALL(v) (v).begin(), (v).end()
#define RALL(v) (v).rbegin(), (v).rend()
#define SI(a) ((a).size())
#define PB push_back
#define MP make_pair
#define CLR(a,v) memset((a),(v),sizeof(a)) 
#define TLE while(1);
#define RTE printf("%d", 1/0);

using namespace std;
typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef vector<VD> VVD;
typedef vector<VS> VVS;
typedef set<int> SI;
typedef set<double> SD;
typedef set<string> SS;
typedef pair<int,int> PII;
typedef signed long long i64; typedef unsigned long long u64;

#define EPS 1E-14
#define INF 0x3F3F3F3F
#define DINF 1E16
#define NULO -1

inline int cmp(double x, double y = 0, double tol = EPS) {
    return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}


int a[1001], b[1001];


int main(){
	int teste,t,r,x,y,n,j,i;
	
	scanf("%d",&teste);	
	for(t=1;t<=teste;t++){
		scanf("%d",&n);
		for(i=0;i<n;i++) scanf("%d %d",&a[i],&b[i]);
		
		r =  0;
		for(i=0;i<n-1;i++) for(j=i+1;j<n;j++){
			if(a[i]<a[j] && b[i]>b[j]) r++;
			else if(a[i]>a[j] && b[i]<b[j]) r++;
		}
		
		printf("Case #%d: %d\n",t,r);
	}
	return 0;
}