#include<iostream>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<sstream>
#include<utility>

using namespace std;
using namespace __gnu_cxx;

typedef long long _ll;
typedef vector<int> _vi;
typedef vector<vector<int> > _vvi;
typedef vector<string> _vs;
typedef istringstream _is;
typedef ostringstream _os;

#define INFTY 1000000000
#define PB push_back
#define ALL(v) (v).begin(),(v).end()
#define FUP(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define REP(i,n) for(_ll (i)=0;(i)<(n);(i)++)
#define FDN(i,a,b) for(int (i)=(a);(i)>=(b);(i)--)
#define PRINT(v) FORS(i,v) cerr<<v[i]<<" "; cerr<<endl;
#define FORS(i,a) for(_ll (i)=0;(i)<(_ll)(a).size();(i)++)

void do_it(int cs){
	string s;
	cin >> s;
	int hm = s.size()-1;
	_vi c(hm,0);

	_ll res = 0LL;

	// 0 - nothing; 1 - minus; 2 - plus
	while(true){
		int last = 2;
		_ll sum = 0LL, cur = 0LL;
		REP(i,hm){
			cur *= 10LL;
			cur += static_cast<_ll>(s[i]-'0');
			if(c[i] != 0){
				sum += (last==2?cur:-cur);
				last = c[i];
				cur = 0LL;
			}
		}
		cur *= 10LL;
		cur += static_cast<_ll>(s[hm]-'0');
		sum += (last==2?cur:-cur);

		if(sum % 2LL == 0LL || sum % 3LL == 0LL || sum % 5LL == 0LL || sum % 7LL == 0LL)
			res++;

		int g = -1;
		REP(i,hm) if(c[i] != 2){ g = i; break; };
		if(g==-1) break;
		c[g]++;
		REP(i,g) c[i] = 0;
	}

	cout << "Case #" << cs << ": " << res << endl;
}

int main(){
	int N;
	cin >> N;
	REP(i,N) do_it(i+1);
	return 0;
}

