#include <iostream>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>
#include <utility>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cstring>
#include <cassert>

using namespace std;
using namespace rel_ops;

//#define all(n) n.begin(), n.end()
#define sz size()
//#define forn(i, n) for( int ___n=(n), i = 0 ; i < ___n ; i++ )
//#define fordn()
//#define forsn(i, s, n) for(int i = (s); i < (n); i++)
//#define forall(i, n) for( typeof( (n).begin() ) i = (n).begin(); i != (n).end(); ++i) 
#define DEBUG(x) cout << __LINE__ << " => " << #x << " : " << x << flush; cin.get()
#define entre(a,x,b) ( ((a)<=(x)) && ((x)<(b)) )

#define forn(i,n) for(int ___n=n, i=0;i<___n;++i)
#define fordn(i,n) for(int i=(n)-1;i>=0;--i)
#define forsn(i,s,n) for(int ___n=n, i=s;i<___n;++i)
#define fordsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define forall(it,X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define fordall(it,X) for(typeof((X).rbegin()) it = (X).rbegin(); it != (X).rend(); ++it)
#define all(X) (X).begin(), (X).end()
#define esta(e, c) (c.find(e) != c.end())
#define DBG(a) cerr << __LINE__ << " :: " << #a << " = " << a << endl;

template<class T> string itos(const T&x) { ostringstream o; o<<x; return o.str(); }


struct punto{
	int x,y;
	punto():x(0),y(0){}
	punto(int y,int x):x(x),y(y){}
	punto operator+(punto& p){ return punto(x+p.x,y+p.y);}
	punto operator-(){ return punto(-x,-y); }
	punto operator-(punto& p){ return punto(x-p.x,y-p.y); }
	bool operator<(const punto& p)const{ return (y==p.y)?x<p.x:y<p.y; }
	bool operator==(const punto& p)const{ return y==p.y&&x==p.x; }
};

template <class T> ostream& operator<<(ostream& o, vector<T>& v){
	o << endl << '[';
	forall(i,v) o << (*i) << ',';
	o << ']' ;
	return o;
}

template <class U, class V> ostream& operator<<(ostream& o, pair<U,V>& p){
	o << '(' << p.first << ',' << p.second << ')';
	return o;
}

ostream& operator<<(ostream& o, punto& p){
	o << '(' << p.y << ',' << p.x << ')';
	return o;
}

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<VPII> VVPII;
typedef pair<int, string> PIS;
typedef pair<string, int> PSI;
typedef pair<string, string> PSS;

const int inf = 1234567890;

const int mx[]={-1,0,1,0};
const int my[]={0,-1,0,1};



int main(){
	ofstream sal("sol.txt");
	int nc;
	cin >> nc;
	string s;
	getline(cin,s);
	forn(l,nc){

		VI digits;
		int aux=getchar();
		do{
			digits.push_back(aux-'0');
			aux=getchar();
		}while(aux!=EOF && aux!='\n');
//		DBG(digits);
		if(!next_permutation(all(digits))){
			sort(all(digits));
			int i=-1;
			while(!digits[++i]);
			swap(digits[0],digits[i]);
			digits.insert(digits.begin()+1,0);
		}
		
		sal << "Case #" << l+1 << ": " ;
		forall(i,digits) sal <<char( (*i)+'0');
		sal <<endl;
	}
	return 0;
}