#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstdlib>


using namespace std;

#define sqr(a) ((a) * (a))

struct st {
	long long r;
	long long id;
	long long x;
	long long y;
};

long long clrand() {
	return (((long long)rand()) << 16) | ((long long) rand());
}

bool cmpr(st a, st b) {
	return a.r > b.r;
}

bool cmpid(st a, st b) {
	return a.id < b.id;
}

void solveone() {
	int n, w, l;
	vector<st> sts;

	cin >> n >> w >> l;

	sts.resize(n);

	for(int i = 0; i < n; i++) {
		cin >> sts[i].r;
		sts[i].id = i;
	}


	sort(sts.begin(), sts.end(), cmpr);

	for(int i = 0; i < sts.size(); i++) {
		bool isOk = false;
		while(!isOk) {
			sts[i].x = clrand() % w;
			sts[i].y = clrand() % l;	
			isOk = true;
			for(int j = 0; j < i; j++)
				if((sqr(sts[j].x - sts[i].x) + sqr(sts[j].y - sts[i].y)) < sqr(sts[i].r + sts[j].r)) {
					isOk = false;
					break;
				}
		}
		
	}


	sort(sts.begin(), sts.end(), cmpid);

	for(int i = 0; i < n; i++)
		printf("%lld %lld ", sts[i].x, sts[i].y);

}


int main() {
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solveone();
		printf("\n");
	}
}