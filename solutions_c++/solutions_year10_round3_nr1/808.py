#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include<cstring>

using namespace std;

#define FOR(i, a, b) for (int (i) = (a), _b = (b); (i) < _b; ++(i))
#define REP(i, N) FOR(i, 0, N)
#define ALL(x) (x).begin(), (x).end()
#define mp(a, b) make_pair(a,b)
#define px(x) push_back(x)

typedef vector<int> VI;
typedef pair<int, int> PII;
typedef long long LL;
typedef vector<string> VS;

int main(){
	int T;
	cin >> T;

	FOR (kase, 1, T + 1) {
		vector<PII> pos;
		int N;
		cin>>N;
		int i,j;
		REP(i,N){
			int t1, t2;
			cin>>t1>>t2;
			pos.px((mp(t1,t2)));
		}
		int count= 0;
		for(i=0;i<N;i++)
			for(j=i+1;j<N;j++){
				if((pos[i].first<pos[j].first && pos[i].second>pos[j].second) || (pos[i].first>pos[j].first && pos[i].second<pos[j].second) )
					count++;
			}
	cout << "Case #" << kase << ": " << count << endl;
	}
	//cin>>T;
	return 0;
}
