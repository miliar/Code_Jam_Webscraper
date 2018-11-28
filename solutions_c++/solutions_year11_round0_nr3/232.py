#include <iostream>
#include <algorithm>

using namespace std;

int a[1002];

int main()
{
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		int N;
		cin >> N;
		for(int j=0;j<N;j++) cin >> a[j];
		int sum = 0;
		for(int j=0;j<N;j++) sum += a[j];
		sort(a, a+N);
		int exor = 0;
		for(int j=0;j<N;j++) exor ^= a[j];
		if(exor)
		{
			cout << "Case #" << i << ": " << "NO" << endl;
		}
		else
		{
			cout << "Case #" << i << ": " << (sum-a[0]) << endl;
		}
	}
	return 0;
}
