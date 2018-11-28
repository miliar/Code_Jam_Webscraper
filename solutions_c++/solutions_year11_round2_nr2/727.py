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
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <ctime>
using namespace std;

const int MAXN = 200+10;
int N ,D;
int A[ MAXN ], B[ MAXN ] ;
int main(int argc, char *argv[]){
	int T ;scanf("%d",&T);
	for( int t = 1 ; t <= T ; t ++ ){
		scanf("%d%d",&N,&D);
		for( int i = 0 ; i < N ; i ++ ){
			scanf("%d%d",&A[i],&B[i]);
		}
		double lo = 0 , hi = 1e20 ,ret;
		int cnt = 0 ;
		while( lo < hi ){
			if( ++cnt > 1000 ) break;
			double md = ( lo + hi ) / 2;
			double l = -1e20;
			int ok = 1;
			for( int i = 0 ; i < N ; i++ ){
				double ll = max( A[ i ] - md , l );
				double rr = A[i] + md ;
				if( rr - ll < (B[i]-1) * D ) { ok = 0 ; break;}
				l = ll + B[i]*D;
			}
			if( ok ){
				ret = md ;
				hi = md ;
			}else lo = md ;
		}
		printf("Case #%d: %.10lf\n",t,ret);
	}
	return 0;
}
