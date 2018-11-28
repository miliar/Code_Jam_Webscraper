#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <memory>
#define sz size()
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define fu(i,n) for(int i=0; i<(n); i++)
#define ALL(a) (a).begin(),(a).end()
#define cl(a,co) memset(a,co,sizeof a)
#define un(a) sort(ALL(a)),a.erase( unique(ALL(a)), a.end() )
typedef long long ll;
//istringstream is(s); is >> a;

using namespace std;

int ileTestow;

double o(int x1, int y1, int x2, int y2){
	return sqrt( (x1-x2)*(x1-x2) + (y1-y2) * (y1-y2) );
}

int main(){

	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		printf("Case #%d: ",q);
		
		int n;
		int x[100], y[100], r[100];
		scanf("%d",&n);

		fu(a,n){
			scanf("%d%d%d",&x[a],&y[a],&r[a]);
		}
		
		if( n == 3 ){
		double r1 = o(x[0],y[0],x[1],y[1]) + r[0] + r[1];
		double res1 = max( (double)r1/2 , (double)r[2] );

		double r2 = o(x[0],y[0],x[2],y[2]) + r[0] + r[2];
		double res2 = max( (double)r2/2 , (double)r[1] );
		
		double r3 = o(x[1],y[1],x[2],y[2]) + r[1] + r[2];
		double res3 = max( (double)r3/2 , (double)r[0] );
		
		printf("%.6f\n",min( min(res1,res2), res3) );
		} else if( n == 1 ){
			printf("%d\n",r[0]);
		} else if( n == 2 ){
			printf("%d\n",max(r[0],r[1]));
		}

	}

	return 0;
}
