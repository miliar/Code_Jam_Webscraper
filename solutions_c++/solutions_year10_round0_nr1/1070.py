#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++)
	{
		long long N, K;
		cin >> N >> K;
		int mask = 1ll<<N;
		mask--;
		
		if((K & mask) == mask)
			cout << "Case #" << i << ": ON" << endl;
		else
			cout << "Case #" << i << ": OFF" << endl;

	}
}