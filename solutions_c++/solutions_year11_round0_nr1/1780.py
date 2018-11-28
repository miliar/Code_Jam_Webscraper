#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
using namespace std;
typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); --x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)x.size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second

const int N = 1000010;
int n;
vector<pair<int,int> > kol[2];

main(){
	int t;
	cin >> t;
	FOR(q,1,t){
		string pom;
		int poz;
		// O - 0, B - 1
		cin >> n;
		FOR(w,1,n){
			cin >> pom >> poz;
			if(pom[0] == 'O')
				kol[0].PB(make_pair(poz,w));
			else
				kol[1].PB(make_pair(poz,w));
		}
		kol[0].PB(make_pair(0,n+1));
		kol[1].PB(make_pair(0,n+1));
		int wyn = 0;
		int pO = 1, pB = 1;
		int kt =1;
		int wskO = 0, wskB = 0;
		while(kt <= n){
			if(kol[0][wskO].ND < kol[1][wskB].ND){
				int ile = abs(pO - kol[0][wskO].ST) + 1;
				wyn += ile;
				pO = kol[0][wskO].ST;
				if(ile >= abs(pB - kol[1][wskB].ST))
					pB = kol[1][wskB].ST;
				else{
					if(kol[1][wskB].ST > pB)
						pB += ile;
					else
						pB -= ile;
				}
				wskO++;
			}
			else{
				int ile = abs(pB - kol[1][wskB].ST) + 1;
				wyn += ile;
				pB = kol[1][wskB].ST;
				if(ile >= abs(pO - kol[0][wskO].ST))
					pO = kol[0][wskO].ST;
				else{
					if(kol[0][wskO].ST > pO)
						pO += ile;
					else
						pO -= ile;
				}
				wskB++;				
			}
			kt++;
		}
		cout << "Case #" << q << ": " << wyn << endl;
		kol[0].clear();
		kol[1].clear();
	}
	return 0;
}
