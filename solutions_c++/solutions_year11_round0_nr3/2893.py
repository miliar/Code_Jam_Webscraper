#include<algorithm>
#include<vector>
#include<list>
#include<deque>
#include<queue>
#include<iostream>
#include<cctype>
#include<cmath>
#include<iterator>
#include<cstdlib>
#include<sstream>
#include<cstdio>
#include<cassert>
#include<climits>
#include<string>
#include<map>
#include<set>
#include<stack>
#include<numeric>
#include<complex>
#include<valarray>

#define FOR(i,a,b) for(int i=a; i<b; i++)
#define F(i,n) for(int i=0; i<n; i++)
#define VI vector<int>
#define pb(a) push_back(a)
#define pf(a) push_front(a)
#define LL long long


using namespace std;

int mx= -1;

void findMax(int ind, VI &v, int sXor, int sScore, int pXor, int pScore) {
	if(ind == v.size()) {
		if(sXor == pXor && pScore != 0) {
			mx = max(mx,sScore);
		}
		return;
	}
	else {
		findMax(ind+1,v,sXor^v[ind],sScore+v[ind],pXor,pScore);
		findMax(ind+1,v,sXor,sScore,pXor^v[ind],pScore+v[ind]);
	}
}

int main() {
	int N; cin>>N;
	int caseN=0;
	while(N--) {
		caseN++;
		int n;
		cin >> n;
		VI v(n);
		F(i,n) {
			cin >> v[i];
		}
		findMax(0,v,0,0,0,0);
		if(mx == -1) {
			cout << "Case #" << caseN << ": " << "NO" << endl;
		}
		else {
			cout << "Case #" << caseN << ": " << mx << endl;
		}
		mx = -1;
	}	
	return 0;
}
