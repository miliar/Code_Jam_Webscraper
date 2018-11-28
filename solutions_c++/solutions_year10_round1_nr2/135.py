/* C Libs */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
#include <ctime>
/* IOstream Libs */
#include <iostream>
#include <fstream>
#include <sstream>
/* String Libs */
#include <string>
/* STL Containers */
#include <bitset>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
/* STL Algorithm */
#include <algorithm>
/* Miscellaneous */
#include <complex>
#include <functional>
#include <iterator>
//#include <limits>
#include <numeric>
#include <typeinfo>
#include <utility>
#include <valarray>

using namespace std;

#define REP(i,s,t) for(int _t=t,i=s;i<_t;i++ )
#define REPP(i,s,t) for(int _t=t,i=s;i<=_t;i++)

template<class T>
void check_max( T&a, T b ){
	if ( a <  b ) a = b;
}
template<class T>
void check_min( T&a, T b ){
	if ( a > b ) a = b;
}

//#define debug
//const int V = 10;
const int V = 256;
const int MAXN = 120, infi = 0x2f2f2f2f;
int D,I,M,n,a[MAXN];
int f[MAXN][V];

bool inq[V];

int pq[V*2], st,ed;

#define debug
int main(){
	
	int t;
	scanf("%d",&t);
	REP(Case,1,t+1){
		scanf("%d%d%d%d",&D,&I,&M,&n);
		if ( M > V-1 ) M = V-1;
		REP(i,1,n+1) scanf("%d",a+i);
		
		memset(f,0x2f,sizeof(f));
		memset(f[0],0,sizeof(f[0]));
		

		REP(i,1,n+1){
//				/*
			int xx =12;
			REP(i_,0,i){
				REP(v,0,V){
					int low = max(0,v-M), hi = min(V-1,v+M);
					for( int v_ = low; v_ <= hi; v_++ )
						check_min( f[i][v], f[i_][v_] + D*(i-i_-1) + abs(v-a[i]) );
				}
			}
				//	*/
			/*
			REP(i_,0,i){
				st = ed = 0;
				REP(v,0,M+1){
					while ( st < ed && f[i_][ pq[ed-1] ] >= f[i_][ v ] )
						ed--;
					pq[ed++] = v;
				}
				int lo = -M, hi = M;
				REP(v,0,V){
					check_min( f[i][v], f[i_][ pq[st] ] + D*(i-i_-1) + abs(v-a[i]) );

					hi++;
					if ( hi < V ){
						while ( st < ed && f[i_][ pq[ed-1] ] >= f[i_][hi] )
							ed--;
						pq[ed++] = hi;
					}

					if ( st < ed && pq[st] == lo ) st++;
					lo++;
				}
			}
			*/
			/*
#ifdef debug
			printf("%d\n",i);
			REP(v,0,V) printf( "%4d",v );
			printf("\n");
			REP(v,0,V) printf( "%4d",f[i][v] );
			printf("\n");
#endif
			*/
			queue<int> q;
			memset(inq,false,sizeof(inq));
			REP(v,0,V) if ( f[i][v] != infi ){
				q.push(v); inq[v] = true;
			}
			while ( !q.empty() ){
				int v = q.front(); q.pop(); inq[v] = false;
				REP(nv,0,V)
					if ( abs(nv-v)<=M && f[i][nv] > f[i][v] + I ){
						f[i][nv] = f[i][v] + I;
						if ( !inq[nv] ){
							inq[nv] = true;
							q.push(nv);
						}
					}
			}
			/*
#ifdef debug
			REP(v,0,V) printf( "%4d",f[i][v] );
			printf("\n");
			printf("\n");
#endif	
*/
		}

		int ans = infi;
		REP(v,0,V) check_min( ans, f[n][v] );
		printf("Case #%d: %d\n",Case,ans);
	}
	return 0;
}
