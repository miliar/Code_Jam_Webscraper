#include <iostream>
#include <cstdio>
#include <cmath>
#include <fstream>

using namespace std;

bool process(int n, int k)
{
	int p = (int)pow(2.0,n);
	return ((k+1) % p ? false : true);
}

int main()
{
	int T;
	//fstream cin("A-small.in");

	cin >> T;
	
	for(int C=1;C<=T;C++)
	{
		int n, k;
		cin >> n >> k;
		cout << "Case #" << C << ": " << (process(n,k) ? "ON" : "OFF") << endl;
	}

	//cin.close();
	
	return 0;
}