
/* Author :: Yash */
#include <vector>
#include <list>
#include <cassert>
#include <sstream>
#include <map>
#include <set>
#include <climits>
#include <deque>
#include <fstream>
#include <stack>
#include <bitset>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstring>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

template<class A, class B> A cvt(B x) {stringstream s;s<<x;A r;s>>r;return r;}

#define FOR(i,a,b) for(int i= (int )a ; i < (int )b ; ++i) 
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define PP pop()
#define EM empty()
#define INF 1000000000
#define PF push_front
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define V(x) vector< x >
#define Debug false
#define PRINT(x)        cout << #x << " " << x << endl
#define LET(x,a) 	    __typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v)  	IFOR(it,v.begin(),v.end())
#define PRESENT(c,x) 	((c).find(x) != (c).end())
#define SZ(x) 		x.size();
#define CPRESENT(c,x) 	(find(c.begin(),c.end(),x) != (c).end())
#define D(N) 		int N
#define S(N)		scanf("%d",&N)

typedef pair<int,int>  PI;
typedef pair<int,PI>   TRI;
typedef V( int )       VI;
typedef V( PI  )       VII;
typedef V( string )    VS;
typedef long long      LL;


struct tree { 
	
	double w;
	string a;
	tree *f,*s;

	tree() {
		w = 0.0;
		a = "";
		f = s = NULL;
	}
	tree(double t,string y) {
		w = t;
		a = y;
		f = s = NULL;
	}
};

void ScanTree(tree* &t) {


	t = new tree;
	
	double w;
	scanf(" (%lf",&w);
	char c; string a = "";
	while((c = getchar()) == ' ');
        if (c != ')') 	 {

		a += c; c = getchar();
		while(c != '\n') { a += c ; c = getchar(); }
	}
	t->w = w;
	t->a = a;
	
	if ( a != "" ) {
		
		ScanTree(t->f);
		ScanTree(t->s);
		scanf(" %c",&c); assert(c == ')');
	}

}

void PrintTree(tree* &t) {

	if( t != NULL ) {

		cout << t->w << " " << t->a << endl;
		cout << "Left: \n";
		PrintTree(t->f);
		cout << "Right: \n";
		PrintTree(t->s);
	}

}

set < string > features;


double Solve(tree* &t) {

	double ret = 1;
	
	ret *= t->w;
	if(t->f == NULL && t->s == NULL) return ret;
	if(features.count(t->a)) {
		return ret * Solve(t->f);	
	}
	else return ret * Solve(t->s);
}
int main() {

	int kases; 
	S(kases);

	FOR(cases,1,kases+1) {

		int l, n;
		scanf("%d",&l);
		
		tree *t = new tree;
	       	ScanTree(t);
		//PrintTree(t);
		
		S(n); cout << "Case #" << cases << ":\n";
		REP(i,n) {
			int m;
			scanf(" %*s%d",&m);
		
			features.clear();
			REP(i,m) { 
				string a;cin >> a;
				features.insert(a);
			}

			double ans = Solve(t);
			printf("%.10lf\n",ans);
		}

		
	}	
	return 0;
}


