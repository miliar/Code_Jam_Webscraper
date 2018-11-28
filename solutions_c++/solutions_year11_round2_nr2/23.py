#include <stdio.h>
#include <algorithm>
using namespace std;

class DAT{
public:
	double P;
	int V;
	const bool operator < (const DAT &t)const {
		return P < t.P;
	}
} dat[201];
int T, n;
double s, e, m, D;
bool check(double m){
	double now;
	int i;
	for(i=0;i<n;i++){
		if(i == 0) now = dat[i].P - m;
		else{
			now = max(now, dat[i].P - m);
		}
		now += D * (double)dat[i].V;
		if(now - D > dat[i].P + m) break;
	}
	return (i == n);
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("result.txt","w",stdout);
	scanf("%d",&T);
	while(T>0){T--;
		int i;
		scanf("%d %lf",&n, &D);
		for(i=0;i<n;i++){
			scanf("%lf %d", &dat[i].P, &dat[i].V);
		}
		sort(dat, dat+n);

		s = 0.0;
		e = 1.0e18;
		while(e-s > e * 1.0e-12){
			m = (s + e) / 2;

			if(check(m)) e = m;
			else s = m;
		}
		


		static int cs = 1;
		printf("Case #%d: %.10lf\n", cs++, m);
		
	}
	return 0;
}