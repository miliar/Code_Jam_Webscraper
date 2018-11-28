#include <iostream>
#include <algorithm>

using namespace std;

bool count(long long A, long long B){
	if( A < B) return count(B,A);
	if( B == 0) return true;
	if( A == 1) return false;
	if(A/B >= (2-1e-14)) return true;
	else return !(count(B,A-B));
}

int main(){
	int T;
	cin >> T;
	for(int tell = 1; tell <= T; tell++){
		long long A1,A2,B1,B2;
		cin >> A1 >> A2 >> B1 >> B2;
		long long total = 0;
		for(int a = A1; a <= A2; a++){
			for(int b = B1; b <= B2; b++){
				total += count(a,b);
			}
		}
		cout << "Case #" << tell << ": " << total << endl;
	}
}
