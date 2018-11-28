
#include<algorithm>
#include<bitset>
#include<iostream>
#include<string>
#include<cstdio>
#include<sstream>
#include<vector>
#include<stack>
#include<deque>
#include<map>
#include<iterator>
#include<cmath>
#include<complex>
#include<queue>
#include<cassert>
#include<set>
#include<cstring>
#include<list>

#define FOREACH(it ,c ) for( typeof((c).begin()) it= (c).begin();it!=(c).end();++it) 
#define debug(x) cerr<< #x << " = " << x << "\n";
#define debugv(x) cerr<< #x << " = " ; FOREACH(it,(x)) cerr << *it << "," ; cerr<< "\n" ;
#define MP make_pair
#define PB push_back
#define siz(w) (int)w.size()
#define fup(i,st,ko) for(int i=st;i<=ko;i++)
#define fdo(i,st,ko) for(int i=st;i>=ko;i--)
#define REP(i,w) for(int i=0;i<siz(w);i++)
#define inf 100000000
using namespace std;

typedef long long ll;
int next[150][150];
int now[150][150];

int main(){
	int cas;
	cin >> cas;
	fup(test, 1, cas) {
		fup(j, 0, 110) fup(k, 0, 110) { next[j][k] = now[j][k] = 0; };
		int R;
		cin >> R;
		fup(j, 1, R) {
			int X1, Y1, X2, Y2;
			cin >> X1 >> Y1 >> X2 >> Y2;
			fup(p, Y1, Y2) fup(w, X1, X2) now[p][w] = 1;
		}
			
		int ile = 0;
		while(true) {
			int is = false;
			fup(p, 0, 100) fup(w, 0, 100) {
				if(now[p][w] == 1 && now[p - 1][w] == 0 && now[p][w - 1] == 0)
					next[p][w] = 0;
				else if(now[p][w] == 0 && now[p - 1][w] == 1 && now[p][w - 1] == 1) {
					next[p][w] = 1;
					is = true;
				}
				else {
					next[p][w] = now[p][w];
					if(now[p][w]) is = true;
				}
			}

			fup(p, 0, 100) fup(w, 0, 100) {
				now[p][w] = next[p][w];
				next[p][w] = 0;
			}
			ile ++;
			if(!is) break;
		}
		cout << "Case #" << test << ": " << ile << endl;
	}

return 0;
}
