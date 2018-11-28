#include<cstdio>
#include<iostream>
#include<sstream>
#include<string>
using namespace std;
#define GI ({int t;scanf("%d",&t);t;})

int check(int n, int m) {
	stringstream sstm1, sstm2;
	sstm1 << n;
	sstm2 << m;
	string N,M;
	sstm1 >> N;
	sstm2 >> M;
	
	if(N.size() < 2)
		return 0;
	string tmp;
	for(int i = 1;i < N.size();++i) {
		tmp = N.substr(i) + N.substr(0,i);
		if(tmp == M)
			return 1;
	}
	return 0;
}

int main() {
	int T = GI,A,B;

	for(int t = 0;t < T;++t) {
		A = GI, B = GI;
		int tot = 0;
		for(int n = A;n <= B;++n){
			for(int m = n+1;m <= B;++m) {
				tot += check(n,m);
			}
		}
		printf("Case #%d: %d\n", t+1, tot);
	}

	return 0;
}

