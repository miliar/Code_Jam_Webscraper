#include <iostream>

using namespace std;

int main()
{
	//cout << "Hello!!!" << endl;
	int T;

	cin >> T;
	for(int i=1; i<=T; i++){
		/************************************
		*	Input Data
		*************************************/
		unsigned int N, K;
		cin >> N >> K;
		/************************************
		*	Solve the Problem
		*************************************/
		// prepare a mask
		unsigned int MASK = 0xFFFFFFFF;
		MASK>>=N; MASK<<=N; MASK=MASK^0xFFFFFFFF;
		// check if all N low-order binary digits are 1
		int fl;
		K&=MASK; fl=(K==MASK);
		/************************************
		*	Output Results
		*************************************/
		cout << "Case #" << i << ": " << (fl? "ON" : "OFF") << endl;
	}

	return 0;
}
