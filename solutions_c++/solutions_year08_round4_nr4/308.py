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
	int k;
	string S;
	cin >> k >> S;
	int res = INFTY;
	_vi p(k);
	REP(i,k) p[i] = i;

	do{
		string x;
		x.append(S);
		REP(i,S.size()/k) REP(j,k){
			x[i*k + j] = S[i*k + p[j]];
		}

		int z = 1;
		FUP(i,1,x.size()-1)
			if(x[i] != x[i-1])
				z++;
		res = min(res,z);
	}
	while(next_permutation(ALL(p)));
	cout << "Case #" << cs << ": " << res << endl;
}

int main(){
	int N;
	cin >> N;
	REP(i,N) do_it(i+1);
	return 0;
}

