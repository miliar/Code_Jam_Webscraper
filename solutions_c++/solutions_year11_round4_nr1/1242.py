#include <cstdio>
#include <vector>

using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for(int tt=0;tt<t;tt++) {
		int x,s,r,n;
		double rt;
		scanf("%d %d %d %lf %d",&x,&s,&r,&rt,&n);
		r-=s;
		vector<double> bucket(400);
		for(int i=0;i<n;i++){
			int b,e,bo;
			scanf("%d %d %d",&b,&e,&bo);
			x-=e-b;
			bucket[bo+s]+=e-b;
		}
		bucket[s]+=x;
		double totTime=0;
		for(int i=0; i<400;i++) {
			if (bucket[i] <= (r+i)*rt) {
				rt -= bucket[i]/((double)r+i);
				totTime += bucket[i]/((double)r+i);
			} else {
				bucket[i] -= (r+i)*rt;
				totTime += rt;
				rt=0;
				totTime += bucket[i]/(double)i;
			}
		}
		printf("Case #%d: %.8lf\n",tt+1,totTime);
	}
	return 0;
}
