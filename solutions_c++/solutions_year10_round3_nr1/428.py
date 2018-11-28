#include <iostream>
#include <string>
#include <vector>
#include <cstdio>
using namespace std;
int T, N;
int A[1100], B[1100];
bool inter(int x, int y){
	if(A[x]>A[y]&&B[x]<B[y])
		return 1;
	if(A[x]<A[y]&&B[x]>B[y])
		return 1;
	return 0;
}
int main(){
	cin >> T;
	for(int z=1; z<=T; z++){
		cin >> N;
		for(int i=1; i<=N; i++){
			cin >> A[i];
			cin >> B[i];
		}
	
	int result = 0;
	for(int i=1; i<=N-1; i++)
		for(int j=i+1; j<=N; j++)
			result +=inter(i, j);
	cout << "Case #" <<z <<": " << result <<endl;
	}

	return 0;
}


