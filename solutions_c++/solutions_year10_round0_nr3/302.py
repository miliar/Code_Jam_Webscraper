#include <iostream>
#include <cstring>
#include <map>
using namespace std;

#define MAX 1100
typedef long long int Lint;
Lint r, k, n;
Lint q[MAX], s[MAX];
Lint front = 0;
map<Lint, bool> m;
map<Lint, Lint> mc;
map<Lint, Lint> cm;

int main(){

	//freopen("test", "r", stdin);
	//freopen("out", "w", stdout);
	Lint cases, c = 0;
	scanf("%lld", &cases);
	while(cases--){
		memset(q, 0, sizeof(q));
		memset(s, 0, sizeof(s));
		m.clear();
		mc.clear();
		cm.clear();
		scanf("%lld %lld %lld", &r, &k, &n);
		for(int i = 1;i <= n; i++){
			scanf("%d", &q[i]);
		}

		front = 1;
		Lint cycle = 0;
		Lint last = 0;
		Lint start = 0;
		Lint sum = 0;
		for(cycle = 0;; cycle++){
			if(m[front])break;
			m[front] = true;

			Lint v = 0, cc = 0;
			start = front;
			while(v + q[front] <= k){
				cc++;
				if(cc>n)break;
				v += q[front];
				if(front + 1 > n)front = 1;
				else	front = front + 1;
			}

			s[start] = s[last] + v;
			mc[cycle+1] = s[start];
			cm[start] = cycle+1;
			last = start;
			//printf("%d %d %d\n", cm[start], start, mc[cycle+1]);
		}
		Lint bec = mc[cm[front]-1];
		Lint cyclev = mc[cycle] - bec;
		Lint cyc = cycle - cm[front] + 1;
		if(	r < cm[front])printf("Case #%lld: %lld\n", ++c, mc[r]);//??
		else{
			sum = bec;
			//printf("%d\n", cyc);
			//printf("%d\n", sum);
			r -= (cm[front]-1);
			sum += (r / cyc * cyclev);
			//printf("%d\n", sum);
			sum += (mc[cm[front] + (r%cyc) - 1] - bec);
			//printf("%d\n", sum);
			printf("Case #%lld: %lld\n", ++c, sum);
		}
	}
	return 0;
}
