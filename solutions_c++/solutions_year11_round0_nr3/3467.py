// q.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <iostream>
#include <set>
#include <queue>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	
	for (int test = 1; test <= t; ++test) {
		int n;
		cin >> n;
		int sum = 0;
		int xsum = 0;
		int cur = 0;
		int mn = 10004000;
		for (int i = 0; i < n; ++i) {
			cin >> cur;
			sum += cur;
			mn = min(mn, cur);
			xsum=xsum^cur;
		}
		cout << "Case #"<<test<<": ";
		if (xsum != 0) {
			cout<<"NO";
		} 
		else {
			cout << sum - mn;
		}
		cout << endl;
	}

	return 0;
}
