#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <sstream>
#include <queue>

#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>

#define forn(i, n) for(int i=0;i<int(n);i++)
#define FOR(i, a, b) for(int i=(a);i<int(b);i++)
#define RFOR(i, b, a) for(int i=(b);i>int(a);i--)
#define foreach(it, c)  for(__typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define ALL(x)   (x).begin(),(x).end()
#define SIZE(x)   (int)(x).size()
#define SORT(x) sort(ALL(x))
using namespace std;
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define ISS istringstream
#define OSS ostringstream
typedef long long ll;
ll N, M, A;

int main(){
	int i,j ,k;
	int casos; 
	scanf("%i", &casos);
	for(int h = 0 ;h < casos;  h ++ ){
	scanf("%lld %lld %lld\n", &N, &M, &A);
	int listo = 0;
for(i=0;i<=M&&!listo;i++)for(int x1 = 0; x1 <=N && !listo; x1++)for(int x2=x1;x2<=N&&!listo;x2++){
			for(int y1=0;!listo&&y1<=M;y1++)for(int y2 = 0;!listo&& y2 <= M ; y2++){
				int area = abs(x1*(y2-i)-x2*(y1-i));
				if( area == A ){
					printf("Case #%i: %i %i %i %i %i %i\n", h+1,0,i,x1,y1,x2,y2);
					listo = 1;
				}
			}
		}
		if( !listo ) printf("Case #%i: IMPOSSIBLE\n",h+1);
		int vale = 0;
	}
	return 0;
}


























