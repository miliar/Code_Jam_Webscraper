#include <iostream>
#include <cassert>
#include <vector>
using namespace std;
typedef long long i64;
#define fu(i,m,n) for(int i=m; i<n; i++)

i64 fit(vector<int>& g, i64 sum, int k, int pos, int& pos2) {
	if(k>=sum) {
		pos2=pos;
		return sum;
	}
	i64 money = 0;
	pos2 = pos;
	while(k>=g[pos2]) {
		k-=g[pos2];
		money += g[pos2];
		pos2=(pos2+1)%g.size();
		//if(pos2==pos) break;
	}
	return money;
}

int main(void) {
	int T;
	cin >> T;
	fu(t,0,T) {
		int R,k,N;
		cin >> R >> k >> N;
		vector<int> g(N);
		fu(i,0,N) cin >> g[i];
		i64 sum=0;
		fu(i,0,N) sum+=g[i];

		int pos = 0, pos2;
		vector<i64> ms(N,-1);
		vector<int> npos(N);

		i64 ret=0;

		while(ms[pos]==-1 && R) {
			ms[pos] = fit(g, sum, k, pos, pos2);
			ret += ms[pos];
			npos[pos]=pos2;
			pos = npos[pos];
			R--;
		}
		int pos1 = pos;

		i64 sum2 = 0;
		int ll = 0;
		do {
			sum2 += ms[pos];
			pos = npos[pos];
			ll++;
		} while(pos!=pos1);

		i64 r = R/ll;
		ret += r*sum2;
		R -= r*ll;
		pos=pos1;
		while(R) {
			ret += ms[pos];
			pos = npos[pos];
			R --;
		}

		cout << "Case #" << t+1 << ": " << ret << endl;
	}
}
