#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<cmath>
#include<map>
#include<cstdlib>
#include<string>
#include<cstring>
#include<utility>

using namespace std;

const double ERRO = 1e-7;

struct walkway {
	int b;
	int e;
	int w;
};

bool compare1(walkway w1, walkway w2) {
	return (w1.w < w2.w);
}

bool compare2(walkway w1, walkway w2) {
	return (w1.b < w2.b);
}

int main() {
	int T = 0;
	scanf("%d", &T);

	for(int caseNum = 1; caseNum <= T; caseNum++) {
		int x = 0, s = 0, r = 0, n = 0;
		double t = 0.0;
		scanf("%d %d %d %lf %d", &x, &s, &r, &t, &n);

//		if(caseNum == 40)
//			printf("x = %d; s = %d; r = %d; t = %lf; n = %d\n", x, s, r, t, n);

		vector< walkway > v;

		for(int i = 0; i < n; i++) {
			int b = 0, e = 0, w = 0;
			scanf("%d %d %d", &b, &e, &w);
			walkway walk;
			walk.b = b;
			walk.e = e;
			walk.w = w;
			v.push_back(walk);
		}

//		for(int i = 0; i < v.size(); i++)
//			printf("%d\n", i);

		sort( v.begin(), v.end(), compare2 );

//		printf("teste\n");

//		for(int i = 0; i < v.size(); i++)
//			printf("%d\n", i);

//		printf("teste 111\n");

		int total = v[0].e - v[0].b;

//		printf("teste 000\n");

		for(int i = 1; i < v.size(); i++)
			total += v[i].e - v[i].b;

		int without = x - total;

//		printf("teste 2\n");

		double myt = 0.0;
		double prev = ((double)without / (double)r);
		if(prev > t) {
			myt += t;
			myt += (((double)without - (double)(t*r)) / (double)s);
			t = 0.0;
		}
		else {
			t -= prev;
			myt += prev;
		}

//		printf("TIME 0 = %lf\n", myt);

		sort( v.begin(), v.end(), compare1 );

//		printf("teste 3\n");

		for(int i = 0; i < v.size(); i++) {
//			printf("t = %lf\n", t);

//			printf("%d\n", v[i].w);

			if(t > 0) {
				double prev = ((double)v[i].e - (double)v[i].b) / (double)(v[i].w + r);

				if(prev > t) {
					myt += t;
					myt += (((double)v[i].e - (double)v[i].b) - (t*(double)(v[i].w+r))) / (double)(v[i].w + s);
					t = 0.0;
				}
				else {
					t -= prev;
					myt += prev;
				}
			}
			else {
				myt += ((double)v[i].e - (double)v[i].b) / (double)(v[i].w + s);
			}

//			printf("TIME %d = %lf\n", i+1, myt);
		}

		printf("Case #%d: %.7lf\n", caseNum, myt);
	}

	return 0;
}
