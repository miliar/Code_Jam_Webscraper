#include <iostream>

int T;

using namespace std;


int num[1001];

void work(int cur)
{
	int n;
	int x = 0;
	cin >> n;
	int sum = 0;
	for (int i=1;i<=n;i++)
	{
		cin >> num[i];
		x ^= num[i];
		sum += num[i];
	}
	for (int i=1;i<=n;i++)
		for (int j=i+1;j<=n;j++)
			if (num[j] < num[i]) swap(num[i],num[j]);
	if (x != 0 )
		cout << "Case #" << cur << ": NO\n";
	else
	{
		cout << "Case #" << cur << ": " << sum - num[1] << endl;
	}
}

int main()
{
	int T;
	cin >> T;
	for (int i=1;i<=T;i++)
		work(i);
}
