#include <iostream>
#include <cmath>
using namespace std;

int main(void)
{
	int numCases;
	unsigned long long int N, K, max;
	
	cin >> numCases;
	for(int numCase = 1; numCase <= numCases; numCase++)
	{
		cin >> N >> K;
		
		max = pow(2, N);
		
		cout << "Case #" << numCase << ": ";
		
		if(K % max == max - 1) cout << "ON" << endl;
		else cout << "OFF" << endl;
	}
}
