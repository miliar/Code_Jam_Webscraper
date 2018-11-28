#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<string>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<deque>
#include<complex>
#include<numeric>
using namespace std;
#define LL long long

LL gcd(LL a, LL b){
	return !b ? a : gcd(b, a%b);
}

int Solve() {
	LL N, A, B;
	cin >> N >> A >> B;
	if(B == 100) return A==100;
	//if(!A && B) return false;
	if(!A) return true;
	if(A && !B) return false;
	LL x = 100 * A / gcd(100, A);
	return x / A <= N;
}

int main() {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int test; scanf("%d", &test);
	for(int no=1;no<=test;++no){
		printf("Case #%d: ", no);
		if(Solve())printf("Possible\n");
		else printf("Broken\n");
	}
}
