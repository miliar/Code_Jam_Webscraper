#include<iostream>
#include<iomanip>
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

int main(){
	ios::sync_with_stdio(0);
	int N;
	char buf[1000];
	const char* text = "welcome to code jam";
	int dp[1000];
	cin >> N;
	cin.ignore(10, '\n');
	REP(i,N){
		cin.getline(buf, 900);
		string s(buf);
		dp[s.size()] = 0;
		FDN(j,s.size()-1,0)
			if(s[j] == 'm') dp[j] = dp[j+1] + 1;
			else dp[j] = dp[j+1];

		int lst;
		FDN(j,17,0){
			lst = 0;
			FDN(k,s.size()-1,0){
				int tmp = dp[k];
				dp[k] = dp[k+1];
				if(s[k] == text[j])
					dp[k] += lst;
				dp[k] %= 10000;
				lst = tmp;
			}
		}
		cout.fill('0');
		cout << "Case #" << i+1 << ": " << setw(4) << dp[0] << endl;
	}
	return 0;
}

