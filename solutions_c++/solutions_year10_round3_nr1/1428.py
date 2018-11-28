#include <iostream>
using namespace std;

int main(){
	int N;
	int n;
	cin >> N;
	for(int i = 0; i < N; i++){
		int A[1001];
		int B[1001];
		cin >> n;

		for(int j = 0; j < n; j++){
			cin >> A[j];
			cin >> B[j];
		}
		
		int answer = 0;
		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
					if((A[i] - A[j]) * (B[i] - B[j]) < 0)
						answer ++;
			}
		}
		answer /= 2;
		cout << "Case #"<< i+1 << ": " << answer << endl;
	}
	return 0;
}