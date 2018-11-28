#include <iostream>
	using namespace std;
#include <cmath>
	
int main(){
	long long int T, A1, A2, B1, B2, Case, i;
	double l, u;
	long long int ans;
	long long int L, U;
	l = (sqrt(5.0)-1)/2;
	u = (sqrt(5.0)+1)/2;
	cin >> T;
	for(Case = 1; Case <= T; ++Case){
		cin >> A1 >> A2 >> B1 >> B2;
		ans = 0;
		for(i = A1; i <= A2; ++i){
			L = (long long int)(i*l)+1;
			U = (long long int)(i*u);
			if(L > B1){
				if(U > B2 && L > B2)
					U = L-1;
				else if(U > B2 && L <= B2)
					U = B2;
			}
			else if(L <= B1 && U >= B1){
				L = B1;
				if(B2 < U)
					U = B2;
			}
			else{
				U = L-1;
			}
			ans += (U-L+1);
			//cout << i << "   "<<U << " " << L << endl;
		}
		//cout << ans << endl;
		cout << "Case #" << Case << ": " << (A2-A1+1)*(B2-B1+1)-ans << endl;
	}
	return 0;
}