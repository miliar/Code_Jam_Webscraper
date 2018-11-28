
//{{{
#define DEF
#ifdef DEF
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <stack>
#include <vector>
#include <list>
#include <map>
#include <cctype>
#include <queue>
#include <cstring>
#include <cmath>
#include <set>
#include <deque>


//-----------------------------------------------------


using namespace std;
typedef unsigned int uint;
typedef long long int llint;
typedef unsigned long long int ullint;

typedef pair<int,int> Pii;
typedef pair<llint,llint> Pll;

#define mrepp(i,n,x)  for(int i = n-1; i >= x; i--)
#define mrep(i,n) mrepp(i,n,0)
#define repp(i,x,n)  for(int i = x; i < n; i++)
#define rep(i,n) repp(i,0,n)
#define pb        push_back
#define all(vec)  (vec).begin(),(vec).end()
#define each(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
//#define reach(i,c) for(__typeof((c).rbegin()) i=(c).rbegin();i!=(c).rend();i++)
#define fst         first
#define scd         second

#define sz(v)     ((llint)(v).size())
//#define bit(n)    (1ll<<(li)(n))
//#define mkP        make_pair

//-----------------------------------------------------
#endif
//}}}

char tb[5][5];
int T;
#define mT 0x00
#define mX 0x01
#define mO 0x02
#define mB 0x04

int main(){
	cin >> T;
	rep(t,T){
		printf("Case #%d: ",t+1);
		bool not_comp = false;
		rep(y,4) rep(x,4){
			char a; cin >> a;
			switch(a){
				case 'T': tb[y][x] = mT; break;
				case 'O': tb[y][x] = mO; break;
				case 'X': tb[y][x] = mX; break;
				case '.': tb[y][x] = mB; not_comp = true; break;
			}
		}
		
		char m = 0;
		rep(y,4){
			m = 0;
			rep(x,4) m |= tb[y][x];
			if( m == mX ) goto won;
			if( m == mO ) goto won;
		}
		

		rep(x,4){
			m = 0;
			rep(y,4) m |= tb[y][x];
			if( m == mX ) goto won;
			if( m == mO ) goto won;
		}
		m = 0;
		rep(x,4) m |= tb[x][x];
		if( m == mX ) goto won;
		if( m == mO ) goto won;
		
		m = 0;
		rep(x,4) m |= tb[x][3-x];
		if( m == mX ) goto won;
		if( m == mO ) goto won;
		
		cout << (not_comp?"Game has not completed":"Draw") << endl;
		continue;
		
won:
		cout << (m == mX?"X won":"O won") << endl;
		
		
	}
	return 0;
}
