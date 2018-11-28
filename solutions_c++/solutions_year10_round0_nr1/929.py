#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;

int main()
{
	int tcase;
	cin >> tcase;
	for(int i = 1; i <= tcase; i++)
	{
		cout << "Case #" << i << ": ";
		int N,K;
		cin >> N >> K;
		int stat = K%((1<<N));
		if(stat==((1<<N)-1))cout << "ON" << endl;
			else cout << "OFF" << endl;
	}
	return 0;
}