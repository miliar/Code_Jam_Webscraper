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

#define INF 1000000000
#define PB push_back
#define ALL(v) (v).begin(),(v).end()
#define FUP(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define REP(i,n) for(int (i)=0;(i)<(n);(i)++)
#define FDN(i,a,b) for(int (i)=(a);(i)>=(b);(i)--)
#define PRINT(v) FORS(i,v) cerr<<v[i]<<" "; cerr<<endl;
#define FORS(i,a) for(int (i)=0;(i)<(int)(a).size();(i)++)

_vi revr;

// k*a + l*b = GCD(a,b)
int ExtGCD(int a, int b, int &k, int &l){
	if(!b){ k=1; l=0; return a; }
	int k1,l1;
	int d = ExtGCD(b, a%b, k1, l1);
	k = l1; l = k1 - (a/b)*l1;
	return d;
}

int SolveLinEq(int a, int b, int n){
        int k,l;
	int d = ExtGCD(a,n,k,l);
	return b%d?-1:(((b/d)*k)%n+n)%n;
}

int newton(int N, int K){
	K = min(K,N-K);
	int res = 1;
	FUP(i,N-K+1,N){ res *= i; res %= 10007; }
	FUP(i,1,K){ res *= revr[i]; res %= 10007; }
	return res;
}

int paths(int x, int y){
	if(x > y) swap(x,y);
	if(y > 2*x - 1) return 0;
	if((x+y) % 3 != 2) return 0;
	int N = (x+y-2) / 3;
	int K = abs((N*2+1) - x);
	return newton(N,K);
}

void do_it(int cs){
	int H,W,R;
	cin >> H >> W >> R;
	vector<pair<int,int> > rocks(R);
	FORS(i,rocks) cin >> rocks[i].first >> rocks[i].second;
	int res = paths(H,W);
	FUP(mask,1,(1<<R)-1){
		vector<pair<int,int> > tmp;
		REP(i,R){
			if( (mask & 1 << i) != 0 ){
				tmp.PB(rocks[i]);
			}
		}
		sort(ALL(tmp));

		bool c = true;
		FUP(j,1,tmp.size()-1){
			if(tmp[j].first <= tmp[j-1].first || tmp[j].second <= tmp[j-1].second){
				c = false;
				break;
			}
		}

		if(!c) continue;

		int wyn = paths(tmp[0].first, tmp[0].second);
		FUP(j,1,tmp.size()-1){
			wyn *= paths(tmp[j].first - tmp[j-1].first + 1, tmp[j].second - tmp[j-1].second + 1);
			wyn %= 10007;
		}
		int ss = tmp.size() - 1;
		wyn *= paths(H - tmp[ss].first + 1, W - tmp[ss].second + 1);
		wyn %= 10007;

		res += (tmp.size() % 2 == 0 ? wyn : -wyn);
		res %= 10007;
	}
	res = (res + 10007 ) % 10007;
	cout << "Case #" << cs << ": " << res << endl;
}

int main(){
	revr.resize(10007);
	revr[0] = 0;
	FUP(i,1,10006) revr[i] = SolveLinEq(i,1,10007);
	int N;
	cin >> N;
	REP(i,N) do_it(i+1);
	return 0;
}

