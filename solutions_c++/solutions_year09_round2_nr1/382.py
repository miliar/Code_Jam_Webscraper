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

struct nodo{
	long double n;
	bool hasname;
	string name;
	nodo *left,*right;
	nodo():hasname(false),left(NULL),right(NULL){}
};

int c;

void lee(nodo* n){
	while( !isgraph(c=getchar()) );
	ungetc(c,stdin);
	cin >> n->n;
	bool first=true;
aa:
	while( !isgraph(c=getchar()) );
	if(c=='('){
		if(first){
			n->left=new nodo();
			lee(n->left);
			first=false;
		}else{
			n->right=new nodo();
			lee(n->right);
		}
		goto aa;
	}else
	if(c==')')
		return;
	else{
		ungetc(c,stdin);
		n->hasname=true;
		cin >> n->name;
		if(n->name[n->name.size()-1]==')'){
			ungetc(')',stdin);
			n->name.erase(n->name.size()-1);
		}
		goto aa;
	}
}

long double rank(nodo* n, const VS& v){
	if( n->right==NULL){
		if(n->left==NULL)
			return n->n;
		if(!n->hasname)
			return n->n*rank(n->left,v);
		if(binary_search(all(v),n->name))
			return n->n*rank(n->left,v);
		return n->n;
	}
	if(binary_search(all(v),n->name))
		return n->n*rank(n->left,v);
	return n->n*rank(n->right,v);
}

void Print (nodo *n){
	cout << '(' << n->n << ' ';
	if(n->hasname)
		cout << n->name;
	cout << endl;
		if(n->left!=NULL)
			Print(n->left);
		if(n->right!=NULL)
			Print(n->right);
	cout << ')' << endl;
}

int main(){
	ofstream sal("sol.txt");
	int nc;
	cin >> nc;
	forn(l,nc){
		int L;
		cin >> L;
		nodo *head=new nodo();
		
		while( (c=getchar())!='(');
		
		lee(head);
		c=getchar();
//		cout << c << endl;
//		c=getchar();
//		cout << (char)c << endl;
		//		Print(head);
		
		cout << "Case #" << l+1 << ":" << endl;
		
		int cant;
		string name;
		cin >> cant;
		forn(i,cant){
			int cc;
			cin >> name >> cc;
//			DBG(cc);
			VS ani(cc);
			forall(j,ani)
				cin >> (*j);
			sort(all(ani));
			long double r=rank(head,ani);
			cout << fixed << setprecision(7) << r << endl;
		}
		
	}
	return 0;
}