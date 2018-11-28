#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
#include<ctime>
#include<cassert>
#include<climits>
using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for( __typeof(b) i=(a); i<=(b); i++)
#define FORD(i,a,b) for(__typeof(a) i=(a); i>=(b); i--) 
#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define SET(t,v) memset((t), (v), sizeof(t))
#define ALL(x) x.begin(), x.end()
#define REV(x) reverse( ALL( x ) )
#define UNIQUE(c) (c).resize( unique( ALL(c) ) - (c).begin() )

#define sz(v) int(v.size())
#define pb push_back
#define VI vector<int>
#define VS vector<string>

typedef long long LL;
typedef long double LD;
typedef pair<int,int> pii;

#define D(x) if(1) cerr << __LINE__ <<" "<< #x " = " << x << endl
#define D2(x,y) if(1) cerr << __LINE__ <<" "<< #x " = " << x <<", " << #y " = " << y << endl

vector < VI > v;

string toStr(int n) {
	string ans = "";
	while(n>0){
		ans += (n%10 + '0');
		n /= 10;
	}
	REV(ans);
	return ans;
}


void precalc(){
	REP(i,1000){
		VI temp;
		if ( i<10 ) v.pb(temp);
		else if ( i>=10 && i<=99 ) {
			string s = toStr(i);
			if ( s[0] == s[1] ) v.pb(temp);
			else {
				string s2;
				s2[0] = s[1]; s2[1] = s[0];
				int a; a = atoi(s2.c_str());
				temp.pb(a);
				v.pb(temp);
			}
		}
		else {
			string s = toStr(i);
			if ( s[0] == s[1] && s[1] == s[2]) v.pb(temp);
			else {
				string s2,s3; s2 = s3 = "";
				s2+=s[1]; s2+=s[2]; s2+=s[0];
				s3+=s[2]; s3+=s[0]; s3+=s[1];
				int a; a = atoi(s2.c_str());
				int b; b = atoi(s3.c_str());
				temp.pb(a); temp.pb(b);	v.pb(temp);
			}
		}
	}
}

int main() {
//	freopen("out.txt","w",stdout);
	int tc; tc = 0;
	int t; cin >> t;
	precalc();
	while ( t-- ){
		int res; res = 0;
		int A,B; cin >> A >> B;	
		FOR(i,A,B) REP(j,sz(v[i])) if ( v[i][j] >= A && v[i][j] <= B && v[i][j] > i ) res++;
		cout << "Case #" << ++tc << ": " << res << endl;
	}
    return 0;
}

