#include <iostream>
using namespace std;
int main(){
	
	int N;
	int K;
	int caseNum;
	
	cin >> caseNum;
	for(int i =0; i < caseNum; i++){
		cin >> N;
		cin >> K;

		int mi = 1u << N;
		int yu = mi - 1;
		if( K % mi == yu)
			cout << "Case #" << i+1 <<": ON" << endl;
		else
			cout << "Case #" << i+1 <<": OFF" << endl;
	}

	return 0;
}