#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	int t, i, ans, C;
	double P, L;
	float temp;
	cin >> t;
	for ( i = 0; i < t; i ++)
	{
		cin >> L >> P >> C;
		temp = P / L;
		ans = 0;
		while (C < temp)
		{
			ans++;
			temp = sqrt(temp);
		}
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}