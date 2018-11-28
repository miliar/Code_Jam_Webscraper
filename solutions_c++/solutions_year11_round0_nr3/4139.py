#include <iostream>
#include <stdio.h>
using namespace std;

int main ()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
 int T, N, sum = 0, min = 1000*1001, digSum = 0, x;
 cin >> T;
 for (int i = 0; i < T; i++)
 {
	cin >> N;
	for(int j = 0; j < N; j++)
	{
		cin >> x;
		digSum = digSum ^ x;
		sum += x;
		if(x < min) min = x;
	}
	if(digSum)
		cout << "Case #" << i+1 << ": " << "NO"  << endl;
	else
		cout << "Case #" << i+1 << ": " << sum - min  << endl;
	digSum = sum = 0;
	min = 1000*1001;
 }
}