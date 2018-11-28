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
#define MOD(a,p) (( (a)%p+p)%p )
template<class T>
void check_max( T&a, T b ){
	if ( a <  b ) a = b;
}
template<class T>
void check_min( T&a, T b ){
	if ( a > b ) a = b;
}

//#define debug
const int MAXP = 10000, MAXK = 12;
int k,maxp,d;
int b[MAXK];
int aa,ap,ab;
bool isp[MAXP];
int main(){
	memset(isp,true,sizeof(isp));
	isp[0] = isp[1] = false;
	REP(i,2,MAXP){
		if ( isp[i] ){
			for( int j= i+i; j < MAXP; j+=i )
				isp[j] = false;
		}
	}
	int T;cin >>T;
	REP(Case,1,T+1){
		cin >> d >> k;
		maxp = 1;while(d--)maxp*=10;
		REP(i,0,k)cin >> b[i];
		int cok = 0,lb;
		bool ok;
		int mv = 1;
		int ans = -1;
		REP(i,0,k)check_max(mv,b[i]);
		for( int p = mv+1; p <= maxp; p++ )if(isp[p]){
			for( int a = 0; a < p; a++ ){
				if ( k == 1 ){
					cok++;
				}else{
					lb = MOD(b[1]-a*b[0],p);
					ok = true;
					REP(i,2,k) if ( lb != MOD(b[i]-a*b[i-1],p) ){
						ok = false;
						break;
					}
					if ( ok ){
						int cans = (a*b[k-1]+lb)%p; 
						if ( cans != ans ){
					//		cout << "a="<<a<<"b="<<lb<<"p="<<p<<"cans="<<cans << endl;
							ans = cans;
							cok++;
						}
					}
				}
				if ( cok > 1 ) break;
			}
			if ( cok > 1 ) break;
		}
		cout << "Case #"<<Case<<": ";
		if ( cok == 1 )
			cout << ans << endl;
		else
			cout << "I don\'t know." << endl;
	}
	return 0;
}
