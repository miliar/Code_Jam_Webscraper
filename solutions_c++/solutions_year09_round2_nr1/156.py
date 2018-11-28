#include<iostream>
#include<cstdio>
#include<cmath>
#include<complex>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<sstream>
#include<utility>

using namespace std;
using namespace __gnu_cxx;

typedef long long _ll;
typedef double _db;
typedef unsigned int _ui;
typedef vector<int> _vi;
typedef vector<vector<int> > _vvi;
typedef vector<string> _vs;
typedef istringstream _is;
typedef ostringstream _os;

#define INF (1<<30)
#define INFLL (1LL<<61LL)
#define EPS = (1e-9)
#define PB push_back
#define FI first
#define SE second
#define ALL(v) (v).begin(),(v).end()
#define REP(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FUP(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define FDN(i,a,b) for(int (i)=(a);(i)>=(b);(i)--)
#define FORS(i,a) for(int (i)=0;(i)<(int)(a).size();(i)++)
#define FORE(i,a) for(__typeof((a).begin()) i=(a).begin();i!=(a).end();i++)
#define PRINT(v) for(int (i)=0;(i)<(int)(a).size();(i)++) cerr<<v[i]<<" "; cerr<<endl;

struct Tr{
	double p;
	string s;
	Tr *a, *b;
};

string curr;
int pnt;

void bracket(){
	while(true){
		if(pnt >= curr.size()){ cin >> curr; pnt = 0;}
		while(pnt < curr.size()){
			if(curr[pnt] == '(' || curr[pnt] == ')'){ pnt++; return; }
			pnt++;
		}
	}
}

double numb(){
	string l;
	double res;
	while(true){
		if(pnt >= curr.size()){ cin >> curr; pnt = 0;}
		while(pnt < curr.size()){
			if(curr[pnt] == '0' || curr[pnt] == '1'){
				while(pnt < curr.size() && (curr[pnt] == '.' || (curr[pnt] >= '0' && curr[pnt] <= '9')))
					l.append(1, curr[pnt++]);
				_is strm(l);
				strm >> res;
				return res;
			}
			pnt++;
		}
	}
}

string feat(){
	string l;
	while(true){
		if(pnt >= curr.size()){ cin >> curr; pnt = 0;}
		while(pnt < curr.size()){
			if(curr[pnt] == ')') return "";
			if(curr[pnt] >= 'a' && curr[pnt] <= 'z'){
				while(pnt < curr.size() && (curr[pnt] >= 'a' && curr[pnt] <= 'z'))
					l.append(1, curr[pnt++]);
				return l;
			}
			pnt++;
		}
	}
}

Tr* czytaj(){
	Tr* tr = new Tr;
	tr->a = 0;
	tr->b = 0;
	bracket();
	tr->p = numb();
	tr->s = feat();
	if(tr->s != ""){
		tr->a = czytaj();
		tr->b = czytaj();
	}
	bracket();
	return tr;
}

void run(int cs){
	int L,A,n;
	cin >> L;
	Tr* p = czytaj();
	cin >> A;

	cout << "Case #" << cs << ":\n";
	REP(i,A){
		string nn;
		cin >> nn;
		cin >> n;
		multiset<string> fts;
		REP(j,n){
			cin >> nn;
			fts.insert(nn);
		}
		double res = 1.0;

		Tr* cr = p;
		while(true){
			res *= cr->p;
			if(cr->s == "") break;
			if(fts.find(cr->s) != fts.end())
				cr = cr->a;
			else cr = cr->b;
		}
		cout << fixed << res << endl;
	}
}

int main(){
	ios::sync_with_stdio(0);
	int C;
	cin >> C;
	REP(i,C) run(i+1);
	return 0;
}

