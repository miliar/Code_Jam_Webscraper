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
#define FUP(i,a,b) for(_ll (i)=(a);(i)<=(b);(i)++)
#define REP(i,n) for(_ll (i)=0;(i)<(n);(i)++)
#define FDN(i,a,b) for(int (i)=(a);(i)>=(b);(i)--)
#define PRINT(v) FORS(i,v) cerr<<v[i]<<" "; cerr<<endl;
#define FORS(i,a) for(_ll (i)=0;(i)<(_ll)(a).size();(i)++)

const _ll MOD = 1000000007LL;

//Binary Indexed Tree (0-based)
class BITree{
public: vector<_ll> t;
BITree(int n){ t.resize(n,0LL); }
void add(int i, _ll v){
	i++;
	while(i<=(int)t.size()){t[i-1]+=v;t[i-1]%=MOD;i+=(i&-i);}
}
_ll sum(int i){
	_ll r=0LL;
	i++;
	while(i>0){r+=t[i-1];i-=(i&-i);}
	return r%MOD;
}};

void do_it(int cs){
	_ll n,m,X,Y,Z;
	cin >> n >> m >> X >> Y >> Z;

	vector<_ll> A(m);
	REP(i,m) cin >> A[i];

	vector<_ll> speed(n);
	REP(i,n){
		speed[i] = A[i % m];
		A[i % m] = (X * A[i % m] + Y * (i + 1LL)) % Z;
	}

	vector<_ll> alls(n);
	REP(i,n) alls[i] = speed[i];
	sort(ALL(alls));
	vector<_ll> uni;
	uni.PB(alls[0]);

	map<_ll,int> where;
	where[alls[0]] = 0;
	FUP(i,1LL,n-1LL)
		if(alls[i] != alls[i-1LL]){
			where[alls[i]] = static_cast<int>(uni.size());
			uni.PB(alls[i]);
		}

	int nn = static_cast<int>(uni.size());
	BITree tr(nn);

	REP(i,n){
		int w = where[speed[i]];
		if(w > 0)
			tr.add(w, tr.sum(w-1) + 1LL);
		else
			tr.add(w, 1LL);
	}

	cout << "Case #" << cs << ": " << tr.sum(nn-1)%MOD << endl;
}

int main(){
	int N;
	cin >> N;
	REP(i,N) do_it(i+1);
	return 0;
}

