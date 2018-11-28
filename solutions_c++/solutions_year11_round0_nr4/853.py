#include <iostream>
#include <algorithm>
#include <utility>
#include <limits.h>

using namespace std;

int input[2000];

long long fact[1000];
double E[2000];
double P[2000];

int main() {
	int T;
	cin >> T;
	
	// prepare
	fact[0]=1;
	for(int i=1; i<=1000; i++) {
		fact[i]=fact[i-1]*i;
		if(i>20) fact[i]=LLONG_MAX;
	}
	
	P[0] = 1;
	P[1] = 0;
	for(int i=2; i<=1000; i++) {
		P[i]=0;
		for(int k=2; k<=i; k++) {
			if(k%2==0) P[i] += 1.0/fact[k];
			else P[i] -= 1.0/fact[k];
		}
	}
	
	E[0] = 0.0;
	E[1] = 0.0;
	E[2] = 2.0;
	for(int i=3; i<=1000; i++) {
		E[i]=0;
		for(int j=0; j<=i; j++) { // jコ揃う
			E[i] += P[i-j]/fact[j]*(E[i-j]+1);
		}
		E[i] /= (1-P[i]);
	}
	
	// solve
	for(int t=1; t<=T; t++) {
		int N;
		cin >> N;
		double sum=0.0;
		for(int i=0; i<N; i++) {
			int tmp;
			cin >> tmp;
			input[tmp]=i;
			if(i+1!=tmp) sum+=1.0;
		}
		cout << "Case #" << t << ": " << sum << endl;
	}
	
	return 0;
}
