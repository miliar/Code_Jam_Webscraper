#include <cstdio>
#include <vector>

using namespace std;

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 0;i < t;++i){
		int A, B;
		scanf("%d%d", &A, &B);
		vector<double> v;
		double p = 1;
		for(int h = 0;h < A;++h){
			double x;
			scanf("%lf", &x);
			v.push_back(x);
			p *= x;
		}
		double res = -1.0;
		//give up
		double r = B + 2;
		res = r;
		//complete
		r = p * (B-A+1) + (1-p) * (2*B-A+1);
		if(res > r) res = r;
		
		p = 1;
		for(int h = 1;h <= A;++h){
			p *= v[h-1];
			r = 2*(A-h) + (B-A+1) * p + (B-A+1 + B+1) * (1-p);
			if(res > r) res = r;
		}
		printf("Case #%d: %f\n", i+1, res);
	}

	return 0;
}
