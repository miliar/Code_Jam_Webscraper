#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <sstream>
#include <fstream>
#include <queue>

using namespace std;

#define forn(i, n) for(int i = 0; i<(int)(n); i++)
#define forsn(i, m, n) for(int i = (int)(m); i<(int)(n); i++)
#define si(x) x.size()
#define mp make_pair
#define pb push_back
#define all(x) x.begin(),x.end()

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef pair<int, ii> iii;
typedef vector<vi> vvi;

typedef long long int tint;

typedef pair<char, char> cc;

map<cc, char> conv;
map<cc, bool> op;

int nc, no, n;
vector<char> res;

void init(){
	conv.clear();
	op.clear();
	res.clear();
}

void check(){
	if(si(res)<2) return ;	
	int s = si(res);
	char c1 = res[s-1], c2 = res[s-2];
	if(c1>c2) swap(c1, c2);
	
//	forn(i, s) cout << res[i]; cout << endl;
	if(conv.find(mp(c1, c2)) != conv.end()){
		res.pop_back(); res.pop_back();
		res.pb(conv[mp(c1, c2)]);
		check(); //return ;	
	}
	s = si(res);
	forn(i, s){
		c1 = res[s-1];
		c2 = res[i];
		if(c1 > c2) swap(c1, c2);
		if(op.find(mp(c1, c2)) != op.end()){ res.clear(); check(); } //return ;}
	}
}

int main(){
	int t; cin >> t;
	forn(tt, t){
		init();			
		cin >> nc;
		forn(i, nc){
			string tmp;
			char c1, c2, c3; cin >> c1 >> c2 >> c3;
			if(c1 > c2) swap(c1, c2);
			conv[mp(c1,c2)] = c3;
		}
		cin >> no;
		forn(i, no){
			char c1, c2; cin >> c1 >> c2;
			if(c1 > c2) swap(c1, c2);
			op[mp(c1, c2)] = true;	
		}
		cin >> n;
		
		forn(i, n){
			char c; cin >> c;	
			res.pb(c);
			check();
		}
		
		cout << "Case #" << tt+1 << ": [";
		forn(i, si(res)-1) cout << res[i] << ", ";
		if(!res.empty()) cout << res[si(res)-1];
		cout << "]" << endl;
	}
			
	return 0;
}
