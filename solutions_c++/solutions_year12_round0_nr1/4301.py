

/*
 * Author: blackBird
 * Email: saketbharamberocks@gmail.com
 */
#include <cstdio>
#include <sstream>
#include <string>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <cmath>
#include <utility>
#include <climits>

using namespace std ;

typedef long long ll ;
typedef pair<int,int> ii ;

#define FOR(i,a,b) for(int i=(a);i<(b);i++) 
#define FOR0(i,a) for(int i=0;i<(a);i++) 
#define FOR1(i,a) for(int i=1;i<(a);i++)
#define REP(i,a,b,c) for(int i=(a);i<(b);i+=(c)) 
#define TRAVERSE(it,s) for(typeof(s.begin()) it=s.begin();it!=s.end();++it)
#define ENDL putchar(10)
#define PB push_back
#define MP make_pair
#define SZ size

#define FILL(a,x) memset(a,x,sizeof a)
#define ALL(c) (c).begin(),(c).end()
#define PRESENT(c,x) (find(ALL(c),x) != (c).end())

#define ABS(a) ((a)<0?-(a):(a))
#define SQ(x) (x)*(x)
#define INF 0xffffff00
#define ESP 1e-6

#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define MININ(a) *min_element(a.begin(), a.end())
#define MININ_A(a,n) *min_element(a, a+n)
#define MAXIN(a) *max_element(a.begin(), a.end())
#define MAXIN_A(a,n) *max_element(a, a+n)

#define P(x) cout << x 
#define PE(x) cout << x << endl 
#define SI ({int _x; scanf("%d",&_x); _x;})
#define SLL ({long long _x; scanf("%lld",&_x); _x;})
#define SLF ({double _x; scanf("%lld",&_x); _x;})
#define SC getchar()
#define SS(n) scanf("%s",n)

	
map<char, char> M ;
string a1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi" ;
string b1 = "our language is impossible to understand" ;
string a2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" ;
string b2 = "there are twenty six factorial possibilities" ;
string a3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv" ;
string b3 = "so it is okay if you want to just give up" ;
string a4 = "y qee" ;
string b4 = "a zoo" ;

void updateM ( string a, string b ) { 
	FOR0(i, a.length()){ 
		M[ a[i] ] = b[i] ; 
	}
	return ; 
}

void change ( string& a ) { 
	FOR0(i, a.length()){
		a[i] = M [ a[i] ] ; 
	}
	return ;
}

int main () {
	updateM(a1, b1);
	updateM(a2, b2);
	updateM(a3, b3);
	updateM(a4, b4);
	M['z'] = 'q' ;
	int Q = SI ; getchar() ;
	string s ; 
	FOR0(i, Q) { 
		getline(cin, s);
		change(s) ;
		cout << "Case #" << i+1 << ": " << s << endl ;
	}
	return 0 ;
}
















