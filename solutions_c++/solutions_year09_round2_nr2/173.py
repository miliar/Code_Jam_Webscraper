#include<iostream>
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

void run(int cs){
	cout << "Case #" << cs << ": ";
	string s;
	cin >> s;
	_vi tab(s.size(), 0);
	FORS(i,s) tab[i] = s[i] - '0';

	int n = s.size();
	FDN(i,n-2,0){
		if(tab[i] < tab[i+1]){
			int p = i+1;
			while(p+1 < n && tab[p+1] > tab[i])
				p++;
			swap(tab[i], tab[p]);
			sort(tab.begin() + (i+1), tab.end());
			REP(i,n) s[i] = tab[i] + '0';
			cout << s << endl;
			return;
		}
	}

	int p = -1;
	FDN(i,n-1,0)
		if(tab[i] > 0){ p = i; break; }
	if(p == -1) cout << "!" << endl;
	swap(tab[0], tab[p]);
	tab.PB(0);
	sort(tab.begin() + 1, tab.end());
	s.resize(tab.size());
	REP(i,tab.size()) s[i] = tab[i] + '0';
	cout << s << endl;
}

int main(){
	ios::sync_with_stdio(0);
	int C;
	cin >> C;
	REP(i,C) run(i+1);
	return 0;
}

