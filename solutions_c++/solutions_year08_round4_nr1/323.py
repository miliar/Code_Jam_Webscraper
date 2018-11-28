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

void do_it(int cs){
	int M,V;
	cin >> M >> V;
	_vi gate(M);
	_vi chg(M);
	_vi val0(M);
	_vi val1(M);

	REP(i,(M-1)/2){
		cin >> gate[i] >> chg[i];
	}
	FUP(i,(M-1)/2, M-1){
		int v;
		cin >> v;
		val0[i] = (v==0?0:INF);
		val1[i] = (v==1?0:INF);
	}
	FDN(i,(M-1)/2-1,0){
		val0[i] = INF;
		val1[i] = INF;
		// AND
		if(gate[i] == 1 || chg[i] == 1){
			int c = 0;
			int a = i*2 + 1;
			int b = a +1;
			if(gate[i] == 0) c = 1;
			val0[i] = min(val0[i], val0[a] + val0[b] + c);
			val0[i] = min(val0[i], val0[a] + val1[b] + c);
			val0[i] = min(val0[i], val1[a] + val0[b] + c);
			val1[i] = min(val1[i], val1[a] + val1[b] + c);
		}
		// OR
		if(gate[i] == 0 || chg[i] == 1){
			int c = 0;
			int a = i*2 + 1;
			int b = a +1;
			if(gate[i] == 1) c = 1;
			val0[i] = min(val0[i], val0[a] + val0[b] + c);
			val1[i] = min(val1[i], val0[a] + val1[b] + c);
			val1[i] = min(val1[i], val1[a] + val0[b] + c);
			val1[i] = min(val1[i], val1[a] + val1[b] + c);
		}
	}


	cout << "Case #" << cs << ": ";

	if(V==0){
		if(val0[0] >= INF)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << val0[0] << endl;
	}
	else{
		if(val1[0] >= INF)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << val1[0] << endl;
	}
}

int main(){
	int N;
	cin >> N;
	REP(i,N) do_it(i+1);
	return 0;
}

