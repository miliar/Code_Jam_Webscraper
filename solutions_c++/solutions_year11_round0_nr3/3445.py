#include <iostream>

#define LIMIT 1000000
#define ERROR "NO"

using namespace std;

typedef long long integer;

int main()
{
	int n, t, c, equal, min;
	integer sum;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		min = LIMIT + 1;
		equal = 0;
		sum = 0;
		cin >> n;
		for (int j = 0; j < n; j++)
		{
			cin >> c;
			sum += c;
			equal ^= c;
			if (c < min)
				min = c;
		}
		sum -= min;
		if (equal == 0)
			cout << "Case #" << i+1 << ": " << sum << endl;
		else
			cout << "Case #" << i+1 << ": " << ERROR << endl;
	}
	return 0;
}
