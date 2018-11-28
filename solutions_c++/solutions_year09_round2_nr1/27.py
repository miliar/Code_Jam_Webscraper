#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <cmath>
#include <algorithm>
#include <sstream>
using namespace std;
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define FORD(i,a,b) for (int i=(a); i>=(b); --i)
#define FORE(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n";
#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset(x,0,sizeof x)
#define xx first
#define yy second
typedef long long int lli;
typedef pair<int, int> P;
typedef vector<int> vi;

template <class Ty, class Tx>
Ty cast(const Tx &x) {
	 Ty y; stringstream ss(""); ss<<x; ss.seekg(0); ss>>y; return y;
}


int T,n,it,m;
string tree,line,ani,s;

struct S{
	double waga;
	S *l,*r;
	string cecha;
	S(double waga):waga(waga){l=r=0;}
};

vector<string> v;

S* read(){
//	cout << "read " << v[it] << endl;
	it++; //"("
	S* res=new S(cast<double>(v[it++]));
	if(v[it] == ")") {it++; return res;}
	res->cecha=v[it++];
	res->l=read();
	res->r=read();
	it++;
	return res;
}

int main(){
	cin >> T;
	FOR(cas,1,T){
		//tree
		cin >> n;
		getline(cin,line);
		tree="";
		REP(i,n){
			getline(cin,line);
			tree+=" "+line;
		}
	//	cout << "~" << tree << "~" << endl;
		stringstream ss(tree);
		v.clear();
		while(ss >> line){
			if(line.size() == 0) continue;
			if(line[0] == '('){v.PB("("); line=line.substr(1);}
			if(line.size() == 0) continue;
			if(line.size()>=2 && line[line.size()-1] == ')'){
				v.PB(line.substr(0,line.size()-1));
				v.PB(")");
			}else
				v.PB(line);
		}
//		FORE(i,v) cout << "!"<<*i<<"!" << " "; cout << endl;
		//root
		it=0;
		S* root=read();
		if(it != v.size()) cout << "error" << endl;
	//	cout << it << " " << v.size()-1 << endl;
		//odp
		cout << "Case #" << cas << ":" << endl;
		cin >> n;
		REP(i,n){
			cin >> ani >> m;
			set<string> fea;
			REP(j,m){cin >> s; fea.insert(s);}
//			debugv(fea);
			S* ak=root;
			double res=1.0;
			while(ak->l != 0){
				res*=ak->waga;
				ak=fea.count(ak->cecha) ? ak->l : ak->r;
			}
			res*=ak->waga;
			cout << res << endl;
		}
	}
	return 0;
}
