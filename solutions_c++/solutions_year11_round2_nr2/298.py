#include <cstdio>
#include <cstring>
#include <cassert>
#include <algorithm>

using namespace std;

pair<double, int> IN[200];

int main(){
	int tc, tcN;
	scanf("%d", &tcN);
	for(tc=0; tc<tcN; ++tc){
		int C;
		double D;
		scanf("%d %lf", &C, &D);
		for(int i=0; i<C; ++i){
			scanf("%lf %d", &IN[i].first, &IN[i].second);
		}
		sort(IN, IN+C);

		double a = 0;
		double o = 10e20;
		for(int k=0; k<300; ++k){
			double t = (o+a)/2;
			bool ok = true;

			double pos = IN[0].first - t - D;
			for(int i=0; i<C; ++i){
				pos = max(IN[i].first - t, pos + D);
				pos += (IN[i].second-1) * D;
				if(pos - IN[i].first > t){
					ok = false;
					break;
				}
			}
			if(ok){
				o = t;
			}else{
				a = t;
			}
		}

		printf("Case #%d: %.20lf\n", tc+1, a);
	}
}
