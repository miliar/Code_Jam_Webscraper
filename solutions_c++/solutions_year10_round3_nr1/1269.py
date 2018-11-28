#include <iostream>

using namespace std;

int main() {
	int T, N;
	int A[1000], B[1000];
	int diff[1000];
	
	cin >> T;
	for(int t=0; t<T; t++) {
		cin>>N;
		
		for(int i=0; i<N; i++) {
			cin>>A[i]>>B[i];
			diff[i] = B[i] - A[i];
		}
		
		int nIntersections = 0;
		for(int i=0; i<N-1; i++) {
			for(int j=i+1; j<N; j++) {
				int den = diff[i] - diff[j];
				//cerr<<i<<", "<<j<<": "<<den<<endl;
				
				if(den != 0) {
					double x = ((double)(A[j] - A[i])) / den;
					double y = A[i] + diff[i] * x;
					
					//cerr<<"y = "<< y<<", x = "<<x<<endl;
					if(x >= 0 && x <= 1)
						nIntersections++;
				}
			}
		}
		
		cout<<"Case #"<<(t+1)<<": "<<nIntersections<<endl;
	}
}
