#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	int t;
	freopen("B-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	cin >> t;

	for (int k = 1; k <= t; k ++)
	{
		cout << "Case #" << k << ": "; 
		vector <int> arr;
		string s;
		cin >> s;
		arr.resize(s.length());
		for (int i = 0 ;i < s.length(); i ++)
			arr[i] = s[i]-'0';
		vector <int> arr2;
		arr2 = arr;
		next_permutation(arr2.begin(), arr2.end());
		if (arr2 > arr)
		{
			for (int i = 0; i < arr2.size(); i ++)
				cout << arr2[i];
			cout << endl;
		}
		else
		{
			sort(arr.begin(), arr.end());
			int an = 0;
			for (int i = 0; i < arr.size(); i ++)
				if (arr[i] != 0)
				{
					an = i;
					break;
				}
			cout << arr[an];
			cout << "0";
			for (int i =0 ; i < arr.size(); i ++)
				if (i != an)
					cout << arr[i];
			cout << endl;
		}
	}
	return 0;
}