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
typedef long long ll;
const int MAXB = 110000;
const int MAXN = 120;
ll b[MAXB];
int n;
ll l;

const ll infi = 0x7fffffffffffffff;
ll d[MAXB];
bool inq[MAXB];
int main(){
	int T;cin>>T;
	for( int Case = 1; Case <= T; Case++ ){
		cin >> l >> n;
		REP(i,0,n)cin>>b[i];
		REP(i,1,n) if ( b[i] > b[0] ) swap( b[i], b[0] );
		REP(i,0,b[0]) d[i] = infi;
		if ( b[0] == 0 ){
			cout << "Case #"<<Case<<": "<<"IMPOSSIBLE"<<endl;
			continue;
		}
		d[0] = 0;
		queue<int> q;
		q.push(0);
		memset(inq,false,sizeof(inq));
		inq[0] = true;
		while ( !q.empty() ){
			int i = q.front(); q.pop();
			inq[i] = false;
			REP(j,1,n){
				int ni = i+b[j];
				if ( ni< b[0] ){
					if ( d[ni] > d[i] + 1 ){
						d[ni] = d[i]+1;
						q.push(ni);
					}
				}else{
					ni = ni%b[0];
					if ( d[ni] > d[i] ){
						d[ni] = d[i];
						q.push(ni);
					}
				}
			}
		}
		cout << "Case #"<<Case<<": ";
		if ( d[l%b[0]] == infi ){
			cout << "IMPOSSIBLE" << endl;
		}else{
			cout << l/b[0] + d[l%b[0]] << endl;
		}
	}
	return 0;
}
