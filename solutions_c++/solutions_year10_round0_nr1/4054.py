#include<iostream>
using namespace std;

int main()
{
	int cases = 0;
	cin >> cases;
	
	int N = 0, K = 0;
	for(int i = 1; i <= cases; i++)
	{
		cin >> N >> K;
		cout << "Case #" << i << ": ";
		int mask = ((1 << N) - 1);
		//cout << mask << endl;
		//cout << (K & mask) << endl;
		if((K & mask) == mask)
			cout << "ON" << endl;
		else
			cout << "OFF" << endl;
	}
	
	
	return 0;
}