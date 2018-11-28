
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
#define REP(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FDN(i,a,b) for(int (i)=(a);(i)>=(b);(i)--)
#define PRINT(v) FORS(i,v) cerr<<v[i]<<" "; cerr<<endl;
#define FORS(i,a) for(int (i)=0;(i)<(int)(a).size();(i)++)

void do_it(int cs){
	_ll P,K,L;
	cin >> P >> K >> L;
	vector<_ll> freq(L);
	REP(i,L) cin >> freq[i];
	sort(ALL(freq));
	reverse(ALL(freq));
	_ll res = 0LL;

	_ll cnt = 0;
	for(_ll i = 1; cnt < L; i++)
		for(_ll j = 0; j < K && cnt < L; j++){
			res += freq[cnt] * i;
			cnt ++;
		}
	cout << "Case #" << cs << ": " << res << endl;
}

int main(){
	int N;
	cin >> N;
	REP(i,N) do_it(i+1);
	return 0;
}

