#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

#define REP(i,a,b) for(int i=a;i<=b;i++)

int solve(int no) {
	long long N, L, H;
	long long f[10100];
	cin >> N >> L >> H;
	for(int i=0;i<N;i++) {
		cin >> f[i];
	}
	sort(f, f + N);
	
	long long ans = f[N-1]+1;
	for(int i=L;i<=H;i++) {
		int j;
		for(j=0;j<N;j++) {
			if(f[j]%i!=0 && i%f[j]!=0) break;
		}
		if(j==N) {
			cout << "Case #" << no << ": " << i << endl;
			return 0;
		}
	}
	
	cout << "Case #" << no << ": NO" << endl;
	return 1;
}

int main()
{
	int T;
	cin >> T;
	for(int no=1;no<=T;no++) {
		solve(no);
	}
	return 0;
}
