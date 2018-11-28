// (c) Copyright 2010 Jianfeng Hu. All Rights Reserved. 

#include <iostream>
#include <string>
using namespace std;

int main() {
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		int n, k;
		cin >> n >> k;
		int base = (1 << n) - 1;
		k %= (1 << n);
		if ((k ^ base) == 0)
			cout << "ON" << endl;
		else
			cout << "OFF" << endl;
	}
}
