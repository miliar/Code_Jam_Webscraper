#include <iostream>
#include <algorithm>
#include <cstring>
#include <climits>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <set>
using namespace std;
double W[105];
int main() {
	int T;
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn) {
		int X,S,R,N;
		double t, ans = 0;
		scanf("%d%d%d%lf%d",&X,&S,&R,&t,&N);
		memset(W,0,sizeof(W));
		W[0] = X;
		for(int i=0;i<N;++i) {
			int b,e,w;
			scanf("%d%d%d",&b,&e,&w);
			W[w] += (e-b);
			W[0] -= (e-b);
		}
		for(int i=0;i<=100;++i) {
			double rt = W[i]/(i+R);
			if(rt <= t) {
				ans += rt;
				t -= rt;
			}
			else {
				// calc when to stop running
				double d = t*(i+R);
				ans += t + (W[i]-d)/(i+S);
				t = 0;
			}
		}
		printf("Case #%d: %.8lf\n",cn,ans);
	}
}
