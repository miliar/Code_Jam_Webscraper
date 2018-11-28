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

int stest, n, T, na, nb;
char s[100];

struct  trip
{
	int start, end;
	int kind;
};
trip f[250];
int res[2];

bool fcmp(trip a, trip b){
	return a.start<b.start;
}

int gettime(){
	scanf("%s", s);
//	printf("%s\n", s);
	return ((s[0]-'0')*10+s[1]-'0')*60+(s[3]-'0')*10+s[4]-'0';
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &stest);
	rep(e, 1, stest){
		scanf("%d%d%d", &T, &na, &nb);
		fori(i, na) f[i].start=gettime(),f[i].end=gettime(),f[i].kind=0;
		fori(i, nb) f[na+i].start=gettime(),f[na+i].end=gettime(),f[na+i].kind=1;
		n=na+nb;
//		fori(i, n) printf("%d %d\n", f[i].start, f[i].end);

		sort(f, f+n, fcmp);
//		printf("after sortting\n");
//		fori(i, n) printf("%d %d\n", f[i].start, f[i].end);
		res[0]=res[1]=0;
		fori(i, n)if(f[i].kind<2){
			int cur=i;
			res[f[i].kind]++;
			for(int j=cur+1;j<n;j++)if(f[cur].end+T<=f[j].start && f[cur].kind+f[j].kind==1) {
				f[cur].kind=2;
				cur=j;
			}
			f[cur].kind=2;
		}				 
		printf("Case #%d: %d %d\n", e, res[0], res[1]);
	}
	return 0;
}
