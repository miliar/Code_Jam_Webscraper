
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set> 
#include<queue>
#include<cstring>
#include<stack>
#include<sstream>
#include<complex>
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it) 
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) { cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n"; }
#define fup(i,a,b) for(int i=(a);i<=(b);i++)
#define fdo(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset((x),0,sizeof (x))
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) ((int)a.size())
#define inf 1000000000
#define SQR(a) ((a)*(a))

using namespace std;
typedef long long lli;
typedef double ld;
int ile[10];
string t;

string first() {
	string act = "";
	fup(i, 0, 9) act += string(ile[i], i + '0');
	return act;	
}
string last(){
	string act = "";
	fdo(i, 9, 0) act += string(ile[i], i + '0');
	return act;
}
string w;
void go(string act) {
	//cout << "GO " << act << endl;
	if (siz(act) == siz(t)) {
		w = act;
		return ;
	}

	fup(i, 0, 9) {
		if (act == "" && i == 0) continue;
		if (ile[i] == 0) continue;	
		ile[i]--;
		string las = act + string(1, i + '0') + last();
	//	debug(las);
		if (las > t) {
			go(act + string(1, i + '0'));
			return ;
		}
		ile[i]++;
	}
	cout << "DUPA" << endl;
}

int main(){
	string liczba;
	int cas;
	cin >> cas;
	fup(c, 1, cas) {
		cin >> liczba;
		t = liczba;
		CLR(ile);
		fup(i, 0, siz(liczba) - 1) ile[liczba[i] - '0']++;
		string las = last();
		string wyn;
		//debug(first());
		//debug(last());

		if (t == las) {
			ile[0]++;
			wyn = "";
			fup(i, 1, 9)  if (ile[i]) { ile[i]--; wyn += string(1, i + '0'); break; } 
			string fi = first();
			wyn = wyn + fi;
		} else {
			w = "";
			go("");	
			wyn = w;
		}

		printf("Case #%d: %s\n", c, wyn.c_str());
	}
	return 0;	
}


