#include <iostream>

using namespace std;

int main()
{
	//cout << "Hello!!!" << endl;
	//return 0;
	int T;
	const int maxN=1000;
	int C[maxN];

	cin >> T;
	for(int t=1; t<=T; t++){
		/************************************
		*	Input Data
		*************************************/
		int N;
		cin >> N;
		for(int i=0; i<N; i++)
			cin >> C[i];
		/************************************
		*	Solve the Problem
		*************************************/
		// Actually, the array is not needed
		int min=C[0], sum=C[0], IMPOSSIBLE=C[0];
		for(int i=1; i<N; i++)
		{
			IMPOSSIBLE^=C[i];
			sum+=C[i];
			if(min>C[i])
				min=C[i];
		}
		/************************************
		*	Output Results
		*************************************/
		cout << "Case #" << t << ": ";
		if(IMPOSSIBLE)
			cout << "NO"; 
		else
			cout << sum-min;
		cout << endl;
	}

	return 0;
}
