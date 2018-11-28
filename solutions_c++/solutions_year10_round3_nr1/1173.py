#include <iostream>
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int c=0; c<t; c++){
		int N;
		int A[1000];
		int B[1000];
		int inter = 0;
		cin >> N;
		for(int n=0; n<N; n++){
			int a,b;
			cin >> a;
			cin >> b;
			A[n] = a;
			B[n] = b;
		}
		for(int i=0; i<N; i++){
			for(int j=i+1; j<N; j++){
				if((A[i] < A[j] && B[i] > B[j]) || (A[i] > A[j] && B[i] < B[j]))
					inter++;
			}
		}
		cout << "Case #" << c+1 << ": " << inter << endl;
	}
}
