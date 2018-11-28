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
	cout << "Case #" << cs << ": ";
	_ll N,M,A;
	cin >> N >> M >> A;
	for(_ll x2 = 0; x2 <= N; x2++)
		for(_ll x3 = 0; x3 <= N; x3++)
			for(_ll y2 = 0; y2 <= M; y2++)
				for(_ll y3 = 0; y3 <= M; y3++)
					if(x3 * y2 - y3 * x2 == A){
						cout << "0 0 " << x2 << " " << y2 << " " << x3 << " " << y3 << endl;
						return;
					}
	cout << "IMPOSSIBLE" << endl;
}

int main(){
	int N;
	cin >> N;
	REP(i,N) do_it(i+1);
	return 0;
}

