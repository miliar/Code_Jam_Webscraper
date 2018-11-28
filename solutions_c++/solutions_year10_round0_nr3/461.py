#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <functional>
#include <numeric>

using namespace std;

typedef long long ll;

#define eps 1e-10
#define inf 0x3f3f3f3f

#define fr(x,y,z) for(int(x)=(y);(x)<(z);(x)++)
#define cast(x,t) *({stringstream ss;static t __ret;ss<<x,ss>>__ret;&__ret;})

#define dbg(x) cout << #x << " == " << x << endl
#define print(x) cout << x << endl

int G[1010], N;
long long R, K;
long long money[1010], tot;
int mark[1010];

int main() {
	
	int T;
	scanf("%d",&T);
	
	for(int i = 1; i <= T; i++) {
		printf("Case #%d: ",i);
		
		scanf("%lld %lld %d",&R,&K,&N);
		
		for(int i = 0; i < N; i++) {
			scanf("%d",&G[i]);
		}
		
		tot = money[0] = 0;
		memset(mark,0,sizeof(mark));
		
		long long pos = 0, tam = 0, add;
		
		for(long long i = 1; i <= R; i++) {
			
			if(mark[pos]) {				
				long long L = tam - mark[pos] + 1;
				long long resta = R - i + 1;
				
				tot += (money[tam] - money[mark[pos]-1]) * (resta / L);
				tot += (money[mark[pos]-1 +(resta)%L] - money[mark[pos]-1]);
				
				break;
			}
			
			mark[pos] = ++tam;
			add = 0;
			if(G[pos] <= K) {
				add = G[pos];
				int ant = pos;
				for(pos = (pos+1)%N; pos != ant && add + G[pos] <= K; pos = (pos+1) % N) {
					add += G[pos];
				}
			}
			
			tot += add;
			money[tam] = money[tam-1] + add;			
		}
		
		printf("%lld\n",tot);
		
	}
	
	return(0);
}
