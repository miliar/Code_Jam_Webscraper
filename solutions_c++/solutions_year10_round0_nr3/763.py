// By mirosuaf v.2.1 modified for CodeJam
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(f,w) ({ bool _ok=true; f _ok=_ok && (w); _ok; })
#define EXISTS(f,w) (!ALL(f,!(w)))
typedef long long LL;
const int INF = 1000000000;
const int MAXN = 2013;
typedef vector<int> VI; 

int main() {
	int ile;
	scanf("%d",&ile);
	FOR(iile,1,ile) {
        int r,k,n;
        VI v;
        scanf("%d%d%d",&r, &k, &n);
        REP(i, n) {
            int a;
            scanf("%d",&a);
            v.push_back(a);
        }
        vector<pair<int, int> > cmp; // Dla kazdego poczatku pamietam gdzie koncze i ile mam wyniku
        REP(i, n) {
            int curr = i, razy=0, sum=0;
            while (sum+v[curr]<=k && razy<n) {
                razy++;
                sum+=v[curr];
                curr++;
                if (curr==n) curr=0;
            }
            cmp.push_back(make_pair(curr, sum));
        }
 //       REP(i, n) cout <<"--> " <<  i << " " << cmp[i].first << "--> " << cmp[i].second << endl;
        LL wynik=0;
        int visited[MAXN]; REP(i, MAXN) visited[i] = -1;
        LL sumka[MAXN]; REP(i, MAXN) sumka[i] = 0;
        int prev_ruch[MAXN]; REP(i,MAXN) prev_ruch[i]=-1;
        int ruch=0, obecnie=0;
        bool done = false;

        while (!done) {

            if (visited[obecnie]!=-1) {
//                LL dodac = sumka[visited[obecnie]];
//                cout << "!! " << obecnie << " " << ruch+1 << " " << visited[obecnie] << endl;
                LL dlugosc = ruch+1-visited[obecnie];
                LL pozost = r - ruch;
//                cout << "Zostalo " << pozost << " " << dlugosc << endl;
                wynik+=(pozost/dlugosc)*(LL)(sumka[ruch]-sumka[visited[obecnie]-1]);
                pozost=pozost%dlugosc;
//                REP(i, 10) cout << sumka[i] << " "; cout << endl;
                REP(i,pozost) {
//                    cout << visited[obecnie]+i << " " << visited[obecnie]+i-1<< endl;
                    wynik+=sumka[visited[obecnie]+i]-sumka[visited[obecnie]+i-1];
//                    cout << wynik << endl;
                }
                done=true;
            } else {
                ruch++;
                visited[obecnie] = ruch;
                wynik+=cmp[obecnie].second;
                sumka[ruch] = wynik;
//                cout << obecnie << " " << cmp[obecnie].first << endl; 
                obecnie = cmp[obecnie].first;
                if (ruch==r) done = true;
            }
        }

		printf("Case #%d: %lld\n",iile, wynik);
	}
	return 0;
}

