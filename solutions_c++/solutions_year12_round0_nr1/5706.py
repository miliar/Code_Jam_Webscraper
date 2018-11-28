#include<iostream>
#include<iomanip>
#include<algorithm>
#include<sstream>
#include<vector>
#include<queue>
#include<string>
#include<cctype>
#include<math.h>
using namespace std;

#define FOR(i,a,b) for ( int i = (a) ; i <= (b) ; i ++ )
#define FRD(i,a,b) for ( int i = (a) ; i >= (b) ; i -- )
#define FR(i,a) FOR(i,0,a)
#define FZ(i,a) FRD(i,a,0)
#define sz size()
#define pb push_back
#define ALL(v) v.begin(), v.end()
#define SORT(v) sort(ALL(v))
#define REV(v) reverse(ALL(v))
#define FRV(i,v) FR( i , v.sz - 1 )
#define vi vector<int>
#define vf vector<float>
#define vd vector<double>
#define vs vector<string>
#define vc vector<char>
#define vb vector<bool>

#define mp make_pair
#define ii <int,int>
#define id <int,double>
#define ss stringstream
#define MAX_INT ((1<<31)-1)

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const long double eps = 1e-12;

int ni() { int n; cin >> n ; return n; }
string ns() { string s; cin >> s ; return s; }
char nc() { char c; cin >> c ; return c; }
long int nli() { long int n; cin >> n; return n; }
long long nll() { long long n; cin >> n; return n; }
string nline() { string n; do { getline(cin,n); } while(n == ""); return n;}

int gcd ( int a, int b ) { return ( a%b == 0 ? b : gcd(b,a%b) ) ; }

void main(){
	int T;

	T = ni();
	/*

	ejp mysljylc kd kxveddknmc re jsicpdrysi
	our language is impossible to understand
	
	rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
	there are twenty six factorial possibilities


	de kr kd eoya kw aej tysr re ujdr lkgc jv
	so it is okay if you want to just give up

	*/
	char mapping[256] = {0};

	mapping['a'] = 'y';
	mapping['b'] = 'h';
	mapping['c'] = 'e';
	mapping['d'] = 's';
	mapping['e'] = 'o';

	mapping['f'] = 'c';
	mapping['g'] = 'v';
	mapping['h'] = 'x';
	mapping['i'] = 'd';
	mapping['j'] = 'u';

	mapping['k'] = 'i';
	mapping['l'] = 'g';
	mapping['m'] = 'l';
	mapping['n'] = 'b';
	mapping['o'] = 'k';

	mapping['p'] = 'r';
	mapping['q'] = 'z';
	mapping['r'] = 't';
	mapping['s'] = 'n';
	mapping['t'] = 'w';

	mapping['u'] = 'j';
	mapping['v'] = 'p';
	mapping['w'] = 'f';
	mapping['x'] = 'm';
	mapping['y'] = 'a';

	mapping['z'] = 'q';

	mapping[' '] = ' ';
	FOR(tcn,1,T){
		string rs = nline();
		ss res;
		FRV(i,rs){
			res<<mapping[rs[i]];
		}
		cout << "Case #" << tcn << ": "<<res.str()<<endl;
	}
}