/*
 * c.cpp
 *
 *  Created on: 2011-5-7
 *      Author: acer
 */


#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	int tn;
	cin >> tn;
	for (int ti = 1; ti <= tn; ++ti)
	{
		int n;
		cin >> n;
		int array[n];
		int t(0);
		int s(0);
		int min_value(100000000);
		for (int i = 0; i < n; ++i)
		{
			cin >> array[i];
			t ^= array[i];
			min_value = min(min_value, array[i]);
			s += array[i];
		}
		if (t != 0)
		{
			cout << "Case #" << ti << ": NO" << endl;
		}
		else
		{
			cout << "Case #" << ti << ": " << s - min_value << endl;
		}
	}
	return 0;
}
