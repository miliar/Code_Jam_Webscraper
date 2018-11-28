#include <iostream>
using namespace std;

bool equiv(int n1, int n2)
{
	int count1[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	int count2[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	
	while (n1 > 0) {
		++count1[n1 % 10];
		n1 /= 10;
	}
	
	while (n2 > 0) {
		++count2[n2 % 10];
		n2 /= 10;
	}
	
	for (int i = 1; i < 10; i++) {
		if (count1[i] != count2[i]) return false;
	}
	
	return true;
}

int T, N, N2;

int main()
{
	cin >> T;
	
	for (int i = 1; i <= T; i++) {
		cin >> N;
		N2 = N+1;
		
		while (! equiv(N, N2)) ++N2;
		
		cout << "Case #" << i << ": " << N2 << endl;
	}

	return 0;
}
