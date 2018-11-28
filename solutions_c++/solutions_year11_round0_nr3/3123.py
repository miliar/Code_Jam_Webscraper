#include <iostream>
using namespace std;

long long caramelle[1010];
long long T, N, sum, xorsum, minvalue;

int main() {

	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		minvalue = 1000001l;
		cin >> N;
		for (int j = 0; j < N; j++)
		{
			cin >> caramelle[j];
			minvalue = caramelle[j] < minvalue ? caramelle[j] : minvalue;
		}
		sum = caramelle[0]+caramelle[1];
		xorsum = caramelle[0]^caramelle[1];
		for (int j = 2; j < N; j++)
		{
			sum += caramelle[j];
			xorsum = xorsum^caramelle[j];
		}
		cout << "Case #" << i << ": ";
		if (xorsum != 0) cout << "NO" << endl;
		else cout << (sum - minvalue) << endl;
	}
	return 0;
}
