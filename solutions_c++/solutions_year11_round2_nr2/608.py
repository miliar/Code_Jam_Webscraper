#include <math.h>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

class vendor {
public:
	int p;
	int v;
};

vector<vendor> v;

bool cmp(vendor a, vendor b) {
	return a.p < b.p;
}

int main() {

	int T, C, D;
	scanf("%d", &T);

	for(int q=0;q<T;q++) {
		scanf("%d %d", &C, &D);
		v.clear();
		vendor t;
		int pp, vv;
		for(int i=0;i<C;i++) {
			scanf("%d %d", &pp, &vv);
			t.v = vv;
			t.p = pp;
			v.push_back(t);
		}
		sort(v.begin(), v.end(), cmp);
		
		double low =  0;
		double high = 200000;
		for(;;) {
			if(fabs(high - low) < 1e-8)
				break;
			double x = (low + high) / 2.0;
			// x 초 안에 가능한가?

			double before = v[0].p - x;
			bool flag = false;

			for(int i=0;i<C;i++) {
				for(int j=0;j<v[i].v;j++) {
					if(i==0 && j ==0)
						continue;
					if(before + D < v[i].p) {
						// 왼쪽으로 움직임
					double able = v[i].p - x;
					if(before + D > able) {
						before = before + D;
					} else {
						before = able;
					}} else {
						// 오른쪽으로
						double able = v[i].p + x;
						if(before + D < able) {
							before = before + D;
						} else {
							flag = true;
							break;
							// impossible;
						}
					}
				}
				if(flag)
					break;
			}

			if(!flag) {
				// 가능하면 x를 줄여보자
				high = x;
			} else {
				low = x;
			}
			
		}
		printf("Case #%d: %lf\n", q+1, low);

	}

	return 0;
}
