# include <iostream>
# include <cstdio>
# include <cstdlib>
# include <algorithm>
# include <vector>
# include <string>
# include <cmath>

using namespace std;

long long LL[10000], A[4000000];

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int TT;
	
	cin >> TT;

	for(int tt = 1; tt <= TT; tt++){
		int P,K,L;

		cin >> P >> K >> L;

		for(int i = 0; i < L; i++) cin >> LL[i];

		sort(LL, LL+L);
		int pos = 0;

		for(int i = 0; i < K; i++ ){

			for(int k = 1; k <= P; k++) A[pos++] = k;
		}

		sort(A,A+pos);

		long long ans = 0;

		for(int i = 0; i < L; i++) ans += A[i]*LL[L-i-1];




		cout << "Case #" << tt << ": " << ans << endl;
	}

	


	return 0;
}