//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

#define For(i, to) for(int i = 0; i<to; ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)
typedef long long ll;
typedef pair<ll, ll> pii;

int P[247], V[247];
int N,D, S, X, t;
ll pos, m;

int main(){
	scanf("%d", &t);
	For(T,t){
		scanf("%d %d", &N, &D);
		For(i, N) scanf("%d %d",P+i, V+i);
		S = 0;
		m = 0;
		For(i, N-1) P[i+1]-=P[0];
		P[0] = 0;
		X = -D;
		For(i, N){
			pos = X+D;
			X = max(ll(P[i]),pos);
			m = max(m, pos-P[i]);
			if (V[i]>1){
				pos = X+(V[i]-1)*D;
				X = max(ll(P[i]),pos);
				m = max(m, pos-P[i]);
			}
		}
		
		printf("Case #%d: %lf\n",T+1, double(m*0.5));
	}
	
}