#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define V(a) vector<a>
#define fori(i, n) for(int i=0;i<n;i++)
#define rep(i, a, b) for(int i=a;i<=b;i++)
#define forv(i, a) for(int i=0;i<a.size(); i++)
#define fill(a) memset(a, 0, sizeof(a));
#define fill1(a) memset(a, -1, sizeof(a));
#define LL long long
#define PB push_back
#define SZ(x) (x.size())


vector<string> split( const string& s, const string& delim =" " ) { vector<string> res; string t; for ( int i = 0 ; i != s.size() ; i++ ) { if ( delim.find( s[i] ) != string::npos ) { if ( !t.empty() ) { res.push_back( t ); t = ""; } } else { t += s[i]; }  } if ( !t.empty() ) {  res.push_back(t); } return res; }
vector<int> splitInt( const string& s, const string& delim =" " ) { vector<string> tok = split( s, delim ); vector<int> res; for ( int i = 0 ; i != tok.size(); i++ ) res.push_back( atoi( tok[i].c_str() ) ); return res; }
template<class T> T tok(string s) {	T a; stringstream ss(s); ss>>a; return a; };
template<class T> string str(T a) {	ostringstream ss; ss<<a; return ss.str();};

int ntest, n, sq;
char s[1005];
string engines[103];
map<string, int> a;
int res;

string getname(){
	fgets(s, 1003, stdin);
	char*ch=s+strlen(s)-1;
	while(!(isdigit(*ch)) && !(isalpha(*ch)) && !(*ch==' '))--ch;
	ch++;
	*ch=0;
	return s;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	sscanf(fgets(s, 1003, stdin), "%d", &ntest);
	rep(ncase, 1, ntest) {
		sscanf(fgets(s, 1003, stdin), "%d", &n);
		fori(e, n) engines[e]=getname();
		sscanf(fgets(s, 1003, stdin), "%d", &sq);
		res=0;a.clear();
		int cnt=0;
		fori(e, sq){
			string g=getname();
//			cout<<g<<endl;
			if(a.count(g)>0); else {
				if(cnt==n-1){
					res++;
					a.clear();
					cnt=0;
				}
				a[g]=1;
				cnt++;
			}
		}
		printf("Case #%d: %d\n", ncase, res);
	}

	return 0;
}
